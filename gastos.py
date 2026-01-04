import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("data/gastos.json")

def cargarGastos():
    if not DATA_FILE.exists():
        return[]
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def guardarGastos(gastos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=2, ensure_ascii=False)

def registrarGasto(fecha, concepto, monto, forma_pago):
    gastos = cargarGastos()

    gasto ={
        "fecha": fecha,
        "concepto": concepto,
        "monto": float(monto),
        "forma_pago": forma_pago.lower()
    }

    gastos.append(gasto)
    guardarGastos(gastos)

    return gasto

def totalMesActual():
    gastos = cargarGastos()
    ahora = datetime.now()

    total = 0.0
    for g in gastos:
        fecha_gasto = datetime.fromisoformat(g["fecha"])
        if fecha_gasto.year == ahora.year and fecha_gasto.month == ahora.month:
            total+= g["monto"]

    return total