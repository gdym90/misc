import numpy as np
import matplotlib.pyplot as plt

def create_grid(m, n):
    """Create an M x N grid of roads (which has (M+1) x (N+1) intersections)."""
    return np.zeros((m, n), dtype=int)

def visualize_grid(grid):
    """Create a visualization of the grid using matplotlib, with roads as lines."""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # The grid has (m+1) x (n+1) intersections
    m, n = grid.shape
    num_intersections_x = n + 1
    num_intersections_y = m + 1
    
    # Set up the grid lines (roads)
    ax.set_xticks(np.arange(0, num_intersections_x, 1))
    ax.set_yticks(np.arange(0, num_intersections_y, 1))
    ax.grid(True, color='black', linewidth=2)
    
    # Hide the axes labels but keep the grid
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    # Add intersection point labels
    for i in range(num_intersections_y):
        for j in range(num_intersections_x):
            ax.text(j, i, f'({i},{j})', ha='center', va='center', fontsize=10, 
                   bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
    
    # Mark start point (bottom-left intersection) with green star
    start_i, start_j = m, 0
    ax.plot(start_j, start_i, 'g*', markersize=30, label='Start')
    
    # Mark end point (top-right intersection) with red star
    end_i, end_j = 0, n
    ax.plot(end_j, end_i, 'r*', markersize=30, label='End')
    
    # Add legend
    ax.legend(loc='upper right')
    
    # Set limits and aspect ratio
    ax.set_xlim(-0.5, num_intersections_x - 0.5)
    ax.set_ylim(-0.5, num_intersections_y - 0.5)
    ax.set_aspect('equal')
    
    # Add title showing both grid size and number of intersections
    graph_title = f'רשת כבישים: {m+1}x{n+1} צמתים'
    reversed_title = graph_title[::-1]
    ax.set_title(reversed_title, fontsize=16)
    
    return fig 