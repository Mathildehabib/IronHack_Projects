# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:33:01 2019

@author: mathi
"""

import pandas as pd
import webbrowser
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import paired_cosine_distances as pcd
import time as t

yoox=pd.read_csv(r'C:\Users\mathi\Documents\GitHub\Data-sets\Final_Project\yoox_final.csv').drop('Unnamed: 0',axis=1)
yoox.drop_duplicates(keep='first',inplace=True)
t.sleep(1)
g=input(f"Choose a Product\nHere is a suggestion{str(yoox.sample()['item'].unique())}\n")
t.sleep(1)
i_d0=yoox[yoox.item==g].index
webbrowser.open(f'http://yoox.com/fr/{g}/item')
t.sleep(8)

yoox_ml = yoox.drop(["brand", "url","price_actual","discount_rate",'compositions','item'], axis=1)
yoox_ml[[ '_Blouses', '_Bodycon Dress', '_Bomber Jackets', '_Cardigans', '_Coats', '_Culottes', '_Denim Pants', '_Down-coat',
 '_Hoodies', '_Jackets', '_Jumpers', '_Jumpsuits', '_Knee Length Skirt', '_Long Coats', '_Maxi Dress', '_Maxi Skirt',
         '_Midi Dress', '_Midi Skirt', '_Mini Dress', '_Mini Skirt', '_One piece Swimsuit', '_Pyjamas', '_Shirts',
 '_Shorts', '_T-shirts', '_Tops', '_Trench Coats', '_Trousers', '_Turtle Necks']]=yoox_ml[[ '_Blouses', '_Bodycon Dress', '_Bomber Jackets', '_Cardigans', '_Coats', '_Culottes', '_Denim Pants', '_Down-coat',
 '_Hoodies', '_Jackets', '_Jumpers', '_Jumpsuits', '_Knee Length Skirt', '_Long Coats', '_Maxi Dress', '_Maxi Skirt',
         '_Midi Dress', '_Midi Skirt', '_Mini Dress', '_Mini Skirt', '_One piece Swimsuit', '_Pyjamas', '_Shirts',
 '_Shorts', '_T-shirts', '_Tops', '_Trench Coats', '_Trousers', '_Turtle Necks']].apply(lambda x: x*1.6)

yoox_ml[[  'size_30','size_32', 'size_34', 'size_36', 'size_38', 'size_40', 'size_42', 'size_44', 'size_46', 'size_48']]=yoox_ml[[  'size_30',
 'size_32', 'size_34', 'size_36', 'size_38', 'size_40', 'size_42', 'size_44', 'size_46', 'size_48']].apply(lambda x: x*0.8)

yoox_ml[['colors_Anthracite', 'colors_Argent', 'colors_Aubergine', 'colors_Beige', 'colors_Blanc', 'colors_Bleu', 'colors_Bleu ciel',
 "colors_Bleu d'azur", 'colors_Bleu foncé', 'colors_Bleu pétrole', 'colors_Bleu électrique', 'colors_Bleu-gris', 'colors_Bordeaux',
 'colors_Brique', 'colors_Camel', 'colors_Chair', 'colors_Chocolat', 'colors_Corail', 'colors_Cuivre', 'colors_Fuchsia',
 'colors_Gris', 'colors_Gris clair', 'colors_Gris tourterelle', 'colors_Ivoire', 'colors_Jaune', 'colors_Jaune clair', 'colors_Kaki',
 'colors_Marron', 'colors_Mauve', 'colors_Moka', 'colors_Noir', 'colors_Noisette', 'colors_Ocre', 'colors_Or', 'colors_Orange',
 'colors_Platine', 'colors_Plomb', 'colors_Pourpre', 'colors_Rose', 'colors_Rose clair', 'colors_Rouge', 'colors_Rouille',
 'colors_Sable', 'colors_Saumon', 'colors_Turquoise', 'colors_Vert', 'colors_Vert acide', 'colors_Vert clair', 'colors_Vert foncé',
 'colors_Vert militaire', 'colors_Vert pétrole', 'colors_Vert émeraude', 'colors_Vieux rose', 'colors_Violet', 'colors_Violet clair',
 'colors_Violet foncé']]=yoox_ml[['colors_Anthracite', 'colors_Argent', 'colors_Aubergine', 'colors_Beige', 'colors_Blanc', 'colors_Bleu', 'colors_Bleu ciel',
 "colors_Bleu d'azur", 'colors_Bleu foncé', 'colors_Bleu pétrole', 'colors_Bleu électrique', 'colors_Bleu-gris', 'colors_Bordeaux',
 'colors_Brique', 'colors_Camel', 'colors_Chair', 'colors_Chocolat', 'colors_Corail', 'colors_Cuivre', 'colors_Fuchsia',
 'colors_Gris', 'colors_Gris clair', 'colors_Gris tourterelle', 'colors_Ivoire', 'colors_Jaune', 'colors_Jaune clair', 'colors_Kaki',
 'colors_Marron', 'colors_Mauve', 'colors_Moka', 'colors_Noir', 'colors_Noisette', 'colors_Ocre', 'colors_Or', 'colors_Orange',
 'colors_Platine', 'colors_Plomb', 'colors_Pourpre', 'colors_Rose', 'colors_Rose clair', 'colors_Rouge', 'colors_Rouille',
 'colors_Sable', 'colors_Saumon', 'colors_Turquoise', 'colors_Vert', 'colors_Vert acide', 'colors_Vert clair', 'colors_Vert foncé',
 'colors_Vert militaire', 'colors_Vert pétrole', 'colors_Vert émeraude', 'colors_Vieux rose', 'colors_Violet', 'colors_Violet clair',
 'colors_Violet foncé']].apply(lambda x: x*1.3)

pca=PCA(0.99)
pca.fit(yoox_ml)
pca.n_components_

yoox_ml_new=pca.transform(yoox_ml)

cosine = [1 - pcd(yoox_ml_new[i_d0].reshape(-1, 1).T, i.reshape(-1, 1).T) for i in yoox_ml_new]
results=cosine.copy()
results.sort(reverse=True)
results=[i for i in results if i > 0.78]
indices = [i for i, x in enumerate(cosine) if x in results[1:]]
urls=[]
for i in indices:
    urls.append(yoox.url[i])
new_urls=yoox[(yoox['url'].isin(urls))==True].sort_values(by='price_actual')['url'].drop_duplicates(keep='first').head(4).tolist()
for i in new_urls:
    webbrowser.open(i)
