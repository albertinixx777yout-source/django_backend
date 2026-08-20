from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
import requests
from django.conf import settings

def index(request):
    try:
        # Intentamos consumir tu API local de Pagos
        response = requests.get('http://127.0.0.1:8000/pagos', timeout=3)
        pagos = response.json()
    except Exception:
        # Datos mock en caso de que tu FastAPI este apagado
        pagos = [
            {"id": 1, "cliente": "Juan Perez", "monto": 100, "fecha": "2026-08-18"},
            {"id": 2, "cliente": "Maria Lopez", "monto": 350, "fecha": "2026-08-19"},
            {"id": 3, "cliente": "Carlos Ruiz", "monto": 40,  "fecha": "2026-08-20"},
            {"id": 4, "cliente": "Ana Gomez",   "monto": 150, "fecha": "2026-08-20"},
            {"id": 5, "cliente": "Luis Silva",  "monto": 200, "fecha": "2026-08-20"},
        ]

    ingreso_total = sum(p.get("monto", 0) for p in pagos)
    pagos_hoy = len(pagos)
    ticket_promedio = round(ingreso_total / pagos_hoy, 2) if pagos_hoy > 0 else 0

    data = {
        "title": "Dashboard - Pagos y Facturación",
        "ingreso_total": ingreso_total,
        "pagos_hoy": pagos_hoy,
        "ticket_promedio": ticket_promedio,
        "pagos": pagos,
    }
    return render(request, "dashboard/index.html", data)