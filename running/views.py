from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RunForm
from .models import Run
from .services import import_activity_file


@login_required
def running_home(request):
    if request.method == "POST":
        form = RunForm(request.POST, request.FILES)
        if form.is_valid():
            run = form.save(commit=False)
            run.user = request.user
            run.save()
            import_activity_file(run)
            return redirect("running_home")
    else:
        form = RunForm()

    runs = Run.objects.filter(user=request.user).prefetch_related("track_points")[:12]
    chart_runs = list(Run.objects.filter(user=request.user).order_by("date")[:20])
    chart_data = {
        "labels": [run.date.strftime("%d/%m") for run in chart_runs],
        "distance": [float(run.distance_km) for run in chart_runs],
        "duration": [run.duration_minutes for run in chart_runs],
    }
    total_distance = sum(float(run.distance_km) for run in runs)
    total_minutes = sum(run.duration_minutes for run in runs)
    latest_track = next((run for run in runs if run.track_points.exists()), None)
    track_points = list(latest_track.track_points.all()) if latest_track else []
    track_data = {
        "labels": [float(point.distance_km) for point in track_points],
        "elevation": [float(point.elevation_m) if point.elevation_m is not None else None for point in track_points],
        "time": [point.seconds_from_start for point in track_points],
    }
    return render(
        request,
        "running/home.html",
        {
            "runs": runs,
            "form": form,
            "chart_data": chart_data,
            "track_data": track_data,
            "latest_track": latest_track,
            "total_distance": round(total_distance, 2),
            "total_minutes": total_minutes,
        },
    )
