# DietHelp

DietHelp e una web app Django pensata per gestire dieta, lista spesa, calorie, allenamento e corsa da un ambiente locale sul PC, con possibile deploy successivo.

L'obiettivo e avere un assistente personale per organizzare alimentazione e attivita fisica, monitorare i progressi nel tempo e usare API AI come Gemini o ChatGPT/OpenAI per suggerimenti su dieta, pasti e lista della spesa.

## Stato Del Progetto

Fase attuale: scaffold Django iniziale creato.

Questo README e il documento di riferimento principale del progetto. Va aggiornato ogni volta che vengono aggiunte funzionalita, app Django, modelli, API, comandi o decisioni tecniche importanti.

Gia presenti nel progetto:

- Configurazione Django base.
- App `accounts`, `nutrition`, `shopping`, `documents`, `workouts`, `running`, `progress`, `ai_assistant`.
- Modelli iniziali per profilo, alimenti, pasti, lista spesa, PDF, allenamenti, corsa e progressi.
- Admin Django per i modelli principali.
- Template base, homepage, dashboard e pagine minime dei moduli.
- Upload PDF locale tramite app `documents`.
- Servizio AI iniziale con scelta provider da `.env`.

## Obiettivi

- Gestire profilo utente, dati fisici e obiettivi.
- Registrare pasti, alimenti e calorie giornaliere.
- Creare e aggiornare una lista della spesa.
- Caricare PDF come diete, piani alimentari o schede allenamento.
- Tracciare allenamenti, corsa e progressi fisici.
- Generare consigli tramite API AI.
- Funzionare in locale sul PC.
- Mantenere una struttura Django pulita e facile da estendere.

## Funzionalita Previste

### Profilo Utente

- Nome o nickname.
- Eta, altezza, peso iniziale e peso attuale.
- Obiettivo: dimagrimento, mantenimento, massa muscolare o performance.
- Preferenze alimentari.
- Allergie o alimenti da evitare.
- Livello di attivita fisica.

### Dieta E Calorie

- Diario alimentare giornaliero.
- Inserimento pasti: colazione, pranzo, cena, snack.
- Calcolo calorie totali.
- Possibile calcolo macro: proteine, carboidrati, grassi.
- Storico dei giorni precedenti.
- Confronto tra calorie assunte e obiettivo giornaliero.

### Lista Spesa

- Creazione manuale di prodotti.
- Generazione automatica da pasti o piano dieta.
- Stato prodotto: da comprare / comprato.
- Categorie: frutta, verdura, proteine, cereali, latticini, altro.
- Suggerimenti AI per completare la lista in base agli obiettivi.

### Documenti PDF

- Caricamento PDF personali.
- Tipi documento: dieta, piano alimentare, scheda allenamento, piano corsa, altro.
- Titolo e descrizione del documento.
- Archiviazione locale dei file.
- Visualizzazione elenco documenti caricati.
- Download o apertura del PDF.
- Collegamento opzionale del PDF a dieta, allenamento o progressi.
- Estrazione testo opzionale in futuro.
- Uso del contenuto PDF come contesto per consigli AI, se autorizzato dall'utente.

Esempi di PDF utili:

- Dieta fornita da nutrizionista.
- Piano alimentare settimanale.
- Scheda palestra.
- Programma corsa.
- Lista alimenti consigliati o vietati.

### Allenamento

- Registro allenamenti.
- Tipo allenamento: palestra, corpo libero, cardio, mobilita.
- Durata.
- Esercizi svolti.
- Serie, ripetizioni e carichi.
- Note personali.
- Schede palestra salvabili e riutilizzabili.
- Avvio sessione da scheda con modifica dei pesi effettivi.
- Calcolo volume totale: peso x serie x ripetizioni.
- Andamento volume complessivo nel tempo.
- Andamento peso e volume per singolo esercizio.

### Corsa

- Registro uscite di corsa.
- Distanza.
- Durata.
- Passo medio.
- Calorie stimate.
- Percorso o note.
- Progressi settimanali e mensili.
- Upload file attivita: GPX, TCX, FIT, CSV.
- Parsing GPX con punti tracciato, distanza progressiva, tempo e quota.
- Grafico del profilo importato dal file GPX.

### Progressi

- Storico peso.
- Misure corporee opzionali.
- Grafici per peso, calorie, allenamenti e corsa.
- Riepilogo settimanale.
- Riepilogo mensile.

### Consigli AI

Possibili integrazioni:

- Gemini API.
- OpenAI / ChatGPT API.

Usi previsti:

- Suggerire pasti in base agli obiettivi.
- Proporre una lista della spesa settimanale.
- Dare idee per ricette semplici.
- Aiutare a correggere una giornata alimentare sbilanciata.
- Suggerire allenamenti compatibili con livello e obiettivo.
- Riassumere i progressi.

Nota: i consigli AI non devono sostituire un medico, nutrizionista o personal trainer.

## Stack Tecnico

- Backend: Django.
- Database locale iniziale: SQLite.
- Frontend iniziale: Django templates.
- Stile: CSS personalizzato o framework leggero da decidere.
- Grafici: Chart.js o libreria simile.
- API AI: Gemini e/o OpenAI.
- Deploy locale: server Django su `localhost`.

## Struttura Prevista

```text
DietHelp/
  manage.py
  README.md
  .env
  .gitignore
  requirements.txt
  diethelp/
    settings.py
    urls.py
    asgi.py
    wsgi.py
  accounts/
    models.py
    views.py
    urls.py
    forms.py
    templates/
  nutrition/
    models.py
    views.py
    urls.py
    forms.py
    templates/
  shopping/
    models.py
    views.py
    urls.py
    forms.py
    templates/
  documents/
    models.py
    views.py
    urls.py
    forms.py
    templates/
  workouts/
    models.py
    views.py
    urls.py
    forms.py
    templates/
  running/
    models.py
    views.py
    urls.py
    forms.py
    templates/
  progress/
    models.py
    views.py
    urls.py
    templates/
  ai_assistant/
    services.py
    prompts.py
    views.py
    urls.py
```

## App Django Previste

### `accounts`

Gestisce utente, profilo, obiettivi e preferenze.

### `nutrition`

Gestisce alimenti, pasti, calorie e diario alimentare.

### `shopping`

Gestisce lista della spesa e prodotti.

### `documents`

Gestisce caricamento, archiviazione e consultazione dei PDF personali.

### `workouts`

Gestisce allenamenti, esercizi e sessioni.

### `running`

Gestisce uscite di corsa e statistiche.

### `progress`

Gestisce dashboard, grafici e riepiloghi.

### `ai_assistant`

Centralizza integrazione con Gemini/OpenAI, prompt e logica per consigli.

## Modelli Dati Iniziali

Questa sezione va aggiornata quando i model Django saranno creati.

### UserProfile

Campi previsti:

- user
- birth_date
- height_cm
- starting_weight_kg
- current_weight_kg
- goal
- activity_level
- dietary_preferences
- allergies

### Food

Campi previsti:

- name
- calories_per_100g
- protein_per_100g
- carbs_per_100g
- fat_per_100g

### Meal

Campi previsti:

- user
- date
- meal_type
- notes

### MealItem

Campi previsti:

- meal
- food
- quantity_g
- calories

### ShoppingItem

Campi previsti:

- user
- name
- category
- quantity
- is_bought
- created_at

### UploadedDocument

Campi previsti:

- user
- title
- document_type
- description
- file
- extracted_text
- uploaded_at
- updated_at

### Workout

Campi previsti:

- user
- date
- workout_type
- duration_minutes
- notes

### ExerciseLog

Campi previsti:

- workout
- exercise_name
- sets
- reps
- weight_kg

### Run

Campi previsti:

- user
- date
- distance_km
- duration_minutes
- average_pace
- estimated_calories
- notes

### BodyProgress

Campi previsti:

- user
- date
- weight_kg
- waist_cm
- chest_cm
- hips_cm
- notes

## Setup Locale

### 1. Creare Ambiente Virtuale

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Installare Dipendenze

Quando esistera `requirements.txt`:

```powershell
pip install -r requirements.txt
```

Dipendenze iniziali previste:

```text
Django
python-dotenv
requests
PyPDF2
```

### 3. Creare Progetto Django

Il progetto Django e gia stato creato manualmente nella cartella.

Questo comando non serve piu, a meno di voler ricreare il progetto da zero:

```powershell
django-admin startproject diethelp .
```

### 4. Migrazioni

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 5. Creare Superuser

```powershell
python manage.py createsuperuser
```

### 6. Avviare Server Locale

```powershell
python manage.py runserver
```

URL locale:

```text
http://127.0.0.1:8000/
```

Nota: se il comando `python` non funziona da terminale, installare Python da https://www.python.org/downloads/ e assicurarsi che sia aggiunto al PATH di Windows.

Se `python` punta a `C:\Users\...\AppData\Local\Microsoft\WindowsApps\python.exe`, significa che Windows sta usando l'alias del Microsoft Store invece di una vera installazione. In quel caso:

- installare Python da https://www.python.org/downloads/;
- selezionare `Add python.exe to PATH` durante l'installazione;
- disattivare gli alias Python in `Impostazioni > App > Impostazioni app avanzate > Alias esecuzione app`.

## Deploy Locale Veloce Su Un PC Windows

Se il PC non ha Django installato, non e un problema: Django viene installato dentro un ambiente virtuale locale `.venv`.

Requisito minimo:

- Python installato sul PC.
- Durante l'installazione di Python, abilitare `Add python.exe to PATH`.

### Primo Avvio Sul PC

Aprire PowerShell nella cartella del progetto ed eseguire:

```powershell
.\scripts\setup_windows.ps1
```

Lo script:

- crea `.venv`;
- installa le dipendenze da `requirements.txt`;
- crea `.env` se manca;
- prepara il database SQLite;
- esegue le migrazioni.

### Avvio Giornaliero

Dopo il setup iniziale:

```powershell
.\scripts\run_windows.ps1
```

Poi aprire:

```text
http://127.0.0.1:8000/
```

### Accesso Da Altri Dispositivi Nella Stessa Rete

Per aprire DietHelp da telefono, tablet o altro PC collegato alla stessa rete Wi-Fi:

```powershell
.\scripts\run_lan_windows.ps1
```

Lo script mostra un indirizzo simile a:

```text
http://192.168.1.50:8000/
```

Aprire quell'indirizzo dal browser dell'altro dispositivo.

Se Django mostra errore `DisallowedHost`, aprire `.env` e aggiungere l'IP del PC in `ALLOWED_HOSTS`.

Esempio:

```env
ALLOWED_HOSTS=127.0.0.1,localhost,192.168.1.50
```

Poi fermare il server con `CTRL+C` e rilanciare:

```powershell
.\scripts\run_lan_windows.ps1
```

Se il sito non si apre:

- controllare che i dispositivi siano sulla stessa rete;
- consentire Python/Django nel firewall di Windows;
- verificare che l'indirizzo IP mostrato dallo script sia corretto.

### Se PowerShell Blocca Gli Script

Eseguire una volta:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Poi rilanciare:

```powershell
.\scripts\setup_windows.ps1
```

### PC Senza Python

Se il PC non ha nemmeno Python, ci sono tre opzioni:

- installare Python e usare gli script sopra;
- usare Docker, se presente sul PC;
- creare in futuro una versione eseguibile/portable, piu comoda ma meno naturale per un'app Django.

Per ora la strada consigliata e Python + `.venv`, perche e semplice, pulita e facile da aggiornare.

## Variabili Ambiente

Creare un file `.env` nella root del progetto.

Esempio:

```env
DEBUG=True
SECRET_KEY=change-me
ALLOWED_HOSTS=127.0.0.1,localhost

GEMINI_API_KEY=
OPENAI_API_KEY=
AI_PROVIDER=gemini
```

Regole:

- Non caricare mai `.env` su Git.
- Tenere le chiavi API fuori dal codice.
- Usare `AI_PROVIDER` per scegliere il provider attivo.

## Integrazione AI

La logica AI andra tenuta dentro `ai_assistant/` per evitare codice duplicato nelle altre app.

Struttura prevista:

```text
ai_assistant/
  services.py
  prompts.py
  views.py
  urls.py
```

### `services.py`

Responsabilita:

- Leggere provider attivo da settings.
- Chiamare Gemini o OpenAI.
- Gestire errori API.
- Restituire risposte pulite alle view.

### `prompts.py`

Responsabilita:

- Prompt per consigli dieta.
- Prompt per lista spesa.
- Prompt per riepilogo progressi.
- Prompt per allenamenti.

### Esempi Di Prompt

Consiglio lista spesa:

```text
Sei un assistente per dieta e spesa. Genera una lista della spesa semplice,
economica e coerente con questi dati utente:
- Obiettivo: {goal}
- Preferenze: {preferences}
- Allergie: {allergies}
- Calorie target: {calorie_target}
- Giorni da coprire: {days}

Rispondi con categorie e quantita indicative.
```

Consiglio pasti:

```text
Suggerisci tre pasti bilanciati per un utente con obiettivo {goal}.
Evita questi alimenti: {allergies}.
Mantieni la risposta pratica, breve e adatta alla preparazione in casa.
```

## Sicurezza E Privacy

- Non salvare chiavi API nel database.
- Non mostrare dati sensibili nei log.
- Proteggere le view con login quando gestiscono dati personali.
- Aggiungere disclaimer medico nelle pagine di consigli AI.
- Evitare diagnosi, prescrizioni o indicazioni mediche rigide.

## Roadmap

### Fase 1 - Base Django

- Creare progetto Django.
- Configurare `.env`.
- Creare `.gitignore`.
- Creare app principali.
- Configurare template base.
- Configurare autenticazione.

### Fase 2 - Profilo E Dashboard

- Modello profilo utente.
- Pagina dashboard.
- Form obiettivi e dati fisici.
- Navigazione principale.

### Fase 3 - Nutrizione

- Modelli alimenti, pasti e elementi pasto.
- CRUD alimenti.
- Diario giornaliero.
- Calcolo calorie.

### Fase 4 - Lista Spesa

- Modello lista spesa.
- CRUD prodotti.
- Stato comprato/non comprato.
- Generazione lista da pasti.

### Fase 5 - Documenti PDF

- Creare app `documents`.
- Modello per PDF caricati.
- Upload PDF da interfaccia web.
- Lista documenti caricati.
- Download o apertura documento.
- Estrazione testo opzionale dal PDF.
- Collegamento futuro con AI per leggere dieta o scheda caricata.

### Fase 6 - Allenamento E Corsa

- Registro allenamenti.
- Registro corsa.
- Calcolo passo medio.
- Storico sessioni.

### Fase 7 - Progressi

- Peso e misure.
- Grafici.
- Riepiloghi settimanali.
- Riepiloghi mensili.

### Fase 8 - AI

- Configurare provider Gemini/OpenAI.
- Creare servizio AI centralizzato.
- Generare lista spesa.
- Generare consigli pasti.
- Generare riepilogo progressi.
- Usare testo estratto dai PDF come contesto, solo se richiesto dall'utente.

### Fase 9 - Rifinitura

- Migliorare UI.
- Validazioni form.
- Test principali.
- Documentare comandi definitivi.

## Convenzioni Di Sviluppo

- Ogni app Django deve avere responsabilita chiara.
- I model devono stare nell'app piu vicina al dominio.
- La logica AI deve stare in `ai_assistant`, non nelle view delle altre app.
- Le view devono rimanere semplici.
- Usare form Django per input utente.
- Salvare i PDF caricati tramite `MEDIA_ROOT` e servirli in locale tramite `MEDIA_URL`.
- Validare estensione e dimensione dei file caricati.
- Aggiornare questo README a ogni nuova decisione tecnica.

## Comandi Utili

```powershell
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

## Decisioni Da Prendere

- Usare solo Gemini, solo OpenAI, o entrambi.
- Scegliere framework CSS o CSS custom.
- Decidere se usare class-based views o function-based views.
- Decidere se aggiungere Django REST Framework in futuro.
- Decidere se servira un database diverso da SQLite.

## Note

DietHelp deve restare semplice da usare in locale. La priorita iniziale e creare una base solida con Django, poi aggiungere moduli uno alla volta senza complicare troppo il progetto.
