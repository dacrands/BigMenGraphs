# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:54:29 2017

@author: dacrands
"""
import seaborn as sb
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
mpl.rcParams['text.color'] = 'blue'        
import matplotlib.pyplot as plt

from basketball_ref_data import main_frame

f, ax = plt.subplots(figsize=(10, 10))

cmap = sb.cubehelix_palette(as_cmap=True, dark=0, light=1,
                            rot=.05, reverse=True)

sb.kdeplot(main_frame['TRB'], main_frame['PTS'], ax=ax, 
           shade=True, cmap=cmap, n_levels=60)

sb.rugplot(main_frame['TRB'], color="gray", ax=ax)
sb.rugplot(main_frame['PTS'], color='#763e8e', vertical=True, ax=ax)

ax.set_title("Points by Boards", y=1.02, x=0.5, 
             fontsize=28, family='monospace', color="lightgray")

ax.tick_params(pad=10, labelsize='large', colors='lightgray')
ax.set_xlabel("Rebounds per Game", fontsize=20, family='monospace', color='lightgray')
ax.set_ylabel("Points per Game", fontsize=20, family='monospace', color='lightgray')

plt.text(4.0, 36.0, "n = {} seasons".format(len(main_frame)), 
         fontstyle='italic', family='serif', color="white", fontsize=12)

f.savefig("graphs/big_kde_rug_graph.png", facecolor='k', bbox_inches='tight')
