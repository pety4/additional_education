import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import cv2


class RectangleOnWebCam():
    rectangles = np.array([[-50, -50]], int)

    def mouseButtonClick(self, event):
        self.rectangles = np.append(self.rectangles, [[event.x, event.y]], axis=0)
        print(event.x, event.y)
        print(self.rectangles)

    def keyPressed(self, event):
        if event.char=='q':
            self.programQuit()
        if event.char == 'c':
            self.clearVideo()

    def clearVideo(self, event):
        print("Button c pressed")
        self.rectangles = np.array([[-50, -50]], int)
    def show_frames(self):
        cv2image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
        for coords in self.rectangles:
            cv2.rectangle(cv2image, (coords[0] - 5, coords[1] - 5), (coords[0] + 5, coords[1] + 5), (0, 0, 0))
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)
        self.label.bind("<Button-1>", self.mouseButtonClick)
        self.clearButton.bind("<Button-1>", self.clearVideo)
        self.win.bind("<KeyPress>", self.keyPressed)
        self.label.after(1, self.show_frames)

    def programQuit(self):
        from tkinter.messagebox import askyesno
        result = askyesno(title="Accept", message="Are you sure you want to quit?")
        if result == 1:
            self.win.destroy()
            self.cap.release()

    def __init__(self):
        self.win = tk.Tk()
        self.label = tk.Label(self.win)
        self.label.grid(row=0, column=0, rowspan=2)
        self.cap = cv2.VideoCapture(0)
        self.quitButton = tk.Button(text="Выход из программы", font=("Times New Roman", 14), command=self.programQuit)
        self.quitButton.grid(row=0, column=1)
        self.clearButton = tk.Button(text="Очистить", font=("Times New Roman", 14))
        self.clearButton.grid(row=1, column=1)
        self.show_frames()
        self.win.mainloop()
        self.cap.release()


RectangleOnWebCam()
