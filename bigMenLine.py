# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:36:28 2017

@author: dacrands
"""
import seaborn as sb
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
import matplotlib.pyplot as plt

from bigMenData import new_frame

"""
Graphs
"""
plt.rcParams['axes.facecolor'] = '#212223'
big_line_graph = sb.lmplot(
                 data=new_frame,
                 legend=False,
                 x="PTS", 
                 y="TRB",
                 hue="player", 
                 size=8, 
                 aspect=1.3,
                 palette=["#9b59b6", "#3498db", "#edb349", "#e74c3c"]
                 )

sb.set(font_scale = 1.6)
plt.ylabel('Boards')
plt.xlabel('Points')
plt.rcParams['axes.titlepad'] = 25
plt.rcParams["axes.labelpad"] = 10
plt.rcParams["axes.labelsize"] = 20
plt.title("The Big Men",
          fontsize=32,
          fontweight='bold'
          )

sb.despine(left=True, bottom=True)

legend = plt.legend(bbox_to_anchor=(.01, .98),
                  loc='upper left', 
                  ncol=1,
                  fontsize=14,
                  frameon=True,
                  shadow=True,
                  labels=["Shaquille O'Neal",
                          "Tim Duncan",
                          "Kevin Garnett",
                          "Kareem Abdul-Jabbar"
                          ])
frame = legend.get_frame()

sb.set_style("darkgrid")

big_line_graph.savefig("graphs/big_line_graph.png")
