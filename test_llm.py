from llm import interpretarMensaje

while True:
    texto = input("Mensaje: ")
    if texto == "salir":
        break

    respuesta = interpretarMensaje(texto)
    print("Respuesta desde el LLM:")
    print(respuesta)