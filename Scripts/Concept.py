
# coding: utf-8

# ### MBST
# 
# This functional module matches and recommends movies based on the similarity of plot. 
# First, using the coref_plot.csv, the plot of each movie is stored. 
# Then, using the IBM Watson NLU API, 8 most relevant concepts are found and stored. 
# Pre-trained word vector file provided by Google is downloaded and 
# the word vector corresponding to each of the concept for the movies is stored in a separate relation. 
# The word vectors of the original movie is compared with the word vectors of every other movie using cosine similarity. 
# The movies with the maximum simiarity is returned and is therefore recommended to the user.
# 
# ##### Input
# 
# Original Movie Name : moviename1
# 
# ##### Output
# 
# 'n' similar movies based on concept

# In[1]:


import numpy as np
import pandas as pd
from typing import List
import math


Vector = List[float]
def vector_len(v: Vector) -> float:
    return math.sqrt(sum([x*x for x in v]))

def dot_product(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2)
    return sum([x*y for (x,y) in zip(v1, v2)])

def cosine_similarity(v1: Vector, v2: Vector) -> float:
    """
    Returns the cosine of the angle between the two vectors.
    Results range from -1 (very different) to 1 (very similar).
    """
    if (vector_len(v1) != 0) and (vector_len(v2) != 0):
        
        return dot_product(v1, v2) / (vector_len(v1) * vector_len(v2))
    else:
        return 0




def replaceA(row):
    val = row['A'][1:-1]
    #print(len(val))
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val

def replaceB(row):
    val = row['B'][1:-1]
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val

def replaceC(row):
    val = row['C'][1:-1]
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val

def replaceD(row):
    val = row['D'][1:-1]
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val

def replaceE(row):
    val = row['E'][1:-1]
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val
def replaceF(row):
    val = row['F'][1:-1]
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val

def replaceG(row):
    val = row['G'][1:-1]
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val

def replaceH(row):
    val = row['H'][1:-1]
    z = val.split(', ')
    final_vec1 = []
    for i in z:
        if i != '':
            final_vec1.append(float(i))
            val = final_vec1
    return val


# In[6]:


def read_dataframe():
    df = pd.read_csv('../hugefile.csv')
    df = df.set_index('I')
    reqdcols = ['A','B','C','D','E','F','G','H']

    df['A'] = df.apply(replaceA, axis = 1)
    df['B'] = df.apply(replaceB, axis = 1)
    df['C'] = df.apply(replaceC, axis = 1)
    df['D'] = df.apply(replaceD, axis = 1)
    df['E'] = df.apply(replaceE, axis = 1)
    df['F'] = df.apply(replaceF, axis = 1)
    df['G'] = df.apply(replaceG, axis = 1)
    df['H'] = df.apply(replaceH, axis = 1)
    return df


# In[7]:


def retfunc(row, row1):
    vall = 0
    #print(len(row))
    #print(len(row1))
    for ind,r in enumerate(row1):
        cossim = [0,0,0,0,0,0,0,0]
        for jnd, s in enumerate(row):
            cossim[jnd] = cosine_similarity(r, s)
        vall = vall + np.max(cossim)

    return vall


# In[8]:


class concept():
    def __init__(self, moviename):
        self.moviename = moviename
        self.df = read_dataframe()
        self.row1 = self.df[self.df.index == moviename].squeeze().tolist()

    def similar_movies(self):
        datafr = pd.DataFrame(columns = ['Name', 'Value'])
        for i in self.df.iterrows():
            if i[0] == self.moviename:
                continue
            else:
                di = {}
                di['Name'] = i[0]
                cool = i[1].tolist()
                #print(cool)
                valueret = retfunc(cool, self.row1)
                di['Value'] = valueret    
                datafr = datafr.append(pd.Series(di), ignore_index = True)
        datafr = datafr.set_index('Name')
        return datafr.sort_values(by = ['Value'], ascending = False)[:5]


# In[9]:

moviename1 = input('Enter Movie')
x = concept(moviename1)
print(x.similar_movies())

