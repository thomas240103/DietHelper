import requests
from django.conf import settings


class AiAssistantError(Exception):
    pass


def ask_ai(prompt):
    provider = settings.AI_PROVIDER.lower()
    if provider == "gemini":
        return ask_gemini(prompt)
    if provider == "openai":
        return ask_openai(prompt)
    raise AiAssistantError(f"Provider AI non supportato: {settings.AI_PROVIDER}")


def ask_gemini(prompt):
    if not settings.GEMINI_API_KEY:
        raise AiAssistantError("GEMINI_API_KEY non configurata.")

    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
    )
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError) as exc:
        raise AiAssistantError("Risposta Gemini non valida.") from exc


def ask_openai(prompt):
    if not settings.OPENAI_API_KEY:
        raise AiAssistantError("OPENAI_API_KEY non configurata.")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "Sei un assistente pratico per dieta e fitness."},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise AiAssistantError("Risposta OpenAI non valida.") from exc

