import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='f11faf136164665418a93df1b6037bc4e5c4cc7e')

print (json.dumps(visual_recognition.classify(images_url="https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg"),indent=2))