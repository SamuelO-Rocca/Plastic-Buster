import os
import pandas as pd

def gerar_dados_sinteticos():
    os.makedirs("data/raw", exist_ok=True)
    synthetic_data = """fungus_name,environment,plastic_type,degradation_rate,temperature,ph,oxygen_level,moisture
Pestalotiopsis microspora,terrestre,PU,0.89,30,7.0,0.8,0.65
Aspergillus niger,aquatico,LDPE,0.56,28,6.8,0.7,0.75
Fusarium solani,terrestre,PET,0.72,32,7.4,0.9,0.6
Penicillium chrysogenum,aquatico,HDPE,0.64,27,6.5,0.85,0.8
Exophiala dermatitidis,vacuo,PP,0.47,10,7.2,0.1,0.05"""
    path = "data/raw/fungi_biodegradation.csv"
    with open(path, "w") as f:
        f.write(synthetic_data)
    print(f"[✔] Dados sintéticos criados em {path}")

# Chame antes do pipeline principal
if not os.path.exists("data/raw/fungi_biodegradation.csv"):
    gerar_dados_sinteticos()
