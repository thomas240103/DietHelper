from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import BodyProgressForm
from .models import BodyProgress


@login_required
def progress_home(request):
    if request.method == "POST":
        form = BodyProgressForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("progress_home")
    else:
        form = BodyProgressForm()

    entries = BodyProgress.objects.filter(user=request.user)[:12]
    chart_entries = list(BodyProgress.objects.filter(user=request.user).order_by("date")[:20])
    chart_data = {
        "labels": [entry.date.strftime("%d/%m") for entry in chart_entries],
        "weight": [float(entry.weight_kg) if entry.weight_kg is not None else None for entry in chart_entries],
        "waist": [float(entry.waist_cm) if entry.waist_cm is not None else None for entry in chart_entries],
    }
    latest = entries[0] if entries else None
    return render(
        request,
        "progress/home.html",
        {"entries": entries, "form": form, "chart_data": chart_data, "latest": latest},
    )
