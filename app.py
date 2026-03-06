import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="4D Slice Lab", page_icon="🌌")

st.title("🌌 4D Slice Lab")
st.write("Move the slider to push a 3D Sphere through our 2D reality.")

# --- Control Panel ---
max_radius = st.slider("Actual Size of Object (3D Radius)", 10, 100, 50)
z_position = st.slider("Object's Position in the 3rd Dimension (Z)", -100, 100, 0)

# The Math: r = sqrt(R^2 - d^2)
sq_val = max_radius**2 - z_position**2

# --- Create the Plot ---
fig, ax = plt.subplots()
ax.set_xlim(-110, 110)
ax.set_ylim(-110, 110)
ax.set_aspect('equal')

# APPLY MATRIX THEME HERE (Now that 'ax' exists)
ax.set_facecolor('#000000') # Absolute black void
fig.patch.set_facecolor('#0e1117') # Match Streamlit dark mode

if sq_val > 0:
    visible_radius = np.sqrt(sq_val)
    
    # Create the Matrix Green Circle
    circle = plt.Circle((0, 0), visible_radius, 
                        color='#00FF41',    # Matrix Green
                        ec='#D1FFD7',       # Glow edge
                        lw=3, 
                        alpha=0.8)          
    
    ax.add_patch(circle)
    st.success(f"Object detected! Visible radius: {visible_radius:.2f}")
else:
    st.warning("Object is outside our dimension. Nothing to see... yet.")

# Hide the axis numbers for a cleaner "Scanner" look
ax.axis('off')

st.pyplot(fig)
