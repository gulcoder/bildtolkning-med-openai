import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_API_KEY"))

def encode_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

image_path = "övning3/example.webp"  # Byt ut med rätt sökväg till din UI-bild
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Ser du något fel eller inkonsekvens i användargränssnittet? Beskriv visuella buggar, felplacerade element, inkonsekventa färger, felmarginaler eller dålig kontrast."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                },
            ],
        }
    ],
    max_tokens=500,
)

print(response.choices[0].message.content)
