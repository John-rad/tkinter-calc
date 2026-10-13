from tkinter import Tk, ttk, StringVar, PhotoImage
import tkinter as tk

class Calc:

    # configuration options for the calculator
    PADDING_SM = 1
    PADDING_BASE = 2
    PADDING_LG = 4

    MARGIN_SM = 2
    MARGIN_BASE = 5
    MARGIN_LG = 10

    # Tk uses a font description such as {courier 10 bold}; 
    # in tkinter this is most naturally passed as a 
    # tuple of (family, size, *styles) 
    # (or as the equivalent string "Courier 10 bold"). 
    # Font sizes with positive numbers are measured in points; 
    # sizes with negative numbers are measured in pixels.
    #  - https://docs.python.org/3/library/tkinter.html#handy-reference
    FONT_SIZE_TERTIARY = -16
    FONT_SIZE_SECONDARY = -18
    FONT_SIZE_PRIMARY = -24

    FONT_PRIMARY = ("Helvetica", FONT_SIZE_PRIMARY, "bold")
    FONT_SECONDARY = ("Helvetica", FONT_SIZE_SECONDARY)
    FONT_TERTIARY = ("Helvetica", FONT_SIZE_TERTIARY)

    DISPLAY_WIDTH = 300 
    DISPLAY_HEIGHT = 370
    
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Calculator")
        self.root.configure(pady=Calc.MARGIN_BASE, padx=Calc.MARGIN_BASE)


        # Window size settings
        self.root.resizable(False, False) # disabled resizing for now
        self.center_window()
        

        # Opacity control for the calc window
        self.root.attributes(alpha=0.95)

        # Image for the backspace button
        self.__bkspace_img = PhotoImage(file="./assets/delete-back-2-line (1).png")
        print(self.__bkspace_img)

        # the text/image, row, and column for each button
        self.__button_text: list[tuple[str, int, int, PhotoImage | None]] = [
            ("del", 0, 0, self.__bkspace_img), ("CE", 0, 1, None), ("C", 0, 2, None), 
            ("/", 0, 3, None), ("7", 1, 0, None), ("8", 1, 1, None), 
            ("9", 1, 2, None), ("x", 1, 3, None), ("4", 2, 0, None), 
            ("5", 2, 1, None), ("6", 2, 2, None), ("-", 2, 3, None), 
            ("1", 3, 0, None), ("2", 3, 1, None), ("3", 3, 2, None), 
            ("+", 3, 3, None), ("+/-", 4, 0, None), ("0", 4, 1, None), 
            (".", 4, 2, None), ("=", 4, 3, None)]


        # Frame controlling the entry input and display field
        self.display_frame = ttk.Frame(self.root)
        self.display_frame.pack(side="top", fill="both", expand=True, pady=Calc.MARGIN_SM)


        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side="bottom", fill="both", expand=True, pady=Calc.MARGIN_SM)

        # style control for ttk widgets
        self.style = ttk.Style()
        self.style.configure("TButton", font=Calc.FONT_SECONDARY) 

        # calculator display variables
        self.input_val = StringVar(self.root, value="0")
        self.last_input = StringVar(self.root, value="")
        self.display_value = StringVar(self.root, value="")
        self.active_operator = StringVar(self.root, value="")

        # TEntry has a weird quirk that does not allow some of its options to be changed 
        # via ttk.Style, so I opted for using its keyword arguments on creation. 
        # I see a future of pain for this component's customizability ^-^
        # I simply switched to tk.Entry as this is more flexible when customizing.
        self.input = tk.Entry(self.display_frame, textvariable=self.input_val, 
                                  justify="right", font=Calc.FONT_PRIMARY, 
                                  takefocus=False, bd=0, highlightthickness=0, 
                                  relief="solid", state="readonly")

        self.display = tk.Entry(self.display_frame, textvariable=self.display_value, 
                                  justify="right", font=Calc.FONT_TERTIARY, 
                                  takefocus=False, bd=0, highlightthickness=0, 
                                  relief="solid", state="readonly")


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
        for text, row, column, image in self.__button_text:
            # if the image test passes, then an image is set for the button
            if isinstance(image, PhotoImage):
                btn = ttk.Button(self.button_frame, image=image, text=text)
            else:
                btn = ttk.Button(self.button_frame, text=text)

            # display the button's value when clicked on the display
            btn.bind("<Button-1>", self.assign_btn)

            btn.grid(row=row, column=column, ipadx=Calc.PADDING_BASE, ipady=Calc.PADDING_LG, sticky="nsew")


    def assign_btn(self, event:tk.Event):
        current_val : str = self.input_val.get()
        pressed_key : str = event.widget.cget("text")
        last_input : str = self.last_input.get()
        previous_operator : str = self.active_operator.get()

        print(previous_operator)
        print(last_input)
        # print(f"{current_val} {pressed_key} {last_input}")

        if (pressed_key.isdigit() or pressed_key == "."):
            # case 3: if there was a previous operator .i.e. x, -, +, or /. Reset the input display
            if (previous_operator):
                self.update_input() # clear the input display
                current_val = "" # reset the temp current_val 

            # case 1: input screen and pressed key equal zero
            if (current_val == "0" and pressed_key != "0"):
                current_val = pressed_key

            # case 2: pressed key and the last input is a digit
            else:
                current_val = f"{current_val}{pressed_key}"

            self.update_input(current_val)


        # case 3: pressed key is a symbol
        else:
            match pressed_key:
                case "CE":
                    self.update_input() # clear the input display
                case "C":
                    self.clear_all()
                case "del":
                    # this check prevents the delete action from being performed 
                    # if there is no visual input in the input field
                    if (current_val == "0"):
                        return
                    elif (len(last_input) > 1): 
                        current_val = current_val[:-1]
                        self.input_val.set(current_val) # set the input field to one character less than before
                        self.last_input.set(current_val)
                    else:
                        self.last_input.set("")
                        self.input_val.set("0")

                case "x" | "/" | "+" | "-":
                    # override the previous operator
                    self.active_operator.set(pressed_key)
                    # set the display field to the current_val and pressed_key
                    self.display_value.set(f"{current_val} {pressed_key}")
                case _:
                    pass

    # Refactored the display clearing mechanism into methods for ease of access
    def update_input(self, placeholder: str = ""):
        '''sets the input display and last_input to placeholder, 
        clears both if placeholder is omitted'''

        # Without this check self.last_input gets assigned zero when placeholder is zero and I don't
        # want that if the action is clearing the screen and zero was not pressed.
        if placeholder == "0": self.last_input.set("") 
        else: self.last_input.set(placeholder) 

        if not placeholder: self.active_operator.set("")

        self.input_val.set(placeholder)

    def clear_all(self):
        self.update_input("0")                 
        self.display_value.set("") # clear the display field

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
        self.display.pack(side="top", expand=True, fill="both")
        self.input.pack(side="bottom", expand=True, fill="both")
        self.make_btns()
        
    def run(self):
        # Hide the window
        self.root.withdraw()

        # Render the components to the root window
        self.show_elements()

        # Force the creation of the window's components
        self.root.update()

        # Reveal the window once the elements have been rendered
        self.root.deiconify()

        # Keep the window open
        self.root.mainloop()


if __name__ == "__main__":
    calc = Calc()
    # print(Calc._Calc__button_text)
    calc.run()