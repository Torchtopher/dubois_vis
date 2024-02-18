# making data visualizations in the style of w.e.b. du bois
# color palette from https://www.dignityanddebt.org/projects/du-boisian-resources/
# https://nightingaledvs.com/the-dubois-challenge/
# data from https://github.com/ajstarks/dubois-data-portraits/tree/master/challenge/2024

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as font_manager

BLACK = '#000000'
BROWN = '#654321'
TAN = '#D2B48C'
GOLD = '#FFD700'
PINK = '#FFC0CB'
RED = '#DC143C'
GREEN = '#00AA00'
PURPLE = '#7e6583'
BLUE = '#4682b4'

# FEEDBACK, use dubois font for titles

font_path = '/usr/share/fonts/dubois/VTCDuBoisTrial-BoldNarrow.ttf'  # Your font path goes here
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = prop.get_name()
# make title font bigger
plt.rcParams['axes.titlesize'] = 20

# load data
df = pd.read_csv('/home/chris/code/amstud_dubois/src/slave_pop.csv')
original = pd.read_csv('/home/chris/code/amstud_dubois/src/slave_pop.csv')

# clamp both slave and free to 3 % to make the chart more readable (and like the original)
df['Slave'] = df['Slave'].clip(upper=3)
df['Free'] = df['Free'].clip(upper=3)


print(df)
# make a stacked bar chart
fig, ax = plt.subplots()

# make year a bar on the Y axis instead of the X axis
ax.barh(df['Year'], df['Slave'], color=RED, label='Free', height=10.0)
ax.barh(df['Year'], df['Free']-df["Slave"], color=BLACK, left=df['Slave'], label='Slave', height=10.0)
# invert the Y axis
ax.invert_yaxis()

# change background color to tan
ax.set_facecolor(TAN)

fig.patch.set_facecolor(TAN)

ax.set_title('Slave and Free Negros')

ax.set_ylabel('Year')
# move the legend out of the way
ax.legend(loc='upper left')
# invert the legend so that red is free

# add a right side y axis label with the actual percentage
ax2 = ax.twinx()
# make a tick mark for each bar even though the data is not evenly spaced
ax2.set_yticks(df['Year'])
# change spacing to make it spead out
ax2.set_ylim(ax.get_ylim())
# now set the labels to the actual percentage
ax2.set_yticklabels(original['Free'].astype(float))
ax2.set_ylabel('Percent of Free Negros')

# flip the x axis so that 3 percent is on the right
ax.invert_xaxis()
# move the x axis to the top
ax.xaxis.tick_top()
# make font bigger
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
# set background color to tan


# save image to png
plt.savefig("test.png", pad_inches=1)

plt.show()
