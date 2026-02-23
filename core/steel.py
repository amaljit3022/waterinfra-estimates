"""
steel.py
-----------------------------------
Steel weight calculations based on theoretical formula.

Formula:
Weight (kg) = (d^2 / 162) × Length (m)

Where:
d = diameter in mm
"""

from core.units import mm_to_m


def bar_weight(diameter_mm: float, length_m: float) -> float:
    """
    Calculate weight of single bar.
    """
    weight = (diameter_mm ** 2) / 162 * length_m
    return round(weight, 3)


def total_steel_weight(diameter_mm: float, total_length_m: float, mode="design") -> float:
    """
    Calculate total steel weight.
    mode:
        design     → exact theoretical
        practical  → includes 5% wastage
    """
    base_weight = (diameter_mm ** 2) / 162 * total_length_m

    if mode == "practical":
        base_weight *= 1.05  # 5% wastage

    return round(base_weight, 3)