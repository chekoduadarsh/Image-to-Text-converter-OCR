
import json
import requests
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types



def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print(texts)
    print('Texts:')

    for text in texts:
        a=("{}".format(text.description))
        print(a)
        #vertices = (['({},{})'.format(vertex.x, vertex.y)
        #            for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))'''
    print((a))
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '' #give path to your Service account keys .json file
bq_client = Client()
path=''    					  #give path to your image
detect_text(path)
