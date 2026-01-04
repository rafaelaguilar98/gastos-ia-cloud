from openai import OpenAI
from datetime import date

client = OpenAI()


SYSTEM_PROMPT = f"""
Eres un asistente que interpreta gastos personales.

Devuelve SOLO JSON válido.

Reglas:
- accion: "registrar_gasto" o "consultar_total"
- fecha: ISO (YYYY-MM-DD)
- Si no se especifica fecha → usa hoy ({date.today().isoformat()})
- forma_pago por defecto: "efectivo"
- concepto: específico (uber, café, tacos)
- monto: número

Ejemplos:

Usuario: Compré café por 20
Respuesta:
{{"accion":"registrar_gasto","fecha":"{date.today().isoformat()}","concepto":"café","monto":20,"forma_pago":"efectivo"}}

Usuario: ¿Cuánto gasté este mes?
Respuesta:
{{"accion":"consultar_total"}}
"""


def interpretarMensaje(mensaje: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": mensaje}
        ],
        temperature=0 #Evitar alucinaciones
    )

    return response.choices[0].message.content
