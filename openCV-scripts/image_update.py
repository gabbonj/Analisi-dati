import tkinter as tk
import cv2

def display_image(a):
    param1 = slider1.get()
    param2 = slider2.get()
    result = cv2.Canny(image, param1, param2)
    cv2.imshow('Result', result)


if __name__ == "__main__":

    image = cv2.imread('../.images/gatto.jpg', 1)

    window = tk.Tk()
    window.title('controlls')
    window.geometry('200x200')

    label1 = tk.Label(window, text='Controll 1')
    label1.grid(row=0, column=0)
    slider1 = tk.Scale(window, from_=0, to=200, command=display_image)
    slider1.grid(row=1, column=0)

    label2 = tk.Label(window, text='Controll 2')
    label2.grid(row=0, column=1)
    slider2 = tk.Scale(window, from_=0, to=200, command=display_image)
    slider2.grid(row=1, column=1)

    window.mainloop()

