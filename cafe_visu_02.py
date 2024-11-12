import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
df = pd.read_csv("data_cafe.csv")

# Initialiser la figure avec deux sous-graphiques
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

# Diagramme de dispersion : Relation entre altitude et acidité
sns.scatterplot(data=df, x="Altitude (m)", y="Acidité", hue="Type / Dénomination", ax=axs[0])
axs[0].set_title("Altitude vs Acidité des cafés par Type/Dénomination")
axs[0].legend(loc='upper left', bbox_to_anchor=(1.2, 1))  # Pour ajuster la légende hors du graphique si nécessaire
#axs[0].legend(loc='upper center', bbox_to_anchor=(0.5, -1.15), ncol=7, fancybox=True, shadow=True)
# Carte de chaleur : Types de café par région
types_par_region = df.pivot_table(index="Région", columns="Type / Dénomination", aggfunc="size", fill_value=0)
sns.heatmap(types_par_region, annot=True, cmap="YlGnBu", ax=axs[1])
axs[1].set_title("Types de Café par Région")

# Afficher la figure
plt.tight_layout()
plt.show()
