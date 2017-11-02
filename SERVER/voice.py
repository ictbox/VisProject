__author__ = 'hpp'
import random
import json
import dataBaseApi as db
import numpy as np

class VoiceMeasure(object):
    def __init__(self):
        self.m_topicNumber = 10     # 10 topic
        self.m_dateNumber =72       # 72 day
        self.features=[]
        self.articleTopic=[]
        self.getArticleTopic()
        self.getFeatures()

    def getRandomVoice(self):
        '''
        :return:return random Voice in (0,100) in json for test
        '''
        voiceData = {}
        for i in range(self.m_topicNumber):
            topicVoice = []
            for j in range(self.m_dateNumber):
                topicVoice.append(random.uniform(0,100))
            topicName = 'topic' + str(i)
            voiceData[topicName]=topicVoice
        voiceDataJson = json.dumps(voiceData,sort_keys= True)
        return voiceDataJson
    def getFeatures(self):
        '''
        ret features
        :return:
        '''
        self.features=db.getRandomfeatures()

    def getArticleTopic(self):
        self.articleTopic = db.getRandomArticlesTopic()

    def computeVoiceWithFeatures(self,VoiceParameter):



        voiceData = {}


        for i in range(self.m_topicNumber):
            topicName = 'topic' + str(i)
            voiceData[topicName] = []


        for i in range (len(self.features)):
            dayVoice = np.matmul(self.features[i],np.mat(VoiceParameter).T)#dayVoice Nx9 *9x1 =N * 1

            dayTopicVoice = np.matmul(np.mat(self.articleTopic[i]).T,dayVoice).tolist()

            for j in range(self.m_topicNumber):
                topicName = 'topic' + str(j)
                voiceData[topicName].append(dayTopicVoice[j])

        voiceDataJson = json.dumps(voiceData,sort_keys=True)


        return voiceDataJson





