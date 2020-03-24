class Calculator(object):
    def __init__(self, win, width, height):
        self.win = win
        self.WIDTH = width
        self.HEIGHT = height
        self.ticking = False
        self.widgets = []
        self.equation = ''
        self.displayval = ''

    def clear(self):
        for widget in self.widgets:
            widget.destroy()

    def draw(self):
        from tkinter import Label, Button, TOP, Frame, X, Y, LEFT

        def click(char):
            newchar = char
            if char not in ['=', 'AC', 'DEL']:
                if char == '÷':
                    newchar = '/'
                elif char == '×':
                    newchar = '*'
                self.equation += newchar
                self.displayval += char
            else:
                if char == '=':
                    try:
                        self.equation = str(eval(self.equation))
                        self.displayval = self.equation
                    except SyntaxError:
                        pass
                elif char == 'AC':
                    self.equation = ''
                    self.displayval = ''

                elif char == 'DEL':
                    self.equation = self.equation[:-1]
                    self.displayval = self.displayval[:-1]

            display.config(text=self.displayval)

        def gen_frame_row():
            frame = Frame(button_frame)
            frame.pack(side=TOP, fill=X, expand=True)
            self.widgets.append(frame)
            return frame

        def gen_button(character, frame):
            btn_frame = Frame(frame, width=self.WIDTH//4, height=self.HEIGHT//4*3//5)
            btn_frame.pack(side=LEFT, fill=Y, expand=True)
            btn_frame.pack_propagate(0)
            button = Button(btn_frame, text=character, command=lambda: click(character), font=('Arial', 40))
            button.pack(expand=True, fill='both')
            self.widgets.append(btn_frame)
            self.widgets.append(button)

        display_frame = Frame(self.win, height=self.HEIGHT//4)
        display_frame.pack(side=TOP, expand=True, fill=X)
        display_frame.pack_propagate(0)
        display = Label(display_frame, text=self.equation, anchor="e", font=('Arial', 45))
        display.pack(expand=True, fill='both')
        self.widgets.append(display)
        self.widgets.append(display_frame)

        button_frame = Frame(self.win, height=self.HEIGHT//4*3)
        button_frame.pack(expand=True, fill='both')
        button_frame.pack_propagate(0)

        buttons = [
            ['(', ')', 'DEL', 'AC'],
            ['7', '8', '9', '÷'],
            ['4', '5', '6', '×'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for row, row_val in enumerate(buttons):
            frame = gen_frame_row()
            for col, col_val in enumerate(row_val):
                gen_button(col_val, frame)
