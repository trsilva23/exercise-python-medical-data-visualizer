# main.py para testar as funções de visualização localmente
from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Gera o gráfico categórico e salva
fig_cat = draw_cat_plot()
fig_cat.savefig('catplot.png')
print("catplot.png salvo.")

# Gera o mapa de calor e salva
fig_heat = draw_heat_map()
fig_heat.savefig('heatmap.png')
print("heatmap.png salvo.")

#plt.show() 
