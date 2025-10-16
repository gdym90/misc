import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from grid_visualizer import create_grid, visualize_grid
from path_counter import count_paths_bfs

st.set_page_config(page_title="חוקר מסלולים", layout="wide")
st.title("חוקר מסלולים לילדים! 🗺️")

# Sidebar controls
st.sidebar.header("הגדרות רשת")
m = st.sidebar.slider("מספר כבישי רוחב", 2, 8, 2)
n = st.sidebar.slider("מספר כבישי אורך", 2, 8, 2)

# Create grid
grid = create_grid(m-1, n-1)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.subheader("הצגת הרשת")
    fig = visualize_grid(grid)
    st.pyplot(fig)

with col2:
    st.subheader("מונה מסלולים")
    if st.button("ספור מסלולים!"):
        # Create placeholders for progress indicators
        time_placeholder = st.empty()
        depth_placeholder = st.empty()
        paths_placeholder = st.empty()
        queue_length_placeholder = st.empty()
        progress_bar = st.progress(0)
        
        def update_progress(current_depth, paths_found, time_elapsed, queue_length):
            # Update time elapsed
            time_placeholder.write(f"⏱️ זמן שחלף: {time_elapsed:.3f} שניות")
            
            # Update current depth
            depth_placeholder.write(f"📏 עומק נוכחי: {current_depth}")
            
            # Update paths found
            paths_placeholder.write(f"🔢 מסלולים שנמצאו עד כה: {paths_found:,}")

            # Update queue length
            queue_length_placeholder.write(f"🔄 מסלולים חלקיים  {queue_length}")
            
            # Update progress bar (using a simple heuristic based on depth)
            # For a grid of size m x n, the maximum possible depth is roughly m + n
            max_possible_depth = m + n
            progress = min(1.0, current_depth / max_possible_depth)
            progress_bar.progress(progress)
        
        with st.spinner("מחפש מסלולים..."):
            total_paths, path_lengths, runtime = count_paths_bfs(grid, progress_callback=update_progress)
            
            # Clear progress indicators and show final results
            time_placeholder.empty()
            depth_placeholder.empty()
            paths_placeholder.empty()
            progress_bar.empty()
            
            st.write(f"✅ סה״כ מספר המסלולים: {total_paths:,}")
            st.write(f"⏱️ זמן חישוב סופי: {runtime:.3f} שניות")
            
            # Create a progress bar for path lengths
            st.subheader("חלוקת אורכי מסלולים")
            for length, count in sorted(path_lengths.items()):
                st.write(f"מסלולים באורך {length}: {count:,}")
                st.progress(min(1.0, count / total_paths))
