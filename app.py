from gastos import registrarGasto, totalMesActual
from datetime import date


def main():
    registrarGasto(
        fecha=date.today().isoformat(),
        concepto="café",
        monto=20,
        forma_pago="efectivo"
    )

    total = totalMesActual()
    print(f"Total gastado este mes: ${total}")


if __name__ == "__main__":
    main()
