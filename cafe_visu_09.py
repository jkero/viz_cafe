import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Charger le fichier CSV
df = pd.read_csv("data_cafe_fric.csv")


# Convertir les valeurs marchandes en numériques (facultatif, en fonction du format des données)
#df['Valeur Marchande (USD/tonne)'] = df['Valeur Marchande (USD/tonne)'].str.extract('(\\d+,\\d+|\\d+)').replace({',': '.'}, regex=True).astype(float)

# Initialiser une figure avec des subplots (2 lignes et 3 colonnes)
fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# 1. Graphique à barres pour la valeur marchande par type de café
types = df.groupby('Type / Dénomination')['Valeur Marchande (USD/tonne)'].mean().sort_values().index
values = df.groupby('Type / Dénomination')['Valeur Marchande (USD/tonne)'].mean().sort_values()

axs[0, 0].bar(types, values)
axs[0, 0].set_title('Valeur marchande moyenne par type de café')
axs[0, 0].set_ylabel('Valeur marchande moyenne (USD/tonne)')

# Fixer les ticks avant de changer les labels
axs[0, 0].set_xticks(range(len(types)))
axs[0, 0].set_xticklabels(types, rotation=45)

# 2. Scatter plot pour l'altitude et la valeur marchande
scatter = axs[0, 1].scatter(df['Altitude (m)'], df['Valeur Marchande (USD/tonne)'], color='green', alpha=0.6)

# Ajouter les labels pour chaque point avec une rotation de 45 degrés
for i in range(len(df)):
    axs[0, 1].annotate(df['Type / Dénomination'][i], (df['Altitude (m)'][i], df['Valeur Marchande (USD/tonne)'][i]),
                       textcoords="offset points", xytext=(0,5), ha='center', fontsize=8, color='black', rotation=45)

axs[0, 1].set_title('Relation entre Altitude et Valeur Marchande')
axs[0, 1].set_xlabel('Altitude (m)')
axs[0, 1].set_ylabel('Valeur Marchande (USD/tonne)')

# 3. Boxplot pour la distribution de la valeur marchande selon le type de café
# Ajouter 'hue' pour éviter la dépréciation de 'palette' sans 'hue'
sns.boxplot(x='Type / Dénomination', y='Valeur Marchande (USD/tonne)', data=df, ax=axs[0, 2], hue='Type / Dénomination', palette='Set2', legend=False)
axs[0, 2].set_title('Distribution de la Valeur Marchande des Types de Café')

# Group by region and calculate the average value for the bar chart
df_region_value = df.groupby('Région')['Valeur Marchande (USD/tonne)'].mean().sort_values(ascending=False)

# Create the horizontal bar chart in the subplot
bars = axs[1, 0].barh(df_region_value.index, df_region_value.values, color='orange')

#---------
# Add country name inside the bars for each region
for i, bar in enumerate(bars):  # Iterate over the bars (patches)
    width = bar.get_width()  # Get the width of the bar (market value)
    region_name = df_region_value.index[i]  # Get the region name

    # Get countries within each region
    countries_in_region = df[df['Région'] == region_name]['Pays'].values

    # For simplicity, you can display the first country in the region's bar
    # If you want to display all countries, you can modify this part to list them
    country_name = ', '.join(countries_in_region[:3])  # Show up to 3 countries

    # Add country name inside the bar, centered both horizontally and vertically
    axs[1, 0].text(width / 2, bar.get_y() + bar.get_height() / 2,
                   f'{country_name}\n{width:.2f}',
                   va='center', ha='center', fontsize=8, color='black')
#--------
axs[1, 0].set_title('Valeur marchande moyenne par région')
axs[1, 0].set_xlabel('Valeur Marchande moyenne (USD/tonne)')
axs[1, 0].set_ylabel('Région')

# 5. Histogramme de la distribution des valeurs marchandes
axs[1, 1].hist(df['Valeur Marchande (USD/tonne)']/1000,bins='auto', color='purple', alpha=0.7)
#df_region_value = df.groupby('Région')['Valeur Marchande (USD/tonne)'].mean().sort_values(ascending=False)
axs[1, 1].yaxis.set_ticks(np.arange(0, 5, 1))
axs[1, 1].xaxis.set_ticks(np.arange(1, 6, .33333))
axs[1, 1].set_title('Répartition de la Valeur Marchande des Cafés')
axs[1, 1].set_xlabel('Valeur Marchande (USD/tonne)')
axs[1, 1].set_ylabel('Nb. de types dans ces valeurs')

# 6. Un graphique vide ou un autre exemple si nécessaire
axs[1, 2].axis('off')  # Peut être utilisé pour un espace vide ou d'autres informations si nécessaire

# Ajuster les espacements pour éviter que les graphes ne se chevauchent
plt.tight_layout()

# Afficher les graphiques
plt.show()
