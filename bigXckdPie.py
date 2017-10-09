# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:12:31 2017

@author: dacrands
"""
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
import matplotlib.pyplot as plt

from bigMenData import shaq_dframe, td_dframe, kg_dframe, ka_dframe, ho_dframe, \
                        cb_dframe, km_dframe
        

point_means= [
    round(shaq_dframe['PTS'].mean(),2),
    round(td_dframe['PTS'].mean(),2),
    round(kg_dframe['PTS'].mean(),2),
    round(ka_dframe['PTS'].mean(),2),
    round(ho_dframe['PTS'].mean(),2),     
    round(cb_dframe['PTS'].mean(),2),    
    round(km_dframe['PTS'].mean(),2)     
]

boards_means= [
    round(shaq_dframe['TRB'].mean(),2),
    round(td_dframe['TRB'].mean(),2),
    round(kg_dframe['TRB'].mean(),2),
    round(ka_dframe['TRB'].mean(),2),
    round(ho_dframe['PTS'].mean(),2),     
    round(cb_dframe['PTS'].mean(),2),    
    round(km_dframe['PTS'].mean(),2)  
]

labels = ["Shaquille O'Neal",
          "Tim Duncan",
          "Kevin Garnett",
          "Kareem Abdul-Jabbar",
          "Hakeem Olajuwon",
          "Charles Barkley",
          "Karl Malone"
          ]


#POINTS GRAPH
big_men_pie_points = plt.figure()
plt.xkcd()
mpl.rcParams['font.sans-serif'] = "Comic Sans MS"
mpl.rcParams['font.size'] = 12
colors = [
          'yellowgreen', 
          'gold', 
          'lightskyblue', 
          'lightcoral',
          'darkgray',
          'blue',
          'red'
]

plt.pie(point_means,
        explode=(0, 0, 0, 0, 0, 0, 0.1),
        colors=colors,
        autopct='%1.1f%%', 
        shadow=True, 
        startangle=90
        )

plt.suptitle("Average Points Per Season",
             fontsize=18,
             y=0.9,
             x=0.5
             )

legend = plt.legend(bbox_to_anchor=(0.05,0.08),
                  loc='upper left', 
                  ncol=2,
                  fontsize=10,
                  frameon=True,
                  shadow=True,
                  labels=labels)

#BOARDS GRAPH
big_men_pie_boards = plt.figure()
colors_boards = ['#6ED294', #greenish
                 '#c9a360', #orangish
                 '#5587a0', #bluish
                 '#9b6e9a', #grayish
                 'darkgray',
                 'blue',
                 'red'
]

plt.pie(boards_means, 
        colors=colors_boards,
        explode=(0, 0, 0, 0, 0, 0, 0.1),       
        autopct='%1.0f%%', 
        shadow=True, 
        startangle=90
        )

plt.suptitle("% Boards relative to peers",
             fontsize=18,
             y=0.9,
             x=0.5
             )

legend2 = plt.legend(bbox_to_anchor=(0.05,0.08),
                  loc='upper left', 
                  ncol=2,
                  fontsize=11,
                  frameon=True,
                  shadow=True,
                  labels=labels)



big_men_pie_points.savefig("graphs/big_xkcd_pie_points.png", bbox_extra_artists=(legend,), bbox_inches='tight')
big_men_pie_boards.savefig("graphs/big_xkcd_pie_boards.png", bbox_extra_artists=(legend2,), bbox_inches='tight')