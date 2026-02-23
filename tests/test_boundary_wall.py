from modules.structural.boundary_wall import calculate


def test_basic_boundary_wall_volume():
    result = calculate(
        length_m=20,
        height_m=2,
        wall_thickness_m=0.23,
        foundation_depth_m=1,
        foundation_width_m=0.6,
        concrete_grade="M15",
        mode="design",
    )

    # Check excavation volume
    assert result["quantities"]["excavation_cum"] == 12.0

    # Check PCC volume
    assert result["quantities"]["pcc_cum"] == 1.2

    # Check brickwork volume (allow small rounding tolerance)
    assert round(result["quantities"]["brickwork_cum"], 2) == 9.2


def test_brick_and_mortar_calculation():
    result = calculate(
        length_m=20,
        height_m=2,
        wall_thickness_m=0.23,
        foundation_depth_m=1,
        foundation_width_m=0.6,
        concrete_grade="M15",
        mode="design",
    )

    # Expected brickwork volume
    expected_brickwork = 20 * 0.23 * 2

    # Expected bricks (approx 500 bricks per m3)
    expected_bricks = int(round(expected_brickwork * 500))

    assert result["quantities"]["number_of_bricks"] == expected_bricks

    # Mortar approx 25% of brickwork
    expected_mortar = round(expected_brickwork * 0.25, 3)

    assert result["quantities"]["mortar_cum"] == expected_mortar


def test_soil_pressure_calculation():
    result = calculate(
        length_m=20,
        height_m=2,
        wall_thickness_m=0.23,
        foundation_depth_m=1,
        foundation_width_m=0.6,
        concrete_grade="M15",
        mode="design",
    )

    engineering = result["engineering"]

    soil_pressure = engineering["soil_pressure_kNm2"]

    # Soil pressure must be positive
    assert soil_pressure > 0

    # Very basic sanity check range (should not be extreme)
    assert soil_pressure < 500


def test_zero_height_wall():
    result = calculate(
        length_m=20,
        height_m=0,
        wall_thickness_m=0.23,
        foundation_depth_m=1,
        foundation_width_m=0.6,
        concrete_grade="M15",
        mode="design",
    )

    # Brickwork volume should be zero
    assert result["quantities"]["brickwork_cum"] == 0

    # Number of bricks should be zero
    assert result["quantities"]["number_of_bricks"] == 0

    # Mortar should be zero
    assert result["quantities"]["mortar_cum"] == 0


import pytest


def test_negative_height_should_fail():
    with pytest.raises(ValueError):
        calculate(
            length_m=20,
            height_m=-2,
            wall_thickness_m=0.23,
            foundation_depth_m=1,
            foundation_width_m=0.6,
            concrete_grade="M15",
            mode="design",
        )


def test_zero_foundation_width_should_fail():
    import pytest

    with pytest.raises(ValueError):
        calculate(
            length_m=20,
            height_m=2,
            wall_thickness_m=0.23,
            foundation_depth_m=1,
            foundation_width_m=0,
            concrete_grade="M15",
            mode="design",
        )
