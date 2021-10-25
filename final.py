#!/usr/bin/env python
# coding: utf-8

#Reconnaissance Faciale
#Chargement des librairies nécessaires

#Installation à faire au préalable : 
#pip install face_recognition
#pip install opencv-python
#charger le fichier : haarcascade_frontalface_default.xml de Open CV

import face_recognition
import cv2
import numpy as np
import os
import glob
import operator

#Chargement du modèle pour détection de visage
faceCascade = cv2.CascadeClassifier('C:/Users/belka/Documents/IOT_PROJECT_DATA/haarcascade_frontalface_default.xml')

from cv2 import *

#Prendre les photos des personnes qui doivent être connues du système (mettre vos propres photos)

faces_encodings = []
faces_names = []
list_of_files = ['C://Users/belka/data/faces/Lina-Belkarfa.jpg']
names = list_of_files.copy()
number_files = len(list_of_files)
cur_direc = 'C://Users/belka/data/faces/'

#Chercher les visages dans les photos 

print('Detection et apprentissage des visages de la Base de données...')
print(str(number_files)+' photos à analyser :')
for i in range(number_files):

    globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
    
    if not(face_recognition.face_encodings(globals()['image_{}'.format(i)])):
        print('Pas de visage detecté!')
        names[i] = names[i].replace(cur_direc, "No detected ")  

    else:
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
        faces_encodings.append(globals()['image_encoding_{}'.format(i)])

        names[i] = names[i].replace(cur_direc, "")  
        names[i] = names[i].replace(".jpg", "")  
        faces_names.append(names[i])
        print('Visage n°'+str(i+1)+ ' détecté!')
    

#Voir les noms des visages reconnus
# names

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

#Lancement du programme de reconnaissance faciale via la webcam du pc : 

video_capture = cv2.VideoCapture(0)

detection=[]
nbInconnus=0
name=""

while True:
    ret, frame = video_capture.read()
    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
    rgb_small_frame = small_frame[:, :, ::-1]
    
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(faces_encodings, face_encoding)
            name = "Unknown"
            
            face_distances = face_recognition.face_distance(faces_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = faces_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame
    
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
    
    # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    # Input text label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    font                   = cv2.FONT_HERSHEY_SIMPLEX
    topLeftCornerOfText = (10,100)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2

    cv2.putText(frame,'Detection :', topLeftCornerOfText, font, fontScale,fontColor,lineType)
        
    index=100
    for i in names :
        if name == i :
            if name not in detection :
                detection.append(name)
                
    if name == str("Unknown"):
        nbInconnus=nbInconnus+1
        name = ""

            
    detec=""        
    for i in detection :
        index=index+50
        cv2.putText(frame,i, (10,index), font, fontScale,fontColor,lineType)        

    cv2.putText(frame,"Unknowns:"+str(nbInconnus), (10,450), font, fontScale,fontColor,lineType)
    
    # Display the resulting image
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()

