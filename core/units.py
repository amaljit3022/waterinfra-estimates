"""
units.py
-----------------------------------
Unit handling and standard engineering constants.
All units must be SI (unless explicitly converted).
"""

# Length
MM_TO_M = 0.001
CM_TO_M = 0.01

# Area
SQMM_TO_SQM = 1e-6

# Volume
CUM_TO_LITRE = 1000

# Density
STEEL_DENSITY = 7850  # kg/m3

# Gravity
GRAVITY = 9.81  # m/s2

def mm_to_m(value_mm: float) -> float:
    return value_mm * MM_TO_M

def cm_to_m(value_cm: float) -> float:
    return value_cm * CM_TO_M

def cum_to_litre(volume_cum: float) -> float:
    return volume_cum * CUM_TO_LITRE