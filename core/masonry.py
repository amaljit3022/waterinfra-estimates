"""
masonry.py
-----------------------------------
Brickwork and mortar calculations.
"""

def bricks_per_cum(brick_with_mortar_volume=0.002):
    """
    Returns number of bricks per cubic meter.
    Default: 0.002 m³ per brick (with mortar)
    """
    return 1 / brick_with_mortar_volume


def brick_count(brickwork_volume_cum: float, mode="design") -> int:
    """
    Calculate number of bricks required.
    """
    base_bricks = brickwork_volume_cum * bricks_per_cum()

    if mode == "practical":
        base_bricks *= 1.05  # 5% breakage

    return int(round(base_bricks))


def mortar_volume(brickwork_volume_cum: float) -> float:
    """
    Mortar volume approx 25% of brickwork volume.
    """
    return round(brickwork_volume_cum * 0.25, 3)