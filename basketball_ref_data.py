# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 12:17:52 2017

@author: dacrands
"""

import pandas as pd

player_dict = {"shaq_dframe" : "https://www.basketball-reference.com/players/o/onealsh01.html",
               "td_dframe" : "https://www.basketball-reference.com/players/d/duncati01.html",
               "kg_dframe" : "https://www.basketball-reference.com/players/g/garneke01.html",
               "ka_dframe" : "https://www.basketball-reference.com/players/a/abdulka01.html",
               "ho_dframe" : "https://www.basketball-reference.com/players/o/olajuha01.html",
               "cb_dframe" : "https://www.basketball-reference.com/players/b/barklch01.html",
               "km_dframe" : "https://www.basketball-reference.com/players/m/malonka01.html"}


dframes = dict()
for k, url in player_dict.items():
    dframes[k] = pd.read_html(url)[0][['AST','PTS','TRB','Age']]


initials = ['SO', 'TD', 'KG', 'KA', 'HO', 'CB', 'KM']
dframe_list = list()
i = 0
for k in dframes.keys():
    dframes[k]['player'] = pd.Series([initials[i] for n in range(len(dframes[k]))])
    dframe_list.append(dframes[k])
    i += 1


main_frame = pd.concat(dframe_list)
