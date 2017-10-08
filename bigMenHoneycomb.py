# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:40:23 2017

@author: dacrands
"""

import seaborn as sb
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
import matplotlib.pyplot as plt

from bigMenData import new_frame


big_honeycomb_graph = sb.jointplot(
                                  "Age", 
                                  "PTS", 
                                  data=new_frame, 
                                  kind ='hex',
                                  size=10,
                                  color='#0ba584', 
                                  alpha=.8
                                  ).plot_joint(
                                               sb.regplot, 
                                               fit_reg=False, 
                                               color='#7c4bbc'
                                              )

plt.rcParams['axes.titlepad'] = 10
plt.rcParams["axes.labelpad"] = 10  
sb.set_style("white")
plt.suptitle("Points as a function of Age",
             fontsize=24,
             y=1.01,
             x=.45,
             fontweight='heavy')
plt.xlabel('Age',fontweight='bold')
plt.ylabel('Points',fontweight='bold')

big_honeycomb_graph.savefig(r"graphs/big_honeycomb_graph.png")