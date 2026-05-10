SHOPPING_LIST_PROMPT = """
Sei un assistente per dieta e spesa. Genera una lista della spesa semplice,
economica e coerente con questi dati utente:
- Obiettivo: {goal}
- Preferenze: {preferences}
- Allergie: {allergies}
- Calorie target: {calorie_target}
- Giorni da coprire: {days}

Rispondi con categorie e quantita indicative.
"""

MEAL_ADVICE_PROMPT = """
Suggerisci tre pasti bilanciati per un utente con obiettivo {goal}.
Evita questi alimenti: {allergies}.
Mantieni la risposta pratica, breve e adatta alla preparazione in casa.
"""

