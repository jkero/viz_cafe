import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le fichier CSV
df = pd.read_csv("data_cafe_fric.csv")

# Afficher les premières lignes
print(df.head())

# Création d'une visualisation simple avec Seaborn (par exemple, une carte de chaleur pour les valeurs marchandes)
# Nous devons d'abord convertir les valeurs marchandes en numériques (facultatif selon les besoins)
# Ici, nous allons uniquement afficher une visualisation des colonnes pertinentes

# Placer les valeurs marchandes dans une colonne numérique
df['Valeur Marchande (USD/tonne)'] = df['Valeur Marchande (USD/tonne)'].str.extract('(\\d+,\\d+|\\d+)').replace({',': '.'}, regex=True).astype(float)

# Affichage d'une carte de chaleur (en fonction de la valeur marchande)
plt.figure(figsize=(10, 6))
sns.heatmap(df[['Altitude (m)', 'Valeur Marchande (USD/tonne)']].corr(), annot=True, cmap="YlGnBu")
plt.title("Carte de chaleur entre l'altitude et la valeur marchande")
plt.show()
