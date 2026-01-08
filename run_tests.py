#Este arquivo usa a biblioteca unittest padrão do Python para testar a função calculate_medical_data.

import unittest
import pandas as pd
from medical_data_visualizer import calculate_medical_data

class MedicalDataTests(unittest.TestCase):
    # Definimos um pequeno conjunto de dados de teste estático como string CSV
    TEST_CSV_DATA = """id,age,sex,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio
1,18383,2,168,62.0,110,80,1,1,0,0,1,0
2,20228,1,156,85.0,140,90,3,1,0,0,1,1
3,18857,2,165,64.0,120,90,2,2,0,0,0,1
4,17623,1,169,82.0,150,100,1,1,0,0,1,1
5,17474,1,154,56.0,100,60,1,1,0,0,1,0
6,18383,2,168,62.0,110,80,1,1,0,0,1,0
7,20228,1,156,85.0,140,90,3,1,0,0,1,1
8,18857,2,165,64.0,120,90,2,2,0,0,0,1
9,17623,1,169,82.0,150,100,1,1,0,0,1,1
10,17474,1,154,56.0,100,60,1,1,0,0,1,0"""

    def setUp(self):
        # Configura o ambiente de teste: Salva os dados de teste em um arquivo temporário
        with open("test_data.csv", "w") as f:
            f.write(self.TEST_CSV_DATA)
        self.df = calculate_medical_data(csv_file="test_data.csv")

    def test_overweight_column(self):
        # Testa se a lógica de 'overweight' funciona corretamente no DF de teste
        # Paciente 1 (IMC ~22) -> 0; Paciente 2 (IMC ~34) -> 1
        self.assertEqual(self.df.loc[1, 'overweight'], 1)
        self.assertEqual(self.df.loc[0, 'overweight'], 0)

    def test_normalization(self):
        # Testa se a normalização (1s viram 0s, >1s viram 1s) funciona
        # Paciente 1: Colesterol 1 (original), Glicose 1 (original)
        # Após normalização, ambos devem ser 0
        self.assertEqual(self.df.loc[0, 'cholesterol'], 0)
        self.assertEqual(self.df.loc[0, 'gluc'], 0)

    def test_data_cleaning_inconsistent_bp(self):
        # O DF de teste tem 10 linhas. A limpeza baseada em percentis não deve remover nenhuma linha nesse DF pequeno.
        self.assertEqual(len(self.df), 10)
        
        # Testando uma linha que deveria ser mantida com base na BP (Linha 2 original: 140/90)
        self.assertTrue(self.df.loc[1, 'ap_hi'] >= self.df.loc[1, 'ap_lo'])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
