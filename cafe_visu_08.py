import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# 4. Bar chart pour la valeur marchande moyenne par région
df_region_value = df.groupby('Région')['Valeur Marchande (USD/tonne)'].mean()
axs[1, 0].barh(df_region_value.index, df_region_value.values, color='orange')
axs[1, 0].set_title('Valeur marchande moyenne par région')
axs[1, 0].set_xlabel('Valeur Marchande moyenne (USD/tonne)')
axs[1, 0].set_ylabel('Région')

# 5. Histogramme de la distribution des valeurs marchandes
axs[1, 1].hist(df['Valeur Marchande (USD/tonne)'], bins=10, color='purple', alpha=0.7)
axs[1, 1].set_title('Répartition de la Valeur Marchande des Cafés')
axs[1, 1].set_xlabel('Valeur Marchande (USD/tonne)')
axs[1, 1].set_ylabel('Fréquence')

# 6. Un graphique vide ou un autre exemple si nécessaire
axs[1, 2].axis('off')  # Peut être utilisé pour un espace vide ou d'autres informations si nécessaire

# Ajuster les espacements pour éviter que les graphes ne se chevauchent
plt.tight_layout()

# Afficher les graphiques
plt.show()
