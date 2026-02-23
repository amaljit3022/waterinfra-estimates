"""
boundary_wall.py
-----------------------------------
Boundary Wall Quantity Estimation
Uses core calculation engine.
"""

from core.concrete import calculate_volume, calculate_materials_for_grade
from core.earthwork import excavation_volume
from core.masonry import brick_count, mortar_volume
from core.soil import calculate_soil_pressure, required_foundation_width


def calculate(
    length_m: float,
    height_m: float,
    wall_thickness_m: float,
    foundation_depth_m: float,
    foundation_width_m: float,
    concrete_grade="M15",
    mode="design",
) -> dict:

    # -------------------------
    # Input Validation
    # -------------------------
    if length_m < 0:
        raise ValueError("Length cannot be negative")

    if height_m < 0:
        raise ValueError("Height cannot be negative")
    if wall_thickness_m <= 0:
        raise ValueError("Wall thickness must be greater than zero")
    if foundation_depth_m < 0:
        raise ValueError("Foundation depth cannot be negative")

    if foundation_width_m <= 0:
        raise ValueError("Foundation width must be greater than zero")

    # 1️⃣ Excavation
    excavation = excavation_volume(length_m, foundation_width_m, foundation_depth_m)

    # 2️⃣ PCC Foundation Volume
    pcc_volume = calculate_volume(length_m, foundation_width_m, 0.1)  # 100mm PCC

    pcc_materials = calculate_materials_for_grade(
        pcc_volume, grade=concrete_grade, mode=mode
    )

    # 3️⃣ Brickwork Volume
    # 3️⃣ Brickwork Volume
    brickwork_volume = calculate_volume(length_m, wall_thickness_m, height_m)

    bricks_required = brick_count(brickwork_volume, mode=mode)
    mortar_required = mortar_volume(brickwork_volume)

    # 4️⃣ Engineering Check (Per Running Meter)

    total_wall_height = height_m + foundation_depth_m
    wall_volume_per_m = wall_thickness_m * total_wall_height
    pcc_volume_per_m = foundation_width_m * 0.1 * 1

    soil_pressure = calculate_soil_pressure(
        wall_volume_per_m, pcc_volume_per_m, foundation_width=foundation_width_m
    )

    total_load = wall_volume_per_m * 20 + pcc_volume_per_m * 25

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
            "number_of_bricks": bricks_required,
            "mortar_cum": mortar_required,
        },
        "materials": {
            "pcc_materials": pcc_materials,
        },
        "cost": {},
        "engineering": {
            "soil_pressure_kNm2": soil_pressure,
            "total_load_kN_per_m": round(total_load, 2),
        },
    }
