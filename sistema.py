"""Conversor de unidades: temperatura, distancia y moneda."""

# Tasa fija definida en el programa (1 USD = 18.00 MXN)
TASA_MXN_POR_USD = 18.00


# ---------- Temperatura ----------
def celsius_a_fahrenheit(celsius):
    return round(celsius * 9 / 5 + 32, 2)


def fahrenheit_a_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5 / 9, 2)


# ---------- Distancia ----------
def km_a_millas(km):
    return round(km * 0.621371, 2)


def millas_a_km(millas):
    return round(millas / 0.621371, 2)


# ---------- Moneda ----------
def mxn_a_usd(pesos):
    return round(pesos / TASA_MXN_POR_USD, 2)


def usd_a_mxn(dolares):
    return round(dolares * TASA_MXN_POR_USD, 2)


# ---------- Interfaz de consola ----------
def pedir_valor():
    """Solicita un valor numérico. Devuelve None si la entrada no es válida."""
    try:
        return float(input("Ingresa el valor a convertir: "))
    except ValueError:
        print("Error: debes ingresar un valor numérico.")
        return None


def mostrar_menu():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Kilómetros -> Millas")
    print("4. Millas -> Kilómetros")
    print("5. Pesos MXN -> Dólares USD")
    print("6. Dólares USD -> Pesos MXN")
    print("0. Salir")


def main():
    conversiones = {
        "1": (celsius_a_fahrenheit, "°F"),
        "2": (fahrenheit_a_celsius, "°C"),
        "3": (km_a_millas, "millas"),
        "4": (millas_a_km, "km"),
        "5": (mxn_a_usd, "USD"),
        "6": (usd_a_mxn, "MXN"),
    }

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Hasta luego.")
            break

        if opcion not in conversiones:
            print("Opción no válida.")
            continue

        valor = pedir_valor()
        if valor is None:
            continue

        funcion, unidad = conversiones[opcion]
        print(f"Resultado: {funcion(valor):.2f} {unidad}")


if __name__ == "__main__":
    main()