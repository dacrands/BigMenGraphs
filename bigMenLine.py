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
plt.rcParams['axes.titlepad'] = 25
plt.rcParams["axes.labelpad"] = 10
plt.rcParams["axes.labelsize"] = 20

big_line = sb.lmplot(
        data=new_frame,
        legend=False,
        x="PTS",
        y="TRB",
        hue="player",
        size=8,
        aspect=1.3,
        palette = [
                "#60d2d6",
                "#3c2cb2",
                "#ea5900",
                "#bc1818",
                "white",
                "#fcee2a",
                "#42c436"
                ]
        )            

big_line.set(ylim=(0,20))
big_line.set(ylabel='Boards')
big_line.set(xlabel='Points')
sb.set(font_scale = 1.6)

plt.title("The Big Men", fontsize=32, fontweight='bold')

sb.despine(left=True, bottom=True)

legend = plt.legend(
                  bbox_to_anchor=(.01, .98),
                  loc='upper left', 
                  ncol=2,
                  fontsize=14,
                  frameon=True,
                  shadow=True,
                  labels=["Shaquille O'Neal",
                          "Tim Duncan",
                          "Kevin Garnett",
                          "Kareem Abdul-Jabbar",
                          "Hakeem Olajuwon",
                          "Charles Barkley",
                          "Karl Malone"
                          ]
                  )

frame = legend.get_frame()

sb.set_style("darkgrid")
plt.show()

big_line.savefig("graphs/big_line_graph.png")