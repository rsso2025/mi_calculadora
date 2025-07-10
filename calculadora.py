def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a: float, b: float) -> float:
    return a ** b

# La función elevar_al_cubo será añadida en otra rama
if __name__ == "__main__":
    print("Suma:", sumar(2, 3))
    print("Resta:", restar(5, 2))
    print("Multiplicación:", multiplicar(3, 4))
    print("División:", dividir(10, 2))
    print("Potencia:", potencia(2, 3))

def elevar_al_cubo(a: float) -> float:
    return a ** 3

# Prueba
print("Cubo:", elevar_al_cubo(3))  # Debería mostrar 27

