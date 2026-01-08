import pandas as pd
import numpy as np

def generate_mockup_medical_data(num_samples=100, filename='mockup_medical_data.csv'):
    # Define uma semente para reprodutibilidade dos dados de mockup
    np.random.seed(42) 

    # Gerando dados de mockup com distribuições realistas
    data = {
        'id': range(num_samples),
        'age': np.random.randint(18, 65, num_samples), # Idade entre 18 e 65 anos
        'sex': np.random.randint(1, 3, num_samples), # 1 para mulher, 2 para homem
        'height': np.random.randint(150, 190, num_samples), # Altura em cm
        'weight': np.random.randint(50, 100, num_samples), # Peso em kg
        'ap_hi': np.random.randint(100, 180, num_samples), # Pressão sistólica
        'ap_lo': np.random.randint(60, 120, num_samples), # Pressão diastólica
        'cholesterol': np.random.randint(1, 4, num_samples), # 1=normal, 2=acima do normal, 3=muito acima
        'gluc': np.random.randint(1, 4, num_samples), # 1=normal, 2=acima do normal, 3=muito acima
        'smoke': np.random.randint(0, 2, num_samples), # 0=não, 1=sim
        'alco': np.random.randint(0, 2, num_samples), # 0=não, 1=sim
        'active': np.random.randint(0, 2, num_samples), # 0=não, 1=sim
        'cardio': np.random.randint(0, 2, num_samples) # 0=saudável, 1=doente
    }

    # Cria o DataFrame e salva no CSV
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Arquivo '{filename}' gerado com {num_samples} linhas de dados de mockup.")

if __name__ == "__main__":
    generate_mockup_medical_data(num_samples=100)
