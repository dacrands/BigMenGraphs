# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:36:28 2017

@author: dacrands
"""
import seaborn as sb
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['patch.force_edgecolor'] = True

from basketball_ref_data import main_frame


plt.rcParams['axes.facecolor'] = '#212223'

line_colors = ["#60d2d6", "#3c2cb2", "#ea5900", "#bc1818", 
               "white", "#fcee2a", "#42c436"]

player_names = ["Shaquille O'Neal", "Tim Duncan", "Kevin Garnett", 
                "Kareem Abdul-Jabbar", "Hakeem Olajuwon", 
                "Charles Barkley", "Karl Malone"]

big_line = sb.lmplot(x="PTS", y="TRB", data=main_frame, legend=False, 
                     hue="player", size=8, aspect=1.3, palette=line_colors)            

big_line.set(ylim=(0,20))
big_line.set(ylabel='Boards')
big_line.set(xlabel='Points')

sb.set(font_scale = 1.6)
sb.despine(left=True, bottom=True)


plt.title("The Big Men", fontsize=32, fontweight='bold')

legend = plt.legend(bbox_to_anchor=(.01, .98), loc='upper left', 
                  ncol=2, fontsize=14, frameon=True, shadow=True,
                  labels=player_names)

sb.set_style("darkgrid")
plt.show()

big_line.savefig("graphs/big_line_graph.png")
