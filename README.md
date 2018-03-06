# Image to Text Converter-OCR  (python 3.x)
The attached code is a simple code which will convert Image into text using tesseract and google vision api.

# Tesseract OCR
Tesseract is an optical chrarecter recognition library used in python but its efficiency is very low compared with google vision api but we can increase contrast or create binary image using opencv to enhance the output.
to install tesseract:-
  https://www.linux.com/blog/using-tesseract-ubuntu
  
 In the given code i have applied binary image convertion to get better output
Required libraries
  OPEN CV
  TESSERACT OCR
  numpy
  
# GOOGLE VISION API
This is the most advanced api availible for optical charecter recognition and it offers other services like face recognition,  logo, and landmark detection, etc. 
https://console.cloud.google.com/apis/api/speech.googleapis.com/overview?project=blind-guidance&duration=PT1H
HOW TO USE IT:-
  1. Create a project in google console and add vision api to it.
  2. In this project go to credentials and create Service account keys
  3. Download Service account keys in .json format 
  4. Give its path in code.
  5. RUN
