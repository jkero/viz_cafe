import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
df = pd.read_csv('coffee_data.csv')

# Set the plot style for readability
sns.set(style="whitegrid")

# Create a figure
plt.figure(figsize=(12, 8))

# Scatter plot for Region vs Grain Type, with color representing Market Value
scatter = plt.scatter(
    x=df['Region'],              # X-axis: Region
    y=df['Bean Type'],           # Y-axis: Grain Type
    c=df['Market Value (USD/tonne)'],  # Color by Market Value
    cmap='viridis',              # Colormap for Market Value
    s=100,                       # Size of points
    alpha=0.7                    # Transparency for overlap
)

# Add color bar for Market Value
color_bar = plt.colorbar(scatter)
color_bar.set_label('Market Value (USD/tonne)')

# Set labels and title
plt.xlabel('Region')
plt.ylabel('Bean Type')
plt.title('Market Value by Region and Bean Type')

# Rotate x-axis labels for readability
plt.xticks(rotation=45)

# Show plot
plt.tight_layout()
plt.show()
