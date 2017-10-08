# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 18:33:17 2017

@author: dacrands
"""

import pandas as pd
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True

scal_url = "https://www.basketball-reference.com/players/s/scalabr01.html"
scal_dframe = pd.read_html(scal_url)
scal_dframe = scal_dframe[0]
scal_dframe = scal_dframe[['AST','PTS','TRB','Age']]

shaq_url="https://www.basketball-reference.com/players/o/onealsh01.html"
shaq_dframe = pd.read_html(shaq_url)
shaq_dframe = shaq_dframe[0]
shaq_dframe = shaq_dframe[['AST','PTS','TRB','Age']]

td_url="https://www.basketball-reference.com/players/d/duncati01.html"
td_dframe = pd.io.html.read_html(td_url)
td_dframe = td_dframe[0]
td_dframe = td_dframe[['AST','PTS','TRB','Age']]

kg_url="https://www.basketball-reference.com/players/g/garneke01.html"
kg_dframe = pd.io.html.read_html(kg_url)
kg_dframe = kg_dframe[0]
kg_dframe = kg_dframe[['AST','PTS','TRB','Age']]

ka_url="https://www.basketball-reference.com/players/a/abdulka01.html"
ka_dframe = pd.io.html.read_html(ka_url)
ka_dframe = ka_dframe[0]
ka_dframe = ka_dframe[['AST','PTS','TRB','Age']]

shaq_dframe['player'] = pd.Series(['SO' for i in range(len(shaq_dframe))])
td_dframe['player'] = pd.Series(['TD' for i in range(len(td_dframe))])
kg_dframe['player'] = pd.Series(['KG' for i in range(len(kg_dframe))])
ka_dframe['player'] = pd.Series(['KA' for i in range(len(ka_dframe))])

new_frame = pd.concat([shaq_dframe,td_dframe,kg_dframe,ka_dframe])
