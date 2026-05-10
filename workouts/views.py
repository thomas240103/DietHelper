from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from collections import defaultdict
from django.utils import timezone

from .forms import ExerciseBulkForm, WorkoutForm, WorkoutPlanForm
from .models import ExerciseLog, Workout, WorkoutPlan, WorkoutPlanExercise


def _parse_exercises(raw_text):
    exercises = []
    for index, line in enumerate(raw_text.splitlines(), start=1):
        parts = [part.strip() for part in line.split(",")]
        if not parts or not parts[0]:
            continue
        exercises.append(
            {
                "exercise_name": parts[0],
                "sets": int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0,
                "reps": int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else 0,
                "weight_kg": parts[3].replace(",", ".") if len(parts) > 3 and parts[3] else None,
                "order": index,
            }
        )
    return exercises


@login_required
def workouts_home(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "create_workout":
            workout_form = WorkoutForm(request.POST, user=request.user)
            exercise_form = ExerciseBulkForm(request.POST)
            if workout_form.is_valid() and exercise_form.is_valid():
                workout = workout_form.save(commit=False)
                workout.user = request.user
                workout.save()

                if workout.plan:
                    for plan_exercise in workout.plan.exercises.all():
                        ExerciseLog.objects.create(
                            workout=workout,
                            exercise_name=plan_exercise.exercise_name,
                            sets=plan_exercise.sets,
                            reps=plan_exercise.reps,
                            weight_kg=plan_exercise.weight_kg,
                        )

                for exercise in _parse_exercises(exercise_form.cleaned_data["exercises"]):
                    ExerciseLog.objects.create(
                        workout=workout,
                        exercise_name=exercise["exercise_name"],
                        sets=exercise["sets"],
                        reps=exercise["reps"],
                        weight_kg=exercise["weight_kg"],
                    )
                return redirect("workouts_home")

        if action == "create_plan":
            plan_form = WorkoutPlanForm(request.POST)
            exercise_form = ExerciseBulkForm(request.POST)
            if plan_form.is_valid() and exercise_form.is_valid():
                plan = plan_form.save(commit=False)
                plan.user = request.user
                plan.save()
                for exercise in _parse_exercises(exercise_form.cleaned_data["exercises"]):
                    WorkoutPlanExercise.objects.create(plan=plan, **exercise)
                return redirect("workouts_home")

        if action == "save_plan_session":
            plan = get_object_or_404(WorkoutPlan, id=request.POST.get("plan_id"), user=request.user)
            workout = Workout.objects.create(
                user=request.user,
                plan=plan,
                date=request.POST.get("date") or timezone.localdate(),
                workout_type="gym",
                duration_minutes=request.POST.get("duration_minutes") or 0,
                notes=request.POST.get("notes", ""),
            )
            for plan_exercise in plan.exercises.all():
                ExerciseLog.objects.create(
                    workout=workout,
                    exercise_name=plan_exercise.exercise_name,
                    sets=request.POST.get(f"sets_{plan_exercise.id}") or plan_exercise.sets,
                    reps=request.POST.get(f"reps_{plan_exercise.id}") or plan_exercise.reps,
                    weight_kg=request.POST.get(f"weight_{plan_exercise.id}") or None,
                )
            return redirect("workouts_home")

    workouts = Workout.objects.filter(user=request.user).prefetch_related("exercises", "plan")[:12]
    plans = WorkoutPlan.objects.filter(user=request.user).prefetch_related("exercises")
    selected_plan = None
    selected_plan_id = request.GET.get("plan")
    if selected_plan_id:
        selected_plan = get_object_or_404(plans, id=selected_plan_id)
    all_workouts = list(
        Workout.objects.filter(user=request.user)
        .prefetch_related("exercises")
        .order_by("date")[:30]
    )
    chart_source = (
        Workout.objects.filter(user=request.user)
        .values("date")
        .annotate(total_minutes=Sum("duration_minutes"))
        .order_by("date")[:20]
    )
    chart_data = {
        "labels": [item["date"].strftime("%d/%m") for item in chart_source],
        "values": [item["total_minutes"] for item in chart_source],
    }
    volume_data = {
        "labels": [workout.date.strftime("%d/%m") for workout in all_workouts],
        "values": [workout.total_volume_kg for workout in all_workouts],
    }
    exercise_map = defaultdict(list)
    for workout in all_workouts:
        for exercise in workout.exercises.all():
            exercise_map[exercise.exercise_name].append(
                {
                    "date": workout.date.strftime("%d/%m"),
                    "weight": float(exercise.weight_kg) if exercise.weight_kg else 0,
                    "volume": exercise.volume_kg,
                }
            )
    exercise_progress = []
    for name, entries in exercise_map.items():
        exercise_progress.append(
            {
                "name": name,
                "labels": [entry["date"] for entry in entries],
                "weights": [entry["weight"] for entry in entries],
                "volumes": [entry["volume"] for entry in entries],
                "max_weight": max([entry["weight"] for entry in entries] or [0]),
                "max_volume": max([entry["volume"] for entry in entries] or [0]),
            }
        )
    exercise_progress = sorted(exercise_progress, key=lambda item: item["max_volume"], reverse=True)[:8]
    context = {
        "workouts": workouts,
        "plans": plans,
        "workout_form": WorkoutForm(user=request.user),
        "plan_form": WorkoutPlanForm(),
        "exercise_form": ExerciseBulkForm(),
        "selected_plan": selected_plan,
        "today": timezone.localdate(),
        "chart_data": chart_data,
        "volume_data": volume_data,
        "exercise_progress": exercise_progress,
    }
    return render(request, "workouts/home.html", context)


@login_required
def start_plan_workout(request, plan_id):
    plan = get_object_or_404(
        WorkoutPlan.objects.prefetch_related("exercises"),
        id=plan_id,
        user=request.user,
    )

    if request.method == "POST":
        workout = Workout.objects.create(
            user=request.user,
            plan=plan,
            date=request.POST.get("date"),
            workout_type="gym",
            duration_minutes=request.POST.get("duration_minutes") or 0,
            notes=request.POST.get("notes", ""),
        )
        for exercise in plan.exercises.all():
            ExerciseLog.objects.create(
                workout=workout,
                exercise_name=exercise.exercise_name,
                sets=request.POST.get(f"sets_{exercise.id}") or exercise.sets,
                reps=request.POST.get(f"reps_{exercise.id}") or exercise.reps,
                weight_kg=request.POST.get(f"weight_{exercise.id}") or exercise.weight_kg,
            )
        return redirect("workouts_home")

    return render(request, "workouts/start_plan.html", {"plan": plan})


@login_required
def delete_plan(request, plan_id):
    plan = get_object_or_404(WorkoutPlan, id=plan_id, user=request.user)
    if request.method == "POST":
        plan.delete()
    return redirect("workouts_home")
