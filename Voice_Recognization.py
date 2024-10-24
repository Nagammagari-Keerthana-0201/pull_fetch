import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import datetime
from PIL import Image, ImageTk

root=tk.Tk()
root.title('Voice Recognization')
root.geometry('400x400')
root.minsize(400,400)
root.configure(bg='#8FBC8F')

Title = tk.Label(root, text='Voice Note', font=('Cambria', 20,'bold'), bg='#0000FF',fg='#FFFFFF',padx=10)
Title.pack(pady=40)

Image_Path="C:/Users/N.Sai Keerthana/OneDrive/Desktop/voice.png"
O_Image=Image.open(Image_Path)
R_Image=O_Image.resize((50,50))
Image=ImageTk.PhotoImage(R_Image)

def listen():
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print(' Speak Something...')
            recognizer.adjust_for_ambient_noise(source)
            voice=recognizer.listen(source)
            try:
                h = recognizer.recognize_google(voice)
                save_voice(h)
                display_text(h)
                speak_text(h)
            except sr.UnknownValueError:
                print('Could not understand your voice')
            except sr.RequestError as e:
                print('Please Check the Internet Connection')
                
def save_voice(text):
    now = datetime.datetime.now()
    filename = f"VoiceNote_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)
    messagebox.showinfo("Voice Note Saved", f"Voice note saved as {filename}")

def speak_text(command):
            engine = pyttsx3.init()
            engine.say(command)
            engine.runAndWait()

def display_text(h):
        text = tk.Label(root, text=h, font=('Helvetica', 14), bg='#8FBC8F', fg='#000000')
        text.pack(pady=20)

Button=tk.Button(root,image=Image,bg='#B0BEC5', activebackground='#00E5FF',command=listen)
Button.pack(side='top',pady=30)


root.mainloop()
