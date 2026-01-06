import json
from llm import interpretarMensaje
from gastos import registrarGasto, totalMesActual
from datetime import date

def ejecutarAccion(data: dict) -> str:
    accion = data.get("accion")

    if accion == "registrar_gasto":
        gasto = registrarGasto(
            fecha=data["fecha"],
            concepto=data["concepto"],
            monto= data["monto"],
            forma_pago=data["forma_pago"]
        )
        return(f"Gasto registrado: {gasto['concepto']}-${gasto['monto']}")
    elif accion =="consultar_total":
        total = totalMesActual()
        return f"Tu total gastado este mes: ${total}"
def chat():
    print("Chat para registro de gastos (escribe 'salir' para terminar)\n")
    while True:
        mensaje = input("Ingresa tu gasto o consulta: ").strip()

        if mensaje.lower()== "salir":
            print("Hasta luego")
            break

        try:
            respuesta_llm = interpretarMensaje(mensaje=mensaje)
            data = json.loads(respuesta_llm)

            respuesta = ejecutarAccion(data=data)
            print("Respuesta del bot:", respuesta)

        except json.JSONDecodeError:
            print("Error, LLM no devolvió JSON válido")
        except KeyError as e:
            print(f"Falta un campo requerido: {e}")
        except Exception as e:
            print("Ocurrió un error:",e)

if __name__ == "__main__":
    chat()
