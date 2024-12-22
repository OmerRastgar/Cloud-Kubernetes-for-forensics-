import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib import colormaps
from datetime import datetime

# Sample data
coordinates = [(1, 2), (1, 2), (3, 4), (3, 4), (5, 6), (5, 6)]  # Example 2D coordinates
times = ['10/26/2023 10:15', '10/27/2023 10:15', '10/28/2023 10:15',
         '10/29/2023 10:15', '10/30/2023 10:15', '10/31/2023 10:15']  # Example times
devices = [1, 2, 3, 2, 1, 3]  # Example devices
frequencies = [1, 2, 3, 4, 1, 5]  # Example frequencies

# Convert times to datetime objects
times = [datetime.strptime(time, "%m/%d/%Y %H:%M") for time in times]

# Normalize time values to create a color map (blue to red)
norm = plt.Normalize(min(times).timestamp(), max(times).timestamp())
cmap = colormaps.get_cmap('coolwarm')  # Updated method for getting colormap

# Plot setup
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through the data and plot each point
for i in range(len(coordinates)):
    x, y = coordinates[i]
    time = times[i]
    device = devices[i]
    frequency = frequencies[i]

    # Use time for color, device for marker shape, frequency for size
    color = cmap(norm(time.timestamp()))  # Color based on time
    if device == 1:
        marker = 'o'  # Circle for device 1
    elif device == 2:
        marker = '^'  # Triangle for device 2
    else:
        marker = 's'  # Square for device 3

    ax.scatter(x, y, c=[color], s=frequency*50, marker=marker, alpha=0.7, label=f"Device {device}, Time {time}")

# Set labels and title
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_title('Scatter Plot of Log Data')

# Create ScalarMappable for the color bar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])  # This is needed to create a colorbar
fig.colorbar(sm, ax=ax, label='Time (Color Gradient)')

# Display the plot
plt.show()
print("done")