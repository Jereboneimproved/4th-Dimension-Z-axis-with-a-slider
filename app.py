import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --- 1. Page Configuration ---
st.set_page_config(page_title="4D Matrix Scanner", page_icon="📟", layout="centered")

# --- 2. The Matrix Rain & Transparency CSS ---
matrix_style = """
<style>
    .stApp, .main, .block-container, [data-testid="stVerticalBlock"] {
        background-color: transparent !important;
    }
    body { background-color: black; }
    .matrix-bg {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1; background: black; overflow: hidden;
    }
    .column {
        position: absolute; top: -1000px; color: #00FF41;
        font-family: monospace; font-size: 20px;
        text-shadow: 0 0 8px #00FF41; writing-mode: vertical-rl;
        text-orientation: upright; animation: fall linear infinite;
    }
    @keyframes fall {
        0% { transform: translateY(0); }
        100% { transform: translateY(2000px); }
    }
</style>
"""

# Create the Rain Background
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

# --- 3. System Terminal (Sidebar) ---
with st.sidebar:
    st.header("⚡ System Terminal")
    auto_pulse = st.checkbox("🔌 Activate Neural Link (Auto-Pulse)")
    pulse_speed = st.slider("Pulse Frequency", 0.1, 5.0, 1.0)
    max_radius = st.slider("Actual Size (3D Radius)", 10, 100, 50)
    
    # Logic for Z-positioning
    if auto_pulse:
        t = time.time() * pulse_speed
        z_pos = np.sin(t) * max_radius
        st.info(f"AUTO-SCANNING Z: {z_pos:.2f}")
    else:
        z_pos = st.slider("Manual Z-Axis Control", -100.0, 100.0, 0.0)

# --- 4. Scanner Visualization ---
st.title("📟 4D Digital Scanner")
st.write("Intercepting higher-dimensional data streams...")

# Math
sq_val = max_radius**2 - z_pos**2

fig, ax = plt.subplots()
ax.set_xlim(-110, 110); ax.set_ylim(-110, 110)
ax.set_aspect('equal')
ax.set_facecolor('#000000') 
fig.patch.set_facecolor('black')

if sq_val > 0:
    visible_radius = np.sqrt(sq_val)
    # Draw Circle & Scanner Ring
    ax.add_patch(plt.Circle((0, 0), visible_radius, color='#00FF41', ec='#D1FFD7', lw=3, alpha=0.9))
    ax.add_patch(plt.Circle((0, 0), visible_radius + 3, color='#00FF41', fill=False, lw=1, ls='--', alpha=0.6))
    st.success(f"DIMENSIONAL BREACH: r={visible_radius:.2f}")
else:
    st.info("SCANNING VOID... NO DATA DETECTED")

ax.axis('off')
st.pyplot(fig)

# Force refresh for animation if Auto-Pulse is on
if auto_pulse:
    time.sleep(0.05)
    st.rerun()
