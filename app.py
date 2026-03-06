import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Page Config ---
st.set_page_config(page_title="4D Matrix Scanner", page_icon="📟", layout="centered")

# --- 2. Enhanced Matrix Rain CSS ---
# This uses 'text-shadow' to give that CRT glow and multiple z-index layers
matrix_css = """
<style>
    .main {
        background: transparent !important;
    }
    .stApp {
        background-color: black;
    }
    .matrix-bg {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1;
        overflow: hidden;
        background: black;
    }
    .layer {
        position: absolute;
        width: 100%;
        color: #00FF41;
        text-shadow: 0 0 5px #00FF41;
        white-space: pre-wrap;
        word-break: break-all;
        line-height: 1;
        opacity: 0.3;
    }
    /* Layer 1: Fast/Small */
    .l1 { font-size: 12px; animation: fall 8s linear infinite; opacity: 0.15; }
    /* Layer 2: Medium/Mid */
    .l2 { font-size: 22px; animation: fall 15s linear infinite; opacity: 0.25; top: -50%; }
    /* Layer 3: Slow/Large */
    .l3 { font-size: 45px; animation: fall 25s linear infinite; opacity: 0.1; top: -20%; }

    @keyframes fall {
        from { transform: translateY(-100%); }
        to { transform: translateY(100%); }
    }
</style>
"""

# Generate random digital noise
def gen_code(chars=1000):
    return "".join(np.random.choice(["0", "1", " ", " ", "0", "1"], chars))

st.markdown(matrix_css, unsafe_allow_html=True)
st.markdown(f"""
<div class="matrix-bg">
    <div class="layer l1">{gen_code(2000)}</div>
    <div class="layer l2">{gen_code(1000)}</div>
    <div class="layer l3">{gen_code(500)}</div>
</div>
""", unsafe_allow_html=True)

# --- 3. The 4D Scanner Logic ---
st.title("📟 4D Digital Scanner")
st.write("Intercepting higher-dimensional data streams...")

max_radius = st.slider("Actual Size of Object (3D Radius)", 10, 100, 50)
z_position = st.slider("Object's Position (Z-Axis)", -100, 100, 0)

sq_val = max_radius**2 - z_position**2

fig, ax = plt.subplots()
ax.set_xlim(-110, 110); ax.set_ylim(-110, 110)
ax.set_aspect('equal')
ax.set_facecolor('#000000') 
fig.patch.set_facecolor('black')

if sq_val > 0:
    visible_radius = np.sqrt(sq_val)
    # The Scanner Circle
    circle = plt.Circle((0, 0), visible_radius, color='#00FF41', ec='#D1FFD7', lw=3, alpha=0.9)
    ax.add_patch(circle)
    # Add a "Scanning" ring
    ring = plt.Circle((0, 0), visible_radius + 2, color='#00FF41', fill=False, lw=1, ls='--', alpha=0.5)
    ax.add_patch(ring)
    st.success(f"DIMENSIONAL BREACH DETECTED: r={visible_radius:.2f}")
else:
    st.info("SCANNING... NO DIMENSIONAL DATA DETECTED")

ax.axis('off')
st.pyplot(fig)
