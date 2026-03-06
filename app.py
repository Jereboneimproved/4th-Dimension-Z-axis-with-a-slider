import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Page Configuration ---
st.set_page_config(page_title="4D Matrix Scanner", page_icon="📟", layout="centered")

# --- 2. The 'Transparency' & 'Rain' Hack ---
# This CSS forces Streamlit's containers to be see-through so the background shows
matrix_style = """
<style>
    /* Force Transparency on Streamlit Elements */
    .stApp, .main, .block-container, [data-testid="stVerticalBlock"] {
        background-color: transparent !important;
    }
    
    body {
        background-color: black;
    }

    /* The Background Rain Container */
    .matrix-bg {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1;
        background: black;
        overflow: hidden;
    }

    .column {
        position: absolute;
        top: -1000px;
        color: #00FF41;
        font-family: monospace;
        font-size: 20px;
        text-shadow: 0 0 8px #00FF41;
        writing-mode: vertical-rl;
        text-orientation: upright;
        animation: fall linear infinite;
    }

    @keyframes fall {
        0% { transform: translateY(0); }
        100% { transform: translateY(2000px); }
    }
</style>
"""

# Create 20 random falling columns of code
rain_html = '<div class="matrix-bg">'
for i in range(20):
    left_pos = i * 5
    duration = np.random.randint(5, 15)
    delay = np.random.randint(0, 10)
    content = "".join(np.random.choice(["0", "1"], 50))
    rain_html += f'<div class="column" style="left:{left_pos}%; animation-duration:{duration}s; animation-delay:-{delay}s;">{content}</div>'
rain_html += '</div>'

st.markdown(matrix_style, unsafe_allow_html=True)
st.markdown(rain_html, unsafe_allow_html=True)

# --- 3. The Scanner UI ---
st.title("📟 4D Digital Scanner")
st.write("Intercepting higher-dimensional data streams...")

max_radius = st.slider("Actual Size of Object (3D Radius)", 10, 100, 50)
z_position = st.slider("Object's Position (Z-Axis)", -100, 100, 0)

# The Math
sq_val = max_radius**2 - z_position**2

fig, ax = plt.subplots()
ax.set_xlim(-110, 110)
ax.set_ylim(-110, 110)
ax.set_aspect('equal')
ax.set_facecolor('#000000') 
fig.patch.set_facecolor('black')

if sq_val > 0:
    visible_radius = np.sqrt(sq_val)
    # Core
    circle = plt.Circle((0, 0), visible_radius, color='#00FF41', ec='#D1FFD7', lw=3, alpha=0.9)
    ax.add_patch(circle)
    # Scanning Ring
    ring = plt.Circle((0, 0), visible_radius + 3, color='#00FF41', fill=False, lw=1, ls='--', alpha=0.6)
    ax.add_patch(ring)
    st.success(f"DIMENSIONAL BREACH: r={visible_radius:.2f}")
else:
    st.info("SCANNING VOID...")

ax.axis('off')
st.pyplot(fig)
