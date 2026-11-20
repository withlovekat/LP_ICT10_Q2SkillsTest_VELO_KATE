from pyscript import display, document

non_metals = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "atomic_weight": 1.008},
    "C": {"name": "Carbon", "atomic_number": 6, "atomic_weight": 12.011},
    "N": {"name": "Nitrogen", "atomic_number": 7, "atomic_weight": 14.007},
    "O": {"name": "Oxygen", "atomic_number": 8, "atomic_weight": 15.999},
    "P": {"name": "Phosphorus", "atomic_number": 15, "atomic_weight": 30.974},
    "S": {"name": "Sulfur", "atomic_number": 16, "atomic_weight": 32.06},
    "Se": {"name": "Selenium", "atomic_number": 34, "atomic_weight": 78.971},
    "F": {"name": "Fluorine", "atomic_number": 9, "atomic_weight": 18.998},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "atomic_weight": 35.45},
    "Br": {"name": "Bromine", "atomic_number": 35, "atomic_weight": 79.904},
    "I": {"name": "Iodine", "atomic_number": 53, "atomic_weight": 126.90},
    "At": {"name": "Astatine", "atomic_number": 85, "atomic_weight": [210]},
    "Ts": {"name": "Tennesine", "atomic_number": 117, "atomic_weight": [294]},
    "He": {"name": "Helium", "atomic_number": 2, "atomic_weight": 4.0026},
    "Ne": {"name": "Neon", "atomic_number": 10, "atomic_weight": 20.180},
    "Ar": {"name": "Argon", "atomic_number": 18, "atomic_weight": 39.948},
    "Kr": {"name": "Krypton", "atomic_number": 36, "atomic_weight": 83.798},
    "Xe": {"name": "Xenon", "atomic_number": 54, "atomic_weight": 131.29},
    "Rn": {"name": "Radon", "atomic_number": 86, "atomic_weight": [222]},
    "Og": {"name": "Oganesson", "atomic_number": 118, "atomic_weight": [294]},
    }


def find_element(e):
    document.getElementById("result").innerHTML = " "
    element1 = document.getElementById('element-input').value.strip().title()

    # using .get() - no if statement
    info = non_metals.get(
        element1,
        {"name": "Element not found", "atomic_number": "-", "atomic_weight": "-"}
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b>{element1} <br>
    <b>Element:</b>{info['name']} <br>
    <b>Atomic number:</b>{info['atomic_number']} <br>
    <b>Atomic mass:</b>{info['atomic_weight']} <br>
    """