



import pandas as pd


df = pd.read_csv('donnees_fictives.csv', encoding='latin-1')

 # Sélection des personnes ayant une expérience supérieure à 10 ans et un diplôme de doctorat
result = df[(df['Annee_experience'] > 10) & (df['Diplome'] == 'Doctorat')]

# Enregistrement dans un nouveau fichier CSV
result.to_csv('result.csv', index=False)