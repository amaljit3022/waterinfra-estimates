from modules.structural.boundary_wall import calculate

result = calculate(
    length_m=20,
    height_m=2,
    wall_thickness_m=0.23,
    foundation_depth_m=1,
    foundation_width_m=0.6,
    concrete_grade="M15",
    mode="design"
)

print(result)