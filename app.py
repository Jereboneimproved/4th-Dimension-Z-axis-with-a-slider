import time # Add this at the top with your imports

# --- Control Panel ---
with st.sidebar:
    auto_pulse = st.checkbox("🔌 Activate Neural Link (Auto-Pulse)")
    pulse_speed = st.slider("Pulse Frequency", 0.1, 2.0, 1.0)
    max_radius = st.slider("Actual Size of Object (3D Radius)", 10, 100, 50)

# Logic for Z-position
if auto_pulse:
    # Use time to create a sine wave for the Z-axis
    t = time.time() * pulse_speed
    z_position = np.sin(t) * max_radius
    st.sidebar.info(f"Auto-Z: {z_position:.2f}")
    # This forces Streamlit to rerun the script to animate
    time.sleep(0.05)
    st.rerun()
else:
    z_position = st.slider("Object's Position (Z-Axis)", -100, 100, 0)
