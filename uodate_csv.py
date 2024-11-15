# Updated CSV content with the new row for Guatemala (Huehuetenango)
updated_csv_content = """
Pays,Région,Altitude (m),Type / Dénomination,Grain vert,Aspect physique,Qualité sensorielle,Acidité,Corps,Saveur,Amertume,Equilibre,Finale,Valeur Marchande (USD/tonne)
Brésil,Minas Gerais,1100,Bourbon,Vert,Foncé,Moyenne,Modérée,Fort,Saveur chocolatée,Modérée,Bon,Longue,2200
Colombie,Antioquia,1500,Arabica,Vert,Clair,Bonne,Elevée,Equilibré,Saveur fruitée et caramel,Modérée,Excellente,Longue,2500
Ethiopie,Yirgacheffe,1900,Heirloom,Vert,Lumineux,Excellente,Elevée,Corps léger,Saveur florale et fruitée,Modérée,Excellente,Longue,3000
Guatemala,Huehuetenango,1800,SHB,Vert,Lumineux,Excellente,Elevée,Corps moyen,Saveur fruitée et florale,Modérée,Excellente,Longue,2800
Jamaïque,Blue Mountain,1600,Blue Mountain,Vert,Foncé,Excellente,Modérée,Corps moyen,Saveur douce et légère,Faible,Excellente,Longue,5000
Inde,Karnataka,1200,Arabica,Vert,Clair,Moyenne,Modérée,Equilibré,Saveur douce,Modérée,Bonne,Longue,2400
Kenya,Central,1700,AA,Vert,Foncé,Excellente,Elevée,Fort,Saveur fruitée et acide,Modérée,Excellente,Longue,3200
Mexique,Chiapas,1500,Arabica,Vert,Clair,Bien,Elevée,Equilibré,Saveur douce et fruitée,Modérée,Bonne,Longue,2300
Nicaragua,Matagalpa,1300,Arabica,Vert,Lumineux,Moyenne,Elevée,Equilibré,Saveur douce,Modérée,Bonne,Longue,2100
Perou,Chanchamayo,1400,Arabica,Vert,Foncé,Moyenne,Modérée,Fort,Saveur douce et équilibrée,Modérée,Bonne,Longue,2000
Rwanda,Nord,1600,Arabica,Vert,Foncé,Excellente,Elevée,Fort,Saveur fruitée et florale,Modérée,Excellente,Longue,3000
Tanzanie,Arusha,1200,Arabica,Vert,Lumineux,Excellente,Elevée,Corps moyen,Saveur fruitée et acidulée,Modérée,Excellente,Longue,2700
Vietnam,Central Highlands,1000,Robusta,Vert,Foncé,Moyenne,Basse,Fort,Saveur terreuse et boisée,Fort,Bon,Longue,1500
"""

# Save the content to a CSV file
with open("data_cafe_fric.csv", "w") as f:
    f.write(updated_csv_content)

print("Updated CSV file has been saved.")
