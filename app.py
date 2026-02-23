import streamlit as st
from modules.structural.boundary_wall import calculate
from core.units import format_cum
from core.formatting import number_to_words

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="WaterInfra Estimates",
    layout="wide"
)

st.title("🏗 WaterInfra Estimate Engine")
st.markdown("Professional Civil & Water Infrastructure Estimation Platform")

# =========================
# SIDEBAR
# =========================

st.sidebar.title("Modules")

module = st.sidebar.selectbox(
    "Select Estimate Type",
    ["Boundary Wall"]
)

mode = st.sidebar.radio(
    "Calculation Mode",
    ["design", "practical"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("Mode: Design = Engineering Precision\n\nPractical = Includes site allowances")

# =========================
# MODULE: BOUNDARY WALL
# =========================

if module == "Boundary Wall":

    st.header("Boundary Wall Estimate")

    col1, col2, col3 = st.columns(3)

    with col1:
        length = st.number_input("Length (m)", min_value=0.0, value=20.0)
        height = st.number_input("Height (m)", min_value=0.0, value=2.0)

    with col2:
        thickness = st.number_input("Wall Thickness (m)", min_value=0.0, value=0.23)
        foundation_depth = st.number_input("Foundation Depth (m)", min_value=0.0, value=1.0)

    with col3:
        foundation_width = st.number_input("Foundation Width (m)", min_value=0.0, value=0.6)
        grade = st.selectbox("Concrete Grade", ["M10", "M15", "M20"])

    st.markdown("---")

    if st.button("Calculate Estimate"):

        result = calculate(
            length_m=length,
            height_m=height,
            wall_thickness_m=thickness,
            foundation_depth_m=foundation_depth,
            foundation_width_m=foundation_width,
            concrete_grade=grade,
            mode=mode
        )

        st.success("Calculation Completed Successfully")

        tab1, tab2, tab3 = st.tabs(["📦 Quantities", "🧱 Materials", "💰 Cost"])

        # =========================
        # TAB 1 – QUANTITIES
        # =========================
        with tab1:
            st.subheader("Quantity Summary")

            q = result["quantities"]

            st.markdown("### 🏗 Excavation")
            st.write(format_cum(q["excavation_cum"]))
            st.caption(number_to_words(q["excavation_cum"], "Cubic Metres"))

            st.markdown("### 🧱 PCC")
            st.write(format_cum(q["pcc_cum"]))
            st.caption(number_to_words(q["pcc_cum"], "Cubic Metres"))

            st.markdown("### 🧱 Brickwork")
            st.write(format_cum(q["brickwork_cum"]))
            st.caption(number_to_words(q["brickwork_cum"], "Cubic Metres"))

            st.markdown("### 🧱 Number of Bricks")
            st.write(f"{q['number_of_bricks']:,}")
            st.caption(number_to_words(q["number_of_bricks"], "Bricks"))

            st.markdown("### 🧱 Mortar")
            st.write(format_cum(q["mortar_cum"]))
            st.caption(number_to_words(q["mortar_cum"], "Cubic Metres"))

        # =========================
        # TAB 2 – MATERIALS
        # =========================
        with tab2:
            st.subheader("Material Breakdown")

            materials = result["materials"]["pcc_materials"]

            st.markdown("### Cement")
            st.write(f"{materials['cement_bags']} Bags")
            st.caption(number_to_words(materials["cement_bags"], "Bags"))

            st.markdown("### Sand")
            st.write(format_cum(materials["sand_cum"]))
            st.caption(number_to_words(materials["sand_cum"], "Cubic Metres"))

            st.markdown("### Aggregate")
            st.write(format_cum(materials["aggregate_cum"]))
            st.caption(number_to_words(materials["aggregate_cum"], "Cubic Metres"))

            st.markdown("### Water")
            st.write(f"{materials['water_litres']} Litres")
            st.caption(number_to_words(materials["water_litres"], "Litres"))

        # =========================
        # TAB 3 – COST (Future Phase)
        # =========================
        with tab3:
            st.info("Cost engine will be integrated in Phase 2 (SOR + BOQ automation).")