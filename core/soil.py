"""
soil.py
-----------------------------------
Soil bearing capacity validation engine.
"""

SOIL_SBC = {
    "Soft Clay": 75,
    "Medium Clay": 100,
    "Loose Sand": 100,
    "Medium Sand": 150,
    "Dense Sand": 250,
    "Hard Soil": 300,
    "Rock": 600,
}


def get_sbc(soil_type: str) -> float:
    return SOIL_SBC.get(soil_type, 100)


def calculate_soil_pressure(
    wall_volume_per_m,
    pcc_volume_per_m,
    wall_density=20,
    concrete_density=25,
    foundation_width=0.6
):
    """
    Calculates soil pressure in kN/m² for 1 running meter.
    """

    wall_load = wall_volume_per_m * wall_density
    pcc_load = pcc_volume_per_m * concrete_density

    total_load = wall_load + pcc_load

    base_area = foundation_width * 1  # per meter length

    soil_pressure = total_load / base_area

    return round(soil_pressure, 2)


def required_foundation_width(total_load, sbc):
    """
    Calculates minimum width required to satisfy SBC.
    """

    width = total_load / sbc
    return round(width, 3)