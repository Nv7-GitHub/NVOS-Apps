class SimpleApp(object):
    def __init__(self, win, width, height):
        self.win = win
        self.WIDTH = width
        self.HEIGHT = height
        self.widgets = []
        self.ticking = False

    def draw(self):
        from tkinter import Label

        label = Label(self.win, text='This is a simple app.')

        label.pack(self.win, expand=True, fill='both')

        self.widgets.append(label)

    def clear(self):
        self.widgets[0].pack_forget()
