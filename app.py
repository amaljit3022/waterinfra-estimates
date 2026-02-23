import streamlit as st
from modules.structural.boundary_wall import calculate

st.set_page_config(
    page_title="WaterInfra Estimates",
    layout="wide"
)

st.title("🏗 WaterInfra Estimate Engine")
st.markdown("Professional Civil & Water Infrastructure Estimation Platform")

# =========================
# SIDEBAR NAVIGATION
# =========================

st.sidebar.title("Modules")

module = st.sidebar.selectbox(
    "Select Estimate Type",
    ["Boundary Wall"]
)

mode = st.sidebar.radio(
    "Calculation Mode",
    ["design", "practical"]
)

# =========================
# BOUNDARY WALL MODULE
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

        st.success("Calculation Completed")

        tab1, tab2, tab3 = st.tabs(["📦 Quantities", "🧱 Materials", "💰 Cost"])

        # =========================
        # TAB 1 - QUANTITIES
        # =========================
        with tab1:
            st.subheader("Quantity Summary")
            st.json(result["quantities"])

        # =========================
        # TAB 2 - MATERIALS
        # =========================
        with tab2:
            st.subheader("Material Breakdown")
            st.json(result["materials"])

        # =========================
        # TAB 3 - COST
        # =========================
        with tab3:
            st.info("Cost engine will be integrated in Phase 2.")