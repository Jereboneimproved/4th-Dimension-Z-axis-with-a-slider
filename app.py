import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Page Config & Matrix Rain CSS ---
st.set_page_config(page_title="4D Matrix Lab", page_icon="📟", layout="centered")

# This CSS creates three layers of falling 1s and 0s at different speeds/sizes
matrix_css = """
<style>
.matrix-container {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    z-index: -1;
    background-color: black;
    overflow: hidden;
    font-family: 'Courier New', Courier, monospace;
}

.layer {
    position: absolute;
    top: -100%;
    width: 100%;
    white-space: nowrap;
    word-wrap: break-word;
    color: #00FF41;
    opacity: 0.3;
    user-select: none;
}

/* Layer 1: Fast & Small (Background) */
.l1 { font-size: 10px; animation: fall 10s linear infinite; opacity: 0.1; }
/* Layer 2: Medium (Midground) */
.l2 { font-size: 20px; animation: fall 15s linear infinite; opacity: 0.2; }
/* Layer 3: Slow & Large (Foreground) */
.l3 { font-size: 40px; animation: fall 25s linear infinite; opacity: 0.05; }

@keyframes fall {
    from { transform: translateY(0%); }
    to { transform: translateY(200%); }
}
</style>
"""

# Injecting the Matrix Rain Background
matrix_content = "".join([np.random.choice(["0", "1", " "]) for _ in range(2000)])
st.markdown(matrix_css, unsafe_allow_html=True)
st.markdown(f'''
<div class="matrix-container">
    <div class="layer l1">{matrix_content * 5}</div>
    <div class="layer l2">{matrix_content * 3}</div>
    <div class="layer l3">{matrix_content}</div>
</div>
''', unsafe_allow_html=True)

# --- 2. App Logic ---
st.title("📟 4D Digital Scanner")
st.write("Intercepting higher-dimensional data...")

# Control Panel
max_radius = st.slider("Actual Size of Object (3D Radius)", 10, 100, 50)
z_position = st.slider("Object's Position in the 3rd Dimension (Z)", -100, 100, 0)

# Math
sq_val = max_radius**2 - z_position**2

# --- 3. Plotting ---
fig, ax = plt.subplots()
ax.set_xlim(-110, 110)
ax.set_ylim(-110, 110)
ax.set_aspect('equal')
ax.set_facecolor('#000000') 
fig.patch.set_facecolor('black')

if sq_val > 0:
    visible_radius = np.sqrt(sq_val)
    circle = plt.Circle((0, 0), visible_radius, 
                        color='#00FF41', 
                        ec='#D1FFD7', 
                        lw=3, 
                        alpha=0.9)
    ax.add_patch(circle)
    st.success(f"DIMENSIONAL BREACH: r = {visible_radius:.2f}")
else:
    st.info("NO DATA DETECTED IN CURRENT SLICE")

ax.axis('off')
st.pyplot(fig)
