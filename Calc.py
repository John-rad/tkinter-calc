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
    MARGIN_LG = 22

    FONT_SIZE_TERTIARY = 16
    FONT_SIZE_SECONDARY = 18

    CALC_WIDTH = 100

    # Tk uses a font description such as {courier 10 bold}; 
    # in tkinter this is most naturally passed as a 
    # tuple of (family, size, *styles) 
    # (or as the equivalent string "Courier 10 bold"). 
    # Font sizes with positive numbers are measured in points; 
    # sizes with negative numbers are measured in pixels.
    #  - https://docs.python.org/3/library/tkinter.html#handy-reference

    FONT_SIZE_PRIMARY = -24

    FONT_PRIMARY = ("Helvetica", FONT_SIZE_PRIMARY, "bold")

    DISPLAY_WIDTH = 50 # had to tone down the size, cos I thought I was working with pixels :(
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Calc")
        # self.root.geometry("640x480")
        self.frame = ttk.Frame(self.root, padding=Calc.MARGIN_SM)
        print(self.frame.winfo_width())
        self.frame.grid()

        # style control for ttk widgets
        self.style = ttk.Style()
        self.style.configure("TButton", ) 

        # calculator display
        self.input_val = tk.StringVar(self.root, value="0")

        # TEntry has a weird quirk that does not allow some of its options to be changed 
        # via ttk.Style, so I opted for using its keyword arguments on creation. 
        # I see a future of pain for this component's customizability ^-^
        self.display = ttk.Entry(self.frame, textvariable=self.input_val, 
                                  justify="right",
                                 font=Calc.FONT_PRIMARY)

        # calculator buttons
        self.backspace = self.make_btn(Calc.__button_text[0])
        self.clear_entry = self.make_btn(Calc.__button_text[1])
        self.clear_screen = self.make_btn(Calc.__button_text[2])
        self.divide_sign = self.make_btn(Calc.__button_text[3])
        self.no_seven = self.make_btn(Calc.__button_text[4])
        self.no_eight = self.make_btn(Calc.__button_text[5])
        self.no_nine = self.make_btn(Calc.__button_text[6])
        self.multiply_sign = self.make_btn(Calc.__button_text[7])
        self.no_four = self.make_btn(Calc.__button_text[8])
        self.no_five = self.make_btn(Calc.__button_text[9])
        self.no_six = self.make_btn(Calc.__button_text[10])
        self.minus_sign = self.make_btn(Calc.__button_text[11])
        self.no_one = self.make_btn(Calc.__button_text[12])
        self.no_two = self.make_btn(Calc.__button_text[13])
        self.no_three = self.make_btn(Calc.__button_text[14])
        self.plus_sign = self.make_btn(Calc.__button_text[15])
        self.polarity = self.make_btn(Calc.__button_text[16])
        self.zero = self.make_btn(Calc.__button_text[17])
        self.decimal_point = self.make_btn(Calc.__button_text[18])
        self.equal_sign = self.make_btn(Calc.__button_text[19])

    def make_btn(self, btn_text: str):
        return ttk.Button(self.frame, text=btn_text)

    def show_elements(self):
        self.display.grid(column=0, row=0, columnspan=4, ipadx=Calc.PADDING_LG)
        self.backspace.grid(column=0, row=1)
        self.clear_entry.grid(column=1, row=1)
        self.clear_screen.grid(column=2, row=1)
        self.divide_sign.grid(column=3, row=1)
        self.no_seven.grid(column=0, row=2)
        self.no_eight.grid(column=1, row=2)
        self.no_nine.grid(column=2, row=2)
        self.multiply_sign.grid(column=3, row=2)
        self.no_four.grid(column=0, row=3)
        self.no_five.grid(column=1, row=3)
        self.no_six.grid(column=2, row=3)
        self.minus_sign.grid(column=3, row=3)
        self.no_one.grid(column=0, row=4)
        self.no_two.grid(column=1, row=4)
        self.no_three.grid(column=2, row=4)
        self.plus_sign.grid(column=3, row=4)
        self.polarity.grid(column=0, row=5)
        self.zero.grid(column=1, row=5)
        self.decimal_point.grid(column=2, row=5)
        self.equal_sign.grid(column=3, row=5)

    def run(self):
        self.show_elements()
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calc()
    # print(Calc._Calc__button_text)
    calc.run()