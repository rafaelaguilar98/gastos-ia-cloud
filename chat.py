def chat():
    print("Chat para control de gastos (escribe 'sali' para terminar)\n")

    while True:
        mensaje = input("Mensaje: ").strip().lower()

        if mensaje == "salir":
            print("Adiós")
            break

        if "cuánto" in mensaje and "gast" in mensaje:
            print("Bot: (aquí se consultaran los gastos)")
        elif "compr" in mensaje or "gast" in mensaje or "pag" in mensaje:
            print("bot: (Aquí se registrarán los gastos)")
        else:
            print("Bot: No entendí, intenta otra frase")

if __name__ == "__main__":
    chat()