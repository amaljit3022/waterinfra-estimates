"""
concrete.py
-----------------------------------
Concrete volume and material calculation engine.
Based on nominal mix proportions.
"""

from core.units import cum_to_litre


# Nominal mix ratios (Cement : Sand : Aggregate)
NOMINAL_MIX = {
    "M10": (1, 3, 6),
    "M15": (1, 2, 4),
    "M20": (1, 1.5, 3),
}


def calculate_volume(length_m: float, breadth_m: float, height_m: float) -> float:
    """
    Calculate geometric concrete volume.
    """
    volume = length_m * breadth_m * height_m
    return round(volume, 4)


def calculate_materials_for_grade(volume_cum: float, grade="M20", mode="design") -> dict:
    """
    Calculate cement, sand, aggregate quantities.

    Assumption:
    Dry volume factor = 1.54
    Cement density = 1440 kg/m3
    1 bag cement = 50 kg
    """

    dry_volume = volume_cum * 1.54

    cement_ratio, sand_ratio, agg_ratio = NOMINAL_MIX[grade]
    total_ratio = cement_ratio + sand_ratio + agg_ratio

    cement_vol = (cement_ratio / total_ratio) * dry_volume
    sand_vol = (sand_ratio / total_ratio) * dry_volume
    agg_vol = (agg_ratio / total_ratio) * dry_volume

    cement_kg = cement_vol * 1440
    cement_bags = cement_kg / 50

    water_litres = volume_cum * 180  # Approx 180 L/m3

    if mode == "practical":
        cement_bags *= 1.03
        sand_vol *= 1.02
        agg_vol *= 1.02

    return {
        "cement_bags": round(cement_bags, 2),
        "sand_cum": round(sand_vol, 3),
        "aggregate_cum": round(agg_vol, 3),
        "water_litres": round(water_litres, 1),
    }