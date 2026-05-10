from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .prompts import SHOPPING_LIST_PROMPT
from .services import AiAssistantError, ask_ai


@login_required
def ai_home(request):
    result = None
    error = None

    if request.method == "POST":
        prompt = SHOPPING_LIST_PROMPT.format(
            goal=request.POST.get("goal", ""),
            preferences=request.POST.get("preferences", ""),
            allergies=request.POST.get("allergies", ""),
            calorie_target=request.POST.get("calorie_target", ""),
            days=request.POST.get("days", "7"),
        )
        try:
            result = ask_ai(prompt)
        except (AiAssistantError, Exception) as exc:
            error = str(exc)

    return render(request, "ai_assistant/home.html", {"result": result, "error": error})

