from openai import OpenAI
from datetime import date
from pathlib import Path

client = OpenAI()

PROMPT_PATH = Path("prompts/gastos_system.txt")
def cargar_system_prompt() -> str:
    return PROMPT_PATH.read_text(encoding="utf-8")

def interpretarMensaje(mensaje: str) -> str: # Definir el tipo de dato que recibe y el que retorna
    SYSTEM_PROMPT = cargar_system_prompt()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": mensaje}
        ],
        temperature=0 #Evitar alucinaciones
    )

    return response.choices[0].message.content
