#Craeted for the sole purpose of GCI 2019
import pyautogui
import webbrowser
from tkinter import *
import time
z="http://"
def youtube(event):
    root.destroy()
    webbrowser.open_new(z+"youtube.com")
    a=4
    time.sleep(7)
    while a!=0:
        pyautogui.press("tab")
        a-=1
    pyautogui.typewrite("pewdiepie",interval=.1)
    pyautogui.press("enter")
    time.sleep(4)
    a=3         
    while a!=0:
        pyautogui.press("tab")
        a-=1
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("f")
def twitter(event):
    root.destroy()
    webbrowser.open_new(z+"twitter.com")
    time.sleep(10)
    lock=120
    while lock!=0:
        pyautogui.scroll(-60)
        lock-=1
        time.sleep(0.5)
def news(event):
    root.destroy()
    webbrowser.open_new(z+"news.google.com")
    time.sleep(10)
    lock=120
    while lock!=0:
        pyautogui.scroll(-60)
        lock-=1
        time.sleep(0.5)
root= Tk()
root.geometry("350x300")
root.config(bg="#220047")
message=Label(root, text="Welcome,\n what would  you like to do?",fg="#CE9141",bg="#220047",font=("roboto", 18))
message.place(x=30,y=10)

pol=Button(root,text="Watch a youtube video!",bg="#CE9141",fg="#220047",font=("roboto", 15))
pol.place(x=60,y=100)
pol.bind("<Button-1>",youtube)

pol2=Button(root,text="Check your twitter feed!",bg="#CE9141",fg="#220047",font=("roboto", 15))
pol2.place(x=60,y=170)
pol2.bind("<Button-1>",twitter)

pol3=Button(root,text="Look for the latest news!",bg="#CE9141",fg="#220047",font=("roboto", 15))
pol3.place(x=60,y=240)
pol3.bind("<Button-1>",news)

root.mainloop()
