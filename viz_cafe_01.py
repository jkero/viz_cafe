import pandas as pd

# Charger le dataset
df = pd.read_csv("data_cafe.csv")

# Afficher les premières lignes
print(df.head())

altitude_par_region = df.groupby("Région")["Altitude (m)"].mean()
print(altitude_par_region)
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(data=df, x="Altitude (m)", y="Acidité", hue="Type / Dénomination")
plt.title("Altitude vs Acidité des cafés par Type/Dénomination")
plt.show()

types_par_region = df.pivot_table(index="Région", columns="Type / Dénomination", aggfunc="size", fill_value=0)
sns.heatmap(types_par_region, annot=True, cmap="YlGnBu")
plt.title("Types de Café par Région")
plt.show()


