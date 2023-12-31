from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3
import threading
import speech_recognition


data_list=[ 
            'Hey,How are you',
            'I am good , what about you',
            'What do you know about python',
            'Python is a popular, user-friendly programming language that is widely used for web development, data science, artificial intelligence, scientific computing, and more.',
            'Make a basic Hello world program in python',
            'okey, the basic hello world program is (print ("hello world"))',
            'What you do in free time',
            'I memorize things in my free time',
            'Ok bye',
            'bye take care'

            ]

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

# for files in os.listdir('data/french/'):
#     data=open('data/french/'+files,'r',encoding='utf-8').readlines()

trainer.train(data_list)

def botReply():
    question=questionField.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Bot: '+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0,END)
    
def audioTotext():
        while True:
            sr=speech_recognition.Recognizer()        
            try:
                with speech_recognition.Microphone()as m:
                    sr.adjust_for_ambient_noise(m,duration=0.2)
                    audio=sr.listen(m)
                    query=sr.recognize_google(audio)
            
            
                questionField.delete(0,END)
                questionField.insert(0,query)
                botReply()
                
            except Exception as e:
             print(e)       


root=Tk()

root.geometry('500x570+100+30')
root.title('ChatBot created by Malyaj Naiwal')
root.config(bg='deep pink')

logoPic=PhotoImage(file='pic.png')

logoPicLabel=Label(root,image=logoPic,bg='deep pink')
logoPicLabel.pack(pady=5)

centerFrame=Frame(root)
centerFrame.pack()

scrollbar=Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=10,yscrollcommand=scrollbar.set
              ,wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=15,fill=X)

askPic=PhotoImage(file='ask.png')


askButton=Button(root,image=askPic,command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()


root.bind('<Return>',click)

thread=threading.Thread(target=audioTotext)
thread.setDaemon(True)
thread.start()

root.mainloop()