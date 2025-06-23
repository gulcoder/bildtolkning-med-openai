# 📸 Bildtolkning med OpenAI

Detta projekt demonstrerar hur man använder OpenAI:s GPT-4o för att tolka bilder, inklusive textigenkänning (OCR), UI-testning, känsloanalys och objektiva bildbeskrivningar. Projektet syftar till att ge praktisk erfarenhet i att kombinera multimodal AI med Python.

## 🎯 Syfte

Målet är att utforska hur GPT-4 Vision kan förstå och analysera olika typer av bilder via API-anrop. Övningarna täcker:

1. **Övning1: Objektiv beskrivning av ett foto**
2. **Övning2: Förklaring av kod via skärmdump**
3. **Övning3: Upptäcka UI-fel och visuella inkonsekvenser**
4. **Övning4: Extrahera text från t.ex. kvitton eller etiketter (OCR)**
5. **Övning5: Identifiera känslor i porträttbilder**

> 💡 **Observera:** Du ansvarar själv för att välja lämpliga bilder till varje övning. Använd exempelbilder från webben eller ta egna skärmdumpar för bästa effekt.

## 📁 Struktur

- Eftersom övningarna följer ett liknande kodmönster, är alla exempel samlade i en enda Python-fil: `main.py`.
- Uppdatera **prompten** i `main.py` beroende på vad du vill att AI:n ska göra.
- Ingen kodförändring krävs utöver prompt och bildväg.


## 🧪 Övningar & exempelprompter

| Övning | Syfte | Prompt |
|--------|-------|--------|
| 1 | Objektiv bildbeskrivning | `Vad visar bilden? Beskriv det på ett objektivt sätt.` |
| 2 | Förstå kod i skärmdump | `Förklara vad koden i bilden gör.` |
| 3 | UI-felanalys | `Ser du något fel eller inkonsekvens i användargränssnittet?` |
| 4 | Textigenkänning (OCR) | `Extrahera all text från denna bild. Formatera som en punktlista.` |
| 5 | Ansiktsuttryck & känslor | `Vilka känslor visar personen på bilden?` |

## ✍️ Förslag på promptformuleringar

Nedan ser du vad du kan skriva som prompt i respektive övning:

### 🖼️ Övning 1 – Bildbeskrivning
> **Prompt:**  
> `Vad visar bilden? Beskriv det på ett objektivt sätt utan att anta något om bilden.`  
> **Tips:** Använd en bild från t.ex. vardagen, en plats, inomhusmiljö, etc.

---

### 🧑‍💻 Övning 2 – Kodanalys från bild
> **Prompt:**  
> `Förklara vad koden på bilden gör. Identifiera om möjligt vilket språk det är.`  
> **Tips:** Skärmdumpa kod i VS Code eller terminalen.

---

### 🧪 Övning 3 – UI-bugganalys
> **Prompt:**  
> `Ser du några designproblem eller inkonsekvenser i användargränssnittet?`  
> **Tips:** Skärmdumpa en webbsida, app, eller formulär.

---

### 🧾 Övning 4 – Textigenkänning (OCR)
> **Prompt:**  
> `Extrahera all text från denna bild. Formatera som en punktlista.`  
> **Tips:** Använd t.ex. ett kvitto, affisch, meny, bokomslag eller skylt.

---

### 😊 Övning 5 – Ansiktsuttryck och känslor
> **Prompt:**  
> `Vilka känslor visar personen på bilden? Beskriv ansiktsuttryck och möjliga känslotillstånd.`  
> **Tips:** Använd en porträttbild där ansiktsuttryck är tydliga.

## 🚀 Kom igång

1. Klona projektet:
   ```bash
   git clone https://github.com/gulcoder/bildtolkning-med-openai.git
   cd bildtolkning-med-openai



