import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from watson_developer_cloud import ToneAnalyzerV3
import webScrape

api_key_alc='1983387b2fb355dca6bc2cf73437d3e4bbfa6dbf'
toneUser = '7dd29476-b1e0-4c5a-a68c-a16e72969667'
tonePass = 'ZsytNE1fO65f'

def analyze(url):
    alchemy_language = AlchemyLanguageV1(api_key=api_key_alc)
    combined_operations = [ 'entity', 'keyword', 'title', 'concept', 'doc-emotion']
    global data
    data = alchemy_language.combined(url=url, extract=combined_operations)
    tone_analyzer = ToneAnalyzerV3(username=toneUser,password=tonePass,version='2016-05-19')
    global tone
    tone = tone_analyzer.tone(text=webScrape.getText(url))

def getTitle():
    global data
    title = data['title']
    return title.encode('ascii','ignore')

def getKeywords():
    global data
    return data['keywords']    

def getKeyKeywords():
    words = []
    global data
    for i in range(0,7):
        words.append(data['keywords'][i]['text'])
    return words
    
def getEmotions():
    global data
    emotions= data['docEmotions']
    return emotions

def getTone():
    global tone
    return tone


