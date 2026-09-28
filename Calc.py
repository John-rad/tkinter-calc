from tkinter import Tk, ttk, StringVar
class Calc:
    # this private class list holds the text/image, row, and column
    __button_text = [("<-", 0, 0), ("CE", 0, 1), ("C", 0, 2), ("/", 0, 3), 
                     ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("x", 1, 3), 
                     ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
                     ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
                     ("+/-", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3)]

    # configuration options for the calculator
    PADDING_SM = 1
    PADDING_BASE = 2
    PADDING_LG = 4

    MARGIN_SM = 2
    MARGIN_BASE = 5
    MARGIN_LG = 10

    FONT_SIZE_TERTIARY = 16
    FONT_SIZE_SECONDARY = -16

    # Tk uses a font description such as {courier 10 bold}; 
    # in tkinter this is most naturally passed as a 
    # tuple of (family, size, *styles) 
    # (or as the equivalent string "Courier 10 bold"). 
    # Font sizes with positive numbers are measured in points; 
    # sizes with negative numbers are measured in pixels.
    #  - https://docs.python.org/3/library/tkinter.html#handy-reference

    FONT_SIZE_PRIMARY = -20

    FONT_PRIMARY = ("Helvetica", FONT_SIZE_PRIMARY, "bold")
    FONT_SECONDARY = ("Helvetica", FONT_SIZE_SECONDARY, "bold")

    DISPLAY_WIDTH = 300 
    DISPLAY_HEIGHT = 300 
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Calculator")
        self.root.configure(pady=5)


        # Window size settings
        self.root.resizable(False, False) # disabled resizing for now
        self.center_window()
        

        # Opacity control for the calc window
        self.root.attributes(alpha=0.95)


        self.display_frame = ttk.Frame(self.root)
        self.display_frame.pack(side="top", fill="both", expand=True, padx=Calc.MARGIN_LG, pady=Calc.MARGIN_BASE)

        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side="bottom", fill="both", expand=True, padx=Calc.MARGIN_LG, pady=Calc.MARGIN_BASE)

        # style control for ttk widgets
        self.style = ttk.Style()
        self.style.configure("TButton", font=Calc.FONT_SECONDARY) 

        # calculator display
        self.input_val = StringVar(self.root, value="0")

        # TEntry has a weird quirk that does not allow some of its options to be changed 
        # via ttk.Style, so I opted for using its keyword arguments on creation. 
        # I see a future of pain for this component's customizability ^-^
        self.display = ttk.Entry(self.display_frame, textvariable=self.input_val, 
                                  justify="right",
                                 font=Calc.FONT_PRIMARY)

        self.show_elements()

    def make_btns(self):
        # Configure grid row/column weights so buttons expand evenly - Thanks Gemini :)
        # Without this loop, the grid within the button frame will not 
        # expand when the window of the app is maximized or resized.
        for i in range(4):
            self.button_frame.columnconfigure(i, weight=1)
            self.button_frame.rowconfigure(i, weight=1)
            if i == 3:
                self.button_frame.rowconfigure(i+1, weight=1)

        # Add buttons to the calculator and display them
        for text, row, column in Calc.__button_text:
            btn = ttk.Button(self.button_frame, text=text)
            btn.grid(row=row, column=column, ipadx=Calc.PADDING_BASE, ipady=Calc.PADDING_LG, sticky="nsew")

    def center_window(self):
        # I need to be more patient with the tkinter doc, thanks Gemini again :>
        # Get the user's screen width and height through self.root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate x and y coordinates for centering
        x = (screen_width - Calc.DISPLAY_WIDTH) // 2
        y = (screen_height - Calc.DISPLAY_HEIGHT) // 2


        # center the window using x and y as offsets
        self.root.geometry(f"{self.DISPLAY_WIDTH}x{Calc.DISPLAY_HEIGHT}"
                           f"+{x}+{y}")

    def show_elements(self):
        # .grid(column=0, row=0, columnspan=4, ipadx=Calc.PADDING_LG)
        # expand=True, ipadx=Calc.PADDING_LG
        self.display.pack(expand=True, fill="both")
        self.make_btns()
        
    def run(self):
        self.show_elements()
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calc()
    # print(Calc._Calc__button_text)
    calc.run()