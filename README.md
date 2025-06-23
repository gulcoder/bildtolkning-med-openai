# 🧠 Bildtolkning med OpenAI – Multimodala AI-övningar

Detta repository innehåller en samling övningar för att lära sig använda OpenAI:s GPT-4o-modell för bildanalys, textutvinning (OCR), UI-inspektion och emotionell analys. Fokus ligger på hur man med Python och OpenAI:s API kan tolka och bearbeta visuell information på ett intelligent sätt.

## 🎯 Syfte

Att stegvis utforska kraften i OpenAI:s multimodala modell (GPT-4o) genom praktiska övningar:
- Tolka innehållet i fotografier och dokument
- Extrahera text från bilder
- Identifiera visuella buggar i användargränssnitt
- Analysera känslor i porträttbilder
- Tolka skärmdumpar av kod

> 💡 **Observera:** Du ansvarar själv för att välja lämpliga bilder till varje övning. Använd exempelbilder från webben eller ta egna skärmdumpar för bästa effekt.

## 📦 Innehåll

### 🔹 Övning 1 – Bildbeskrivning
**Prompt:** *"Vad visar bilden? Beskriv det på ett objektivt sätt."*  
Analyserar foto och genererar en neutral sammanfattning.  
📂 Fil: `övning1/main.py`

---

### 🔹 Övning 2 – Kodsnapptolkning
**Prompt:** *"Förklara vad koden i bilden gör."*  
Analyserar en skärmdump med kod och ger begriplig förklaring.  
📂 Fil: `övning2/main.py`

---

### 🔹 Övning 3 – UI-testning
**Prompt:** *"Ser du något fel eller inkonsekvens i användargränssnittet?"*  
Identifierar visuella buggar eller designmissar i ett UI.  
📂 Fil: `övning3/main.py`

---

### 🔹 Övning 4 – OCR (Textutvinning)
**Prompt:** *"Extrahera all text från denna bild. Formatera som en punktlista."*  
Använder GPT-4 Vision för att extrahera text från bilder (t.ex. kvitton, etiketter).  
📂 Fil: `övning4/main.py`

---

### 🔹 Övning 5 – Emotionell ansiktsanalys
**Prompt:** *"Vilka känslor visar personen på bilden? Beskriv ansiktsuttryck och möjliga känslotillstånd."*  
Analys av uttryck i porträttbilder (obs: API-policyer kan påverka detta).  
📂 Fil: `övning5/main.py`

---



## ⚙️ Installation

1. Klona projektet:
```bash
git clone https://github.com/gulcoder/bildtolkning-med-openai.git
cd bildtolkning-med-openai
