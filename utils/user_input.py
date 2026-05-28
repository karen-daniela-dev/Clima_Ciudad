# utils/user_input.py

def get_city_input() -> str:
    city = input("Ingresa el nombre de la ciudad: ").strip()

    if not city:
        raise ValueError("La ciudad no puede estar vacía")

    if any(char.isdigit() for char in city):
        raise ValueError("La ciudad no debe contener números")

    return city