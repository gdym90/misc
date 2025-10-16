from collections import deque
import time
import numpy as np
import streamlit as st


def get_neighbors(grid, position):
    """Get valid neighboring intersections in the grid."""
    m, n = grid.shape  # m x n grid of roads
    num_intersections_y = m + 1  # number of intersections vertically
    num_intersections_x = n + 1  # number of intersections horizontally
    
    i, j = position
    neighbors = []
    
    # Check all four directions (roads)
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i + di, j + dj
        # Check if the new position is within the intersection grid
        if 0 <= ni < num_intersections_y and 0 <= nj < num_intersections_x:
            neighbors.append((ni, nj))
    
    return neighbors

def count_paths_bfs(grid, progress_callback=None):
    """Count all possible paths from bottom-left to top-right intersection using BFS.
    Returns (total_paths, path_lengths, runtime_seconds)
    
    Args:
        grid: The grid to count paths in
        progress_callback: Optional callback function that receives (current_depth, paths_found, time_elapsed)
    """
    start_time = time.time()
    
    m, n = grid.shape  # m x n grid of roads
    num_intersections_y = m + 1  # number of intersections vertically
    num_intersections_x = n + 1  # number of intersections horizontally
    
    total_paths = 0
    path_lengths = {}
    max_depth = 0
    
    # Start position (bottom-left intersection)
    start = (m, 0)  # (num_intersections_y - 1, 0)
    # End position (top-right intersection)
    end = (0, n)    # (0, num_intersections_x - 1)
    
    queue = deque()
    queue.append(([start], 0))  # (path, length)
    
    while queue:
        path, length = queue.popleft()
        current = path[-1]
        
        # Update max depth if needed
        if length > max_depth:
            max_depth = length
            if progress_callback:
                progress_callback(max_depth, total_paths, time.time() - start_time, len(queue))
        
        # If we reached the end, count this path
        if current == end:
            if length not in path_lengths:
                path_lengths[length] = 0
            path_lengths[length] += 1
            total_paths += 1
            continue
        
        # Add neighbors to queue
        for neighbor in get_neighbors(grid, current):
            if neighbor not in path:  # Avoid cycles
                new_path = path + [neighbor]
                queue.append((new_path, length + 1))

    progress_callback(max_depth, total_paths, time.time() - start_time, len(queue))
    
    runtime_seconds = time.time() - start_time
    return total_paths, path_lengths, runtime_seconds 