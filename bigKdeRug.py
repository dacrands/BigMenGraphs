# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:54:29 2017

@author: dacrands
"""
import seaborn as sb
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
import matplotlib.pyplot as plt

from bigMenData import new_frame

f, ax = plt.subplots(figsize=(10, 10))
cmap = sb.cubehelix_palette(
                            as_cmap=True, 
                            dark=0, 
                            light=1,
                            rot=.05,
                            reverse=True
                            )
sb.kdeplot(new_frame['TRB'], 
           new_frame['PTS'], 
           ax=ax,
           shade=True,
           cmap=cmap,
           n_levels=60
                           )
sb.rugplot(new_frame['TRB'], color="gray", ax=ax)
sb.rugplot(new_frame['PTS'],color='#763e8e', vertical=True, ax=ax)
plt.suptitle("Points by Boards",
             fontsize=28,
             color="lightgray",
             y=0.85,
             x=0.5,
             )

f.savefig("graphs/big_kde_rug_graph.png")