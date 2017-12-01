# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:40:23 2017

@author: dacrands
"""

import seaborn as sb
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
import matplotlib.pyplot as plt

from basketball_ref_data import main_frame


plt.rcParams['axes.titlepad'] = 10
plt.rcParams["axes.labelpad"] = 10  
            
big_honeycomb_graph = sb.jointplot("Age", "PTS", data=main_frame, kind='hex', 
                                  size=10, color='#0ba584', alpha=.8
                                  ).plot_joint(sb.regplot, fit_reg=False, color='#7c4bbc')

sb.set_style("white")
plt.xlabel('Age',fontweight='bold')
plt.ylabel('Points',fontweight='bold')
plt.text(22.0, 5.0, "Sample Size = {}".format(len(main_frame)))
plt.suptitle("Points as a function of Age", y=1.01, x=.45,
             fontsize=24, fontweight='heavy')

big_honeycomb_graph.savefig(r"graphs/big_honeycomb_graph.png")
