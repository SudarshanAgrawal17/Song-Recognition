import speech_recognition as sr
import filecmp
import pandas as pd
import csv

#inializing recognizer 
r = sr.Recognizer()
#give only wav format file 
audio_file = sr.AudioFile('vocals/test/vocals.wav')
#converting audio file record file
with audio_file as source:
    audio_text = r.record(source)
#with google voice we will convert audio to text
lyrics = r.recognize_google(audio_text)
with open('readme.txt', 'x') as f:
    f.write(lyrics)

with open('dataset/tcc_ceds_music.csv','r') as file:
    csv_file = csv.reader(file)
    flag = True
    for row in csv_file:
        if lyrics in row[3]:
            print("Song Found: "+row[1]+" - "+row[0])
            flag = False
            break
    if flag:
        print("Song Not Found!")