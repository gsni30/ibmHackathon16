import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='f11faf136164665418a93df1b6037bc4e5c4cc7e')

with open(join(dirname(__file__), 'summer.zip'), 'rb') as summer, \
      open(join(dirname(__file__), 'winter.zip'), 'rb') as winter:
   print (json.dumps(visual_recognition.create_classifier('Summer_Winter', summer_positive_examples=summer, negative_examples=winter), indent=2))