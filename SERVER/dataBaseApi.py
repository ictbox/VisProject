__author__ = 'hpp'
import numpy as np
def getRandomfeatures():
    '''
    get random features
    :return:
    '''
    features=[]
    for i in range(0,62):
        features.append(np.random.randint(0,100,size=[100,9]))
    return features

def getRandomArticlesTopic():
    '''
    get random article topic
    :return:
    '''
    ArticlesTopic =[]
    for  i in range(0,62):
        ArticlesTopic.append(np.random.random((100,10)))
    return  ArticlesTopic
