import RPi.GPIO as GPIO
import tkinter as tk
import time

GPIO.setwarnings(False)
window = tk.Tk()
window.title("5.2C GUI")
window.geometry('350x250+700+200')


#PINS for LEDS
LED_RED = 21
LED_YELLOW = 20
LED_GREEN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

var = tk.IntVar()

def ledOn():
    reset_leds()
    GPIO.output(var.get(), GPIO.HIGH)


def reset_leds():
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_YELLOW, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.LOW)
    
reset_leds()


redBut = tk.Radiobutton(window, command=ledOn, variable=var, value=LED_RED, text="Red LED")
yellowBut = tk.Radiobutton(window, command=ledOn, variable=var, value=LED_YELLOW, text="Yellow LED")
greenBut = tk.Radiobutton(window, command=ledOn, variable=var, value=LED_GREEN, text="Green LED")

redBut.pack()
yellowBut.pack()
greenBut.pack()

window.mainloop()




