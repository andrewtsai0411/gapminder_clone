import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

connection = sqlite3.connect('data/gapminder.db')
plotting_df = pd.read_sql('SELECT * FROM plotting;', con=connection)
connection.close()
# print(plotting_df.shape)


connection = sqlite3.connect('data/gapminder.db')
plotting_df = pd.read_sql('SELECT * FROM plotting;', con=connection)
connection.close()
# print(plotting_df.shape)

plt.style.use('seaborn-v0_8')

'''
year_to_plot = 2023
subset_df = plotting_df[plotting_df['dt_year'] == year_to_plot]
lex = subset_df['life_expectancy'].values
gdp_pcap = subset_df['gdp_per_capita'].values
cont = subset_df['continent'].values
# print(plotting_df['continent'].unique())
color_map = {'africa': '#C0FFB3', 'americas': '#FFDA99', 'asia': '#9ECCFE', 'europe': '#FA9DE3'}
    # africa:green, americas:yellow, asia:blue, europe:pink
for xi, yi,ci in zip(gdp_pcap, lex, cont):
    ax.scatter(x=xi, y=yi,color=color_map[ci]) # label=ci ?
ax.set_title(f'The world in {2020}')
ax.set_xlabel('GDP Per Capita(in USD)')
ax.set_ylabel('Life Expectancy')
ax.set_xlim(0, 100000)
ax.set_ylim(20, 100)
# plt.legend()
plt.show()
'''


fig, ax = plt.subplots()
def update_plot(year_to_plot: int):
    ax.clear()
    subset_df = plotting_df[plotting_df['dt_year'] == year_to_plot]
    lex = subset_df['life_expectancy'].values
    gdp_pcap = subset_df['gdp_per_capita'].values
    cont = subset_df['continent'].values
    # print(subset_df['continent'].unique())
    color_map = {'africa': '#C0FFB3', 'americas': '#FFDA99', 'asia': '#9ECCFE', 'europe': '#FA9DE3'}
    # africa:green, americas:yellow, asia:blue, europe:pink
    for xi, yi, ci,in zip(gdp_pcap, lex, cont):
        ax.scatter(x=xi, y=yi, color=color_map[ci])
    ax.set_title(f'The world in {year_to_plot}')
    ax.set_xlabel('GDP Per Capita(in USD)')
    ax.set_ylabel('Life Expectancy')
    ax.set_xlim(0, 100000)
    ax.set_ylim(20, 100)
    plt.tight_layout()
ani = animation.FuncAnimation(fig, func=update_plot,frames=range(2000,2024),interval=10)
ani.save('animation.gif',fps=10)
