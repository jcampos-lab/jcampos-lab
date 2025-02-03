import matplotlib.pyplot as plt
import numpy as np

# Data
dimensions = ['Power Distance', 'Individualism', 'Masculinity', 'Uncertainty Avoidance', 'Long-Term Orientation', 'Indulgence']
germany_scores = [35, 67, 66, 65, 83, 40]  # Example scores for Germany
russia_scores = [93, 39, 36, 95, 81, 20]   # Example scores for Russia

# Positions for the bars
x = np.arange(len(dimensions))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35

# Plot bars for Germany and Russia
bar1 = ax.bar(x - bar_width/2, germany_scores, bar_width, label='Germany', color='black')
bar2 = ax.bar(x + bar_width/2, russia_scores, bar_width, label='Russia', color='red')

# Add labels, title, and legend
ax.set_xlabel('Cultural Dimensions')
ax.set_ylabel('Scores')
ax.set_title("Hofstede's Cultural Dimensions: Germany vs. Russia")
ax.set_xticks(x)
ax.set_xticklabels(dimensions, rotation=45, ha='right')
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

# Data
dimensions = ['Power Distance', 'Individualism', 'Masculinity', 'Uncertainty Avoidance', 'Long-Term Orientation', 'Indulgence']
germany_scores = [35, 67, 66, 65, 83, 40]  # Example scores for Germany
russia_scores = [93, 39, 36, 95, 81, 20]   # Example scores for Russia

# Positions for the bars
x = np.arange(len(dimensions))
bar_width = 0.35

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Function to create rounded bars
def rounded_bar(ax, x, y, width, color, label):
    for i, (xi, yi) in enumerate(zip(x, y)):
        # Create a rounded rectangle for each bar
        box = FancyBboxPatch(
            (xi - width / 2, 0), width, yi,
            boxstyle=f"round,pad=0,rounding_size=0.1",
            edgecolor="none", facecolor=color, label=label if i == 0 else None
        )
        ax.add_patch(box)

# Plot rounded bars for Germany and Russia
rounded_bar(ax, x - bar_width / 2, germany_scores, bar_width, color='yellow', label='Germany')
rounded_bar(ax, x + bar_width / 2, russia_scores, bar_width, color='purple', label='Russia')

# Add labels, title, and legend
ax.set_xlabel('Cultural Dimensions')
ax.set_ylabel('Scores')
ax.set_title("Hofstede's Cultural Dimensions: Germany vs. Russia (Rounded Bars)")
ax.set_xticks(x)
ax.set_xticklabels(dimensions, rotation=45, ha='right')
ax.legend()

# Set y-axis limit for better visualization
ax.set_ylim(0, 100)

# Show the plot
plt.tight_layout()
plt.show()

