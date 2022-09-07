# Experimental Tkinter app meant for playing around and developing an app naturally
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image


# Principal Functions
def click_me():
    """Create a label widget upon being called.
    Bound to another widget using command="""
    lbl_message = tk.Label(frm_entries, text="Hello " + ent_widget_testing.get())
    if ent_widget_testing.get() == "" or ent_widget_testing.get() == "Erase me!":
        return ent_widget_testing
    lbl_message.grid(row=3, column=1, sticky="NSEW")


def basic_window_size():
    """NON-FUNCTION AT THE MOMENT"""
    master_window.rowconfigure(0, minsize=100, weight=1)
    master_window.columnconfigure(0, minsize=100, weight=1)
    master_window.resizable(width=False, height=False)


def quit_program():
    """Stops the loop after function is called
    Bound to 'quit' button using command="""
    quit()


def storage_button():
    """Store data into specified database.
    -Need to learn SQL in order to get this button to work
    -Need menu to select 'paths' (aka DBs) to send the inputs"""
    pass


def open_calculator():
    """Opens new window after function called
    -Calculator window will have an option to return to main window []

    As of now, I am uncertain if storing the calc window within the function is the best
    way to do this, but it is the only way I have found that doesn't completely break the app.
    """
    calculator_window = Toplevel(master_window)  # Need to import * from tkinter
    calculator_window.title("Calculator")
    basic_window_size()
    calculator_window.resizable(height=False, width=False)

    Label(calculator_window, text="Tristan's\nCalculator App", font='Helvetica 17 bold',
          relief=RIDGE, bd=5, ).grid(
        row=1, column=3, columnspan=4, sticky="NS"
    )

    # Functions within calculator function
    # number as parameter
    def click(number):
        current_number = ent_calc.get()
        ent_calc.delete(0, END)
        ent_calc.insert(0, str(current_number) + str(number))

    # Removes one digit, symbol at a time, rather than deleting everything at once
    def delete_one():
        ent_calc.get()  # Read entry data
        ent_calc.delete(0)  # Delete index position 0 within the entry

    # Clears entry widget
    def clear():
        ent_calc.delete(0, END)

    # MATHEMATICAL OPERATION FUNCTIONS
    def addition():
        first_number = ent_calc.get()  # Read entry data
        global first_num_global  # global allows for calls outside of function
        global math  # Sets a global variable for our results button to read
        math = "addition"  # Acts as a 'key' for buttons to read the type of operation
        first_num_global = int(first_number)  # Convert entry data to integer
        ent_calc.delete(0, END)  # Clear entry field

    def subtraction():
        first_number = ent_calc.get()
        global first_num_global
        global math
        math = "subtraction"
        first_num_global = int(first_number)
        ent_calc.delete(0, END)

    def multiplication():
        first_number = ent_calc.get()
        global first_num_global
        global math
        math = "multiplication"
        first_num_global = int(first_number)
        ent_calc.delete(0, END)

    def division():
        first_number = ent_calc.get()
        global first_num_global
        global math
        math = "division"
        first_num_global = int(first_number)
        ent_calc.delete(0, END)

    def calc_sum():
        second_number = ent_calc.get()
        ent_calc.delete(0, END)  # Removes the first number regardless of other function calls

        if math == "addition":
            ent_calc.insert(0, first_num_global + int(second_number))
        elif math == "subtraction":
            ent_calc.insert(0, first_num_global - int(second_number))
        elif math == "multiplication":
            ent_calc.insert(0, first_num_global * int(second_number))
        elif math == "division":
            ent_calc.insert(0, first_num_global / int(second_number))  # converts to float

    # Buttons within the calculator
    """Using a brute force approach until I can figure out a more elegant option
    -Assign each button number [x]
    -Assign each button grid
    """
    # Number Buttons
    btn_0 = Button(calculator_window, text="0", padx=50, pady=25, command=lambda: click(0), relief=tk.RIDGE)
    btn_1 = Button(calculator_window, text="1", padx=50, pady=25, command=lambda: click(1), relief=tk.RIDGE)
    btn_2 = Button(calculator_window, text="2", padx=50, pady=25, command=lambda: click(2), relief=tk.RIDGE)
    btn_3 = Button(calculator_window, text="3", padx=50, pady=25, command=lambda: click(3), relief=tk.RIDGE)
    btn_4 = Button(calculator_window, text="4", padx=50, pady=25, command=lambda: click(4), relief=tk.RIDGE)
    btn_5 = Button(calculator_window, text="5", padx=50, pady=25, command=lambda: click(5), relief=tk.RIDGE)
    btn_6 = Button(calculator_window, text="6", padx=50, pady=25, command=lambda: click(6), relief=tk.RIDGE)
    btn_7 = Button(calculator_window, text="7", padx=50, pady=25, command=lambda: click(7), relief=tk.RIDGE)
    btn_8 = Button(calculator_window, text="8", padx=50, pady=25, command=lambda: click(8), relief=tk.RIDGE)
    btn_9 = Button(calculator_window, text="9", padx=50, pady=25, command=lambda: click(9), relief=tk.RIDGE)

    # Symbol Buttons
    btn_equals = Button(calculator_window, font="Arial 10 bold", text="=", padx=49, pady=25, command=calc_sum)
    btn_plus = Button(calculator_window, font='Arial 10 bold', text="+", padx=20, pady=5, command=addition)
    btn_minus = Button(calculator_window, font="Arial 10 bold", text="-", padx=22, pady=5, command=subtraction)
    btn_multiply = Button(calculator_window, font="Arial 10 bold", text="*", padx=22, pady=8, command=multiplication)
    btn_divide = Button(calculator_window, font="Arial 10 bold", text="/", padx=22, pady=8, command=division)
    btn_del_one = Button(calculator_window, text="Backspace", padx=20, pady=3, command=lambda: delete_one())
    btn_clear = Button(calculator_window, text="Clear", padx=20, pady=3, command=clear)

    # Button Grid Layout
    btn_1.grid(row=3, column=2)
    btn_2.grid(row=3, column=1)
    btn_3.grid(row=3, column=0)

    btn_4.grid(row=2, column=2)
    btn_5.grid(row=2, column=1)
    btn_6.grid(row=2, column=0)

    btn_7.grid(row=1, column=2)
    btn_8.grid(row=1, column=1)
    btn_9.grid(row=1, column=0)

    btn_0.grid(row=4, column=0)

    # Symbol Grid
    btn_equals.grid(row=4, column=2)
    btn_plus.grid(row=4, column=1, sticky="NW")
    btn_minus.grid(row=4, column=1, sticky="NE")
    btn_multiply.grid(row=4, column=1, sticky="SW")
    btn_divide.grid(row=4, column=1, sticky="SE")
    btn_del_one.grid(row=5, column=0, sticky="WE")
    btn_clear.grid(row=5, column=1, sticky="WE")

    # Entry Line
    ent_calc = Entry(calculator_window, width=35, borderwidth=5)
    ent_calc.grid(row=0, column=0, columnspan=3, padx=20, pady=10)

    # Local system image widgets
    """NON-FUNCTIONAL, NEED TO DO MORE RESEARCH"""
    img_widget_mast_win = ImageTk.PhotoImage(Image.open("waterfall5.png"))
    water_fall = Label(calculator_window, image=img_widget_mast_win)
    water_fall.grid(calculator_window)


"""THE FOLLOWING IS THE MAIN WINDOW FOR THE APPLICATION"""

# Window
master_window = tk.Tk()
master_window.title("Tristan's App Name")
master_window.iconbitmap("senator_AS.ico")

# Row and Column Configurations
basic_window_size()

# Frame Widgets
frm_buttons = tk.Frame(master_window, relief=tk.RIDGE, bd=3)
frm_entries = tk.Frame(master_window, relief=tk.RAISED, bd=3)
frm_calculator = tk.Frame(master_window, relief=tk.SUNKEN, bd=3)

# Label Widgets
lbl_widget = tk.Label(frm_buttons, text="Entry Box 1:")
lbl_widget_message = tk.Label(frm_entries)
lbl_widget_testing = tk.Label(frm_entries, text="Name:", underline=0)

# Button Widgets
btn_widget_message = tk.Button(frm_buttons, text="Click for message", width=15, height=1, command=click_me)
btn_widget_storage = tk.Button(frm_buttons, text="Click for storage", width=15, height=1)
btn_widget_quit = tk.Button(frm_buttons, text="QUIT", width=15, height=1, command=quit_program)
btn_widget_calc = tk.Button(frm_buttons, text="Calculator", width=15, height=1, command=open_calculator)

# Entry Widgets
ent_widget_desc = tk.Entry(frm_entries)
ent_widget_desc.insert(0, "Entry box")
ent_widget_desc.get()

ent_widget = tk.Entry(frm_entries)
ent_widget.insert(0, "Entry box")
ent_widget.get()

ent_widget_store_message = tk.Entry(frm_entries)
ent_widget_store_message.insert(0, "Entry box")
ent_widget_store_message.get()

ent_widget_testing = tk.Entry(frm_entries, width=10, bd=2)
ent_widget_testing.insert(0, "Erase me!")
ent_widget_testing.get()

"""Below are the geometry managements for widget locations
    THESE ARE NOT THE WIDGETS THEMSELVES"""

# Frame Grids
frm_buttons.grid(row=0, column=0, sticky="N")
frm_entries.grid(row=0, column=1, sticky="N")
frm_calculator.grid(row=0, column=2, sticky="N")

# Entry Grids
ent_widget.grid(row=0, column=1, sticky="N", padx=0, pady=0)
ent_widget_store_message.grid(row=1, column=1, sticky="N", padx=0, pady=0)
ent_widget_desc.grid(row=2, column=1, sticky="N", padx=0, pady=0)
ent_widget_testing.grid(row=3, column=1, sticky="NE", padx=0, pady=0)

# Label Grids
lbl_widget.grid(row=1, column=0, sticky="E")
lbl_widget_message.grid(row=0, column=1, sticky="E")
lbl_widget_testing.grid(row=3, column=1, sticky="NW", padx=10, pady=0)

# Button Grids
btn_widget_message.grid(row=2, column=0, sticky="E", padx=0, pady=0)
btn_widget_storage.grid(row=3, column=0, sticky="E", padx=0, pady=0)
btn_widget_quit.grid(row=5, column=0, sticky="S", padx=0, pady=0)
btn_widget_calc.grid(row=4, column=0, sticky="E", padx=0, pady=0)

master_window.mainloop()

# Personal Notes
"""
!!! Main types of widgets: label, entry, button, frame, text

>>I am not sure what I want this little app to be, but it will
come to me as I experiment and try new things.

>>Layout could be smoothed over. Is this the most efficient way to set up this application?

>>(9/6) So far I am making progress in shaping my skills without the need for a tutorial
It's becoming easier to understand event handling and managing layouts. If needed, I will
look to more tutorials specifically based within Tkinter to expand my knowledge. The next
one I am looking at is Freecodecamp's Tkinter course. The course features an SQL and Tkinter
tutorial. Might be useful! 

>>(9/6) New idea, I think I could create a back-logger. Basically, I tell the system
the type of media(aka which database to enter the data) I want to input. It will act as
a 'what I already own' versus what I do not own. It's becoming hard to remember what movies
and games I already own.

>>(9/6) Decided to save some time on the basic shape and size of the windows by creating
a template function called basic_window_size.

>>(9/6) Could I possibly use loops to optimize the buttons within the calculator function? 
Also, is there a way to store the calculator window outside of the open_calculator function? 
Lastly, have I spent the past 3 hours on this?
Answers are as follows: likely, uncertain, and yes.

>>(9/7) Codemy/FCC had an excellent tutorial over setting up the functions for the calculator.
I learned how to set up the buttons after one or two examples, and now the whole calculator works as intended.
The next step is experimenting with other basic features. I will likely use this as my code sample project.

>>(9/7) Installed the Pillow(PIL) module from the Python Packages section. This should allow for more advanced
image processing. Tkinter apparently supports only gif and pmn(?). Pillow allows for pngs and jpegs
"""
