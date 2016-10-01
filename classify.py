import json
import requests
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='f11faf136164665418a93df1b6037bc4e5c4cc7e')

with open(join(dirname(__file__), './winter_test.jpg'), 'rb') as image_file:
 print (json.dumps(visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639']), indent=2))
# payload={'classifier_ids':'Summer_Winter_1816597639','images_file' : 'ross2.png'}
# r = requests.post("https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key=f11faf136164665418a93df1b6037bc4e5c4cc7e&version=2016-05-20",json=payload)
# print (json.dumps(visual_recognition.classify(images_url= "mn-dresses/1151-summer-clothes-for-women.jpg"), indent=2))

# print r.json()