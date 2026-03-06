import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🌌 4D Slice Lab")
st.write("Move the slider to push a 3D Sphere through our 2D reality.")

# Control Panel
max_radius = st.slider("Actual Size of Object (3D Radius)", 10, 100, 50)
z_position = st.slider("Object's Position in the 3rd Dimension (Z)", -100, 100, 0)

# The Math: r = sqrt(R^2 - d^2)
sq_val = max_radius**2 - z_position**2

fig, ax = plt.subplots()
ax.set_xlim(-110, 110)
ax.set_ylim(-110, 110)
ax.set_aspect('equal')
ax.set_facecolor('#1e1e1e') # Dark space

if sq_val > 0:
    visible_radius = np.sqrt(sq_val)
    circle = plt.Circle((0, 0), visible_radius, color='#00ff96', ec='white', lw=2)
    ax.add_patch(circle)
    st.success(f"Object detected! Visible radius: {visible_radius:.2f}")
else:
    st.warning("Object is outside our dimension. Nothing to see... yet.")

st.pyplot(fig)
