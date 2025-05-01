import json

# definimos el árbol binario con partidos de ida y vuelta
semifinal = {
    "fase": "Semifinal",
    "izquierdo": {
        "equipos": ["Barcelona", "Chelsea"],
        "ida": {
            "local": "Barcelona",
            "visitante": "Chelsea",
            "resultado": "1-1",
            "tarjetas": {
                "rojas": 1,
                "amarillas": 5
            }
        },
        "vuelta": {
            "local": "Chelsea",
            "visitante": "Barcelona",
            "resultado": "0-2",
            "tarjetas": {
                "rojas": 0,
                "amarillas": 2
            }
        }
    },
    "derecho": {
        "equipos": ["Manchester United", "Arsenal"],
        "ida": {
            "local": "Manchester United",
            "visitante": "Arsenal",
            "resultado": "3-1",
            "tarjetas": {
                "rojas": 1,
                "amarillas": 4
            }
        },
        "vuelta": {
            "local": "Arsenal",
            "visitante": "Manchester United",
            "resultado": "2-2",
            "tarjetas": {
                "rojas": 0,
                "amarillas": 3
            }
        }
    }
}

def parse_resultado(resultado):
    goles = resultado.split("-")
    return int(goles[0]), int(goles[1])

print("¿Qué partido quieres ver?")
print("1. Barcelona vs Chelsea")
print("2. Manchester United vs Arsenal")

opcion = input("Ingresa 1 o 2: ")

if opcion == "1":
    partido = semifinal["izquierdo"]
elif opcion == "2":
    partido = semifinal["derecho"]
else:
    print("Opción inválida.")
    exit()

# Mostrar resultados ida y vuelta
ida = partido["ida"]
vuelta = partido["vuelta"]

print("\nResultado del partido de ida:")
print(f"{ida['local']} {ida['resultado']} {ida['visitante']}")
print("Tarjetas:")
print(f"  Amarillas: {ida['tarjetas']['amarillas']}")
print(f"  Rojas: {ida['tarjetas']['rojas']}")

print("\nResultado del partido de vuelta:")
print(f"{vuelta['local']} {vuelta['resultado']} {vuelta['visitante']}")
print("Tarjetas:")
print(f"  Amarillas: {vuelta['tarjetas']['amarillas']}")
print(f"  Rojas: {vuelta['tarjetas']['rojas']}")

# Calcular resultado global
goles_ida_local, goles_ida_visitante = parse_resultado(ida["resultado"])
goles_vuelta_local, goles_vuelta_visitante = parse_resultado(vuelta["resultado"])

# Determinar goles de cada equipo en total
equipo1 = partido["equipos"][0]  # visitante en la vuelta
equipo2 = partido["equipos"][1]  # local en la vuelta

# Total de goles por equipo
total_equipo1 = goles_ida_local + goles_vuelta_visitante
total_equipo2 = goles_ida_visitante + goles_vuelta_local

print("\nResultado global:")
print(f"{equipo1}: {total_equipo1} goles")
print(f"{equipo2}: {total_equipo2} goles")

if total_equipo1 > total_equipo2:
    print(f"\n¡{equipo1} pasa a la siguiente ronda!")
elif total_equipo2 > total_equipo1:
    print(f"\n¡{equipo2} pasa a la siguiente ronda!")
else:
    print("\nEmpate global. Se requiere desempate (penales o goles de visitante, no implementado).")
