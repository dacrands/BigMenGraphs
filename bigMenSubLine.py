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
plt.rcParams["axes.labelsize"] = 14

big_line = sb.lmplot(
        data=new_frame,
        x="PTS",
        y="TRB",
        hue="player",
        col="player",
        size=3.5,
        aspect=1.2,
        col_wrap=3,
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
sb.set(font_scale = 1.6)

sb.despine(left=True, bottom=True)

ax = big_line
ax.add_legend(title="legend", 
              labels=["Shaquille O'Neal",
                      "Tim Duncan",
                      "Kevin Garnett",
                      "Kareem Abdul-Jabbar",
                      "Hakeem Olajuwon",
                      "Charles Barkley",
                      "Karl Malone"
                      ]
              )
#ax.legend(
#          bbox_to_anchor=(.9, .98), 
#          ncol=1,
#          fontsize=14,
#          frameon=True,
#          shadow=True,
#          labels=["Shaquille O'Neal",
#                  "Tim Duncan",
#                  "Kevin Garnett",
#                  "Kareem Abdul-Jabbar",
#                  "Hakeem Olajuwon",
#                  "Charles Barkley",
#                  "Karl Malone"
#                  ]
#          )

#frame = legend.get_frame()

sb.set_style("darkgrid")
plt.show()

big_line.savefig("graphs/big_line_graph.png")