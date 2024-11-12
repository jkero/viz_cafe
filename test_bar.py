import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your dataframe
df = pd.read_csv("data_cafe_fric.csv")

## Group by country and calculate the average value for the bar chart
country_values = df.groupby('Pays')['Valeur Marchande (USD/tonne)'].mean().sort_values()

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(country_values.index, country_values.values, color='skyblue')

# Add country name on the right of each bar
for bar in bars:
    width = bar.get_width()  # Get the width of the bar (market value)
    ax.text(width + -800, bar.get_y() + bar.get_height() / 2, f'{width:.2f}',
            va='center', ha='left', fontsize=10, color='black')

# Set the title and labels
ax.set_title('Valeur Marchande moyenne par pays')
ax.set_xlabel('Valeur Marchande moyenne (USD/tonne)')
ax.set_ylabel('Pays')

# Show the plot
plt.tight_layout()
plt.show()
