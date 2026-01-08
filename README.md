# Medical Data Visualizer (Visualizador de Dados Médicos)

## Sobre
Este é um projeto desenvolvido como parte do curso "Data Analysis with Python" da [freeCodeCamp](www.freecodecamp.org).

O projeto foi aprimorado com a capacidade de gerar dados fictícios para testes 
e inclui testes de unidade robustos usando a biblioteca `unittest` do Python.



## Estrutura

*   **Geração de Dados de Mockup:** Script para criar `mockup_medical_data.csv`.
*   **Testes de Unidade:** Verificação da lógica de pré-processamento e limpeza de dados.
*   **Pré-processamento de Dados:** Cálculo de IMC, normalização de valores e filtragem de outliers.
*   **Gráfico Categórico (Cat Plot):** Visualiza a contagem de características por condição cardiovascular.
*   **Mapa de Calor (Heat Map):** Mostra a matriz de correlação entre todas as variáveis médicas.

  

## Instrução

1.  Clone este repositório:
    ```bash
    git clone github.com
    ```
2.  Navegue até o diretório do projeto:
    ```bash
    cd medical-data-visualizer
    ```
3.  Instale as bibliotecas necessárias: pandas, matplotlib, seaborn, numpy:
    ```bash
    pip install pandas matplotlib seaborn numpy
    ```
4.  **Opcional:** Gere um novo arquivo de dados de mockup:
    ```bash
    python3 generate_mockup_data.py
    ```
5.  Execute o arquivo `main.py` para rodar a análise e gerar os gráficos (ele usa `medical_examination.csv` por padrão):
    ```bash
    python3 main.py
    ```
6.  Execute os testes de unidade:
    ```bash
    python3 run_tests.py
    ```

## Arquivos no Projeto

*   `medical_data_visualizer.py`: Contém as funções `draw_cat_plot()` e `draw_heat_map()`.
*   `main.py`: Arquivo de exemplo para testar as funções e salvar as imagens geradas.
*   `generate_mockup_data.py`: Script para criar dados de mockup.
*   `run_tests.py`: Script para executar os testes de unidade personalizados.
*   `medical_examination.csv`: O conjunto de dados original utilizado na análise.


## Licença e Créditos

Licença MIT. Disponível para modificação e distribuição livre, desde que atribua os créditos ao autor original.

## Autor
- **GitHub:** [trsilva23]
- **E-mail:** [trsilva23.contato@gmail.com] 

