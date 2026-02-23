"""
earthwork.py
-----------------------------------
Earthwork calculations
"""

def excavation_volume(length_m: float, width_m: float, depth_m: float) -> float:
    return round(length_m * width_m * depth_m, 4)