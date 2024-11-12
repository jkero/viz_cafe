import pandas as pd

# Exemple de données avec valeur marchande
data = {
    "Pays": ["Inde", "Inde", "Guatemala", "Costa Rica", "Panama", "Colombie", "Brésil", "Pérou", "Éthiopie", "Éthiopie"],
    "Région": ["Karnataka", "Kerala", "Amérique centrale", "Amérique centrale", "Amérique centrale", "Amérique du Sud", "Amérique du Sud", "Amérique du Sud", "Sidamo", "Yirgacheffe"],
    "Altitude (m)": [1000, 900, 1600, 1300, 1800, 1500, 900, 1800, 2000, 1900],
    "Type / Dénomination": ["Malabar (Arabica)", "Malabar (Arabica)", "Bourbon", "Typica", "Geisha", "Caturra", "Bourbon", "Typica", "Heirloom", "Heirloom"],
    "Acidité": ["Faible", "Faible", "Moyenne-Élevée", "Moyenne", "Très Élevée", "Moyenne", "Faible", "Élevée", "Élevée", "Très Élevée"],
    "Notes de Dégustation": ["Épicé, Boisé, Chocolaté", "Terreux, Noix, Épices", "Fruité, Chocolat, Agrumes", "Caramel, Agrumes", "Floral, Fruité, Notes d’Agrumes", "Chocolat, Noix", "Caramel, Chocolat, Noix", "Fruité, Floral", "Fruité, Floral, Notes de Baies", "Floral, Thé, Notes d'Agrumes"],
    "Valeur Marchande (USD/tonne)": ["3,500 - 4,000", "3,500 - 4,000", "4,000 - 5,000", "3,800 - 4,500", "10,000 - 20,000", "4,000 - 5,500", "3,500 - 4,500", "4,200 - 5,200", "6,000 - 9,000", "6,500 - 10,000"]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Afficher le tableau complet
print(df)
