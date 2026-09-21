#!/usr/bin/env python3
"""Descarga la disponibilidad de GO CARS y la guarda como archivo estático.

Por qué existe: el catálogo pedía la disponibilidad directamente a Google (Apps Script).
Si la red del visitante tiene IPv6 roto (caso real de la red del negocio) o algún
bloqueador corta el script, la consulta se cuelga y el cliente no ve las horas.

Este script lo ejecuta GitHub cada 20 minutos y publica el resultado en
`datos/disponibilidad.json`, servido por el PROPIO dominio (solo IPv4, sin terceros).
El catálogo lo usa como respaldo cuando la consulta en vivo falla.
"""

import datetime
import json
import os
import urllib.request

API = ("https://script.google.com/macros/s/"
       "AKfycbzJ7i6Rq-__fSYs51kKacG6XB20YEzaTbsUVZ5fWOkMxn35Th-sdsLYRqewOjLTSlWT7A/exec")
DIAS = 15           # hoy + 14 días
DURACION = 45       # duración por defecto (el backend recalcula con la real)
SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "disponibilidad.json")


def pedir(fecha):
    url = "%s?action=slots&fecha=%s&dur=%d&ruta=" % (API, fecha, DURACION)
    req = urllib.request.Request(url, headers={"User-Agent": "go-cars-disponibilidad"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    hoy = datetime.date.today()
    salida = {
        "generado": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dias": {},
    }
    errores = []
    for i in range(DIAS):
        fecha = (hoy + datetime.timedelta(days=i)).isoformat()
        try:
            d = pedir(fecha)
            if d.get("ok"):
                salida["dias"][fecha] = {
                    "capacidad": d.get("capacidad"),
                    "rest": d.get("rest"),
                    "slots": [
                        {"hora": s.get("hora"), "estado": s.get("estado", ""),
                         "libres": s.get("libres"), "ruta": s.get("ruta", "")}
                        for s in (d.get("slots") or [])
                    ],
                }
        except Exception as e:                                    # noqa: BLE001
            errores.append("%s: %s" % (fecha, e))

    if not salida["dias"]:
        raise SystemExit("No se pudo descargar ningún día. Errores: " + "; ".join(errores))

    anterior = None
    if os.path.exists(SALIDA):
        try:
            anterior = json.load(open(SALIDA, encoding="utf-8"))
        except Exception:                                          # noqa: BLE001
            anterior = None

    # Si nada cambió en las horas, solo se actualiza la marca de tiempo cada hora
    if anterior and anterior.get("dias") == salida["dias"]:
        try:
            misma_hora = anterior.get("generado", "")[:13] == salida["generado"][:13]
        except Exception:                                          # noqa: BLE001
            misma_hora = False
        if misma_hora:
            print("Sin cambios en esta media hora; no se reescribe.")
            return

    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, separators=(",", ":"))
    print("días guardados: %d | errores: %d" % (len(salida["dias"]), len(errores)))
    for e in errores[:5]:
        print("  -", e)


if __name__ == "__main__":
    main()
