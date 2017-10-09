# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:43:13 2017

@author: dacrands
"""
import seaborn as sb
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
import matplotlib.pyplot as plt

from bigMenData import new_frame

plt.rcParams['axes.facecolor']='white'
big_jointplot = sb.jointplot(
                             "Age", 
                             "PTS", 
                             data=new_frame, 
                             kind ='kde',
                             size=10,
                             color='#4580e0', 
                             alpha=.8
                             ).plot_joint(
                                          sb.regplot, 
                                          fit_reg=False, 
                                          color='#c18617'
                                          )

plt.rcParams['axes.titlepad'] = 10
plt.rcParams["axes.labelpad"] = 10  
plt.suptitle("Points and Aging",fontsize=28,y=1.03,x=.24,rotation=30)
plt.text(36.0, 
         37, 
         "Sample Size = {}".format(len(new_frame)),
         fontsize=14
         )
plt.text(12.0, 
         .1, 
         """
         * Shaq, Karl Malone, Sir Charles, Tim Duncan, Kareem,
            Kevin Garnett         
         """,
         fontsize=10
         )

big_jointplot.savefig(r"graphs/big_jointplot.png")