import tkinter as tk
from tkinter import Tk, ttk
class Calc:
    __button_text = ["<-", "CE", "C", "/", 
                     "7", "8", "9", "x", 
                     "4", "5", "6", "-",
                     "1", "2", "3", "+",
                     "+/-", "0", ".", "="]

    # configuration options for the calculator
    PADDING_SM = 8
    PADDING_BASE = 12
    PADDING_LG = 16

    MARGIN_SM = 5
    MARGIN_BASE = 20
    MARGIN_LG = 25

    FONT_SIZE_TERTIARY = 12
    FONT_SIZE_SECONDARY = 14
    FONT_SIZE_PRIMARY = 16
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Calc")
        # self.root.geometry("640x480")
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.configure(width=200)
        self.frame.grid()

        # calculator display
        self.input_val = tk.StringVar(self.root, value="0")
        # self.button = ttk.Button(self.frame, text="Hello World!").grid(column=0, row=0, columnspan=2)
        self.display = ttk.Entry(self.frame, textvariable=self.input_val).grid(column=0, row=0, columnspan=4, pady=10)

        # calculator buttons
        self.backspace = self.make_btn(Calc.__button_text[0]).grid(column=0, row=1)
        self.clear_entry = self.make_btn(Calc.__button_text[1]).grid(column=1, row=1)
        self.clear_screen = self.make_btn(Calc.__button_text[2]).grid(column=2, row=1)
        self.divide_sign = self.make_btn(Calc.__button_text[3]).grid(column=3, row=1)
        self.no_seven = self.make_btn(Calc.__button_text[4]).grid(column=0, row=2)
        self.no_eight = self.make_btn(Calc.__button_text[5]).grid(column=1, row=2)
        self.no_nine = self.make_btn(Calc.__button_text[6]).grid(column=2, row=2)
        self.multiply_sign = self.make_btn(Calc.__button_text[7]).grid(column=3, row=2)
        self.no_four = self.make_btn(Calc.__button_text[8]).grid(column=0, row=3)
        self.no_five = self.make_btn(Calc.__button_text[9]).grid(column=1, row=3)
        self.no_six = self.make_btn(Calc.__button_text[10]).grid(column=2, row=3)
        self.minus_sign = self.make_btn(Calc.__button_text[11]).grid(column=3, row=3)
        self.polarity = self.make_btn(Calc.__button_text[12]).grid(column=0, row=4)
        self.zero = self.make_btn(Calc.__button_text[13]).grid(column=1, row=4)
        self.decimal_point = self.make_btn(Calc.__button_text[14]).grid(column=2, row=4)
        self.equal_sign = self.make_btn(Calc.__button_text[15]).grid(column=3, row=4)

    def make_btn(self, btn_text: str):
        return ttk.Button(self.frame, text=btn_text)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calc()
    # print(Calc._Calc__button_text)
    calc.run()