"""
boundary_wall.py
-----------------------------------
Boundary Wall Quantity Estimation
Uses core calculation engine.
"""

from core.concrete import calculate_volume, calculate_materials_for_grade
from core.earthwork import excavation_volume


def calculate(
    length_m: float,
    height_m: float,
    wall_thickness_m: float,
    foundation_depth_m: float,
    foundation_width_m: float,
    concrete_grade="M15",
    mode="design",
) -> dict:

    # 1️⃣ Excavation
    excavation = excavation_volume(
        length_m,
        foundation_width_m,
        foundation_depth_m
    )

    # 2️⃣ PCC Foundation Volume
    pcc_volume = calculate_volume(
        length_m,
        foundation_width_m,
        0.1  # 100mm PCC
    )

    pcc_materials = calculate_materials_for_grade(
        pcc_volume,
        grade=concrete_grade,
        mode=mode
    )

    # 3️⃣ Brickwork Volume
    brickwork_volume = calculate_volume(
        length_m,
        wall_thickness_m,
        height_m
    )

    return {
        "input": {
            "length_m": length_m,
            "height_m": height_m,
            "wall_thickness_m": wall_thickness_m,
            "foundation_depth_m": foundation_depth_m,
            "foundation_width_m": foundation_width_m,
            "grade": concrete_grade,
            "mode": mode,
        },
        "quantities": {
            "excavation_cum": round(excavation, 3),
            "pcc_cum": round(pcc_volume, 3),
            "brickwork_cum": round(brickwork_volume, 3),
        },
        "materials": {
            "pcc_materials": pcc_materials,
        },
        "cost": {}
    }