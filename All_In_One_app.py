# Experimental Tkinter app meant for playing around and developing an app naturally
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from datetime import datetime
from tkinter import messagebox
import sqlite3


# Principal Functions & New Windows
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


def open_text():
    # Functions for the button widgets
    # Very basic text editor that can save files.
    # After reading some documents & re-watching tutorials, this makes more sense, but I want to revise it
    text_editor_win = Toplevel(master_window)  # Need to import * from tkinter
    text_editor_win.title("Text Editor")

    Label(text_editor_win, text="Tristan's\nText Editor", font='Helvetica 12 bold',
          relief=RIDGE, bd=5, ).grid(
        row=0, column=2, columnspan=1, sticky="NE"
    )

    def open_file():
        """Open a file for editing"""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete("1.0", tk.END)
        with open(filepath, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        text_editor_win.title(f"Simple Text Editor - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.*"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, mode="w", encoding="utf-8") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        text_editor_win.title(f"Simple Text Editor - {filepath}")

    # Four main widgets
    txt_edit = tk.Text(text_editor_win)
    frm_buttons = tk.Frame(text_editor_win, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
    btn_save = tk.Button(frm_buttons, text="Save as...", command=save_file)

    # Assign widgets to grid locations
    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    frm_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")


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


def submit_address():
    """When called, will initiate the process of connecting to the address database. This takes the
    data from the form on the master window (frm_databases) and stores the data into a .db file.
    """
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')  # Will create db if not already exists
    # Create cursor
    cr = conn.cursor()

    # Insert data into Table
    cr.execute("INSERT INTO addresses VALUES ("
               ":f_name,"
               " :l_name,"
               " :address,"
               " :city,"
               " :state,"
               " :zipcode)",
               {
                   'f_name': f_name.get(),
                   'l_name': l_name.get(),
                   'address': address.get(),
                   'city': city.get(),
                   'state': state.get(),
                   'zipcode': zipcode.get()
               })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # Create a database or connect to one
    conn_address_query = sqlite3.connect('address_book.db')  # Will create db if not already exists
    # Create cursor
    cr = conn_address_query.cursor()

    cr.execute("SELECT *, oid FROM addresses")  # The 'oid' part of this is the PRIMARY KEY
    records = cr.fetchall()

    # Loop through results
    print_records = ""
    for record in records:  # Remember, within a list these data points are stored as tuples
        print_records += str(record[0]) + " " + str(record[1]) + "......................." + str(record[6]) + "\n"

    query_label = Label(frm_databases, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # Commit changes
    conn_address_query.commit()
    # Close connection
    conn_address_query.close()


def delete_record():
    # Create a database or connect to one
    conn_address_query = sqlite3.connect('address_book.db')  # Will create db if not already exists
    # Create cursor
    cr = conn_address_query.cursor()

    # Delete a record
    cr.execute("DELETE from addresses WHERE oid=" + ent_delete.get()) # Formatting is weird

    # Commit changes
    conn_address_query.commit()
    # Close connection
    conn_address_query.close()


"""THE FOLLOWING IS THE MASTER WINDOW FOR THE APPLICATION"""

# Window
master_window = tk.Tk()
master_window.title("Tristan's App Name")
master_window.iconbitmap("senator_AS.ico")
master_window.geometry("")

# Databases (sqlite3)
"""(9/10) Due to the nature of SQL being a major leap in this app's development, I will keep
SQL development notes in this section.

(9/10) I am very tired, but I have been productive! I think it's going to be worth it to 
focus on using the skills I learned from Codemy to develop my movie backlog database.
"""

# Create a database or connect to one
conn_AB = sqlite3.connect('address_book.db')  # Will create db if not already exists
# Create cursor(s)
cr_AB = conn_AB.cursor()

# Create Table
# cr.execute("""CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#         )""")


frm_databases = Frame(master_window, relief=tk.RIDGE, bd=3, height=300)
frm_databases.grid(row=0, column=2, sticky="N")

# Entry Boxes - Address Book
f_name = Entry(frm_databases, width=30)
f_name.grid(row=0, column=1, padx=0)
l_name = Entry(frm_databases, width=30)
l_name.grid(row=1, column=1)
address = Entry(frm_databases, width=30)
address.grid(row=2, column=1)
city = Entry(frm_databases, width=30)
city.grid(row=3, column=1)
state = Entry(frm_databases, width=30)
state.grid(row=4, column=1)
zipcode = Entry(frm_databases, width=30)
zipcode.grid(row=5, column=1)
ent_delete = Entry(frm_databases, width=30)
ent_delete.grid(row=9, column=1)

# Textbox Labels
f_name_label = Label(frm_databases, text="First Name:")
f_name_label.grid(row=0, column=0)
l_name_label = Label(frm_databases, text="Last Name:")
l_name_label.grid(row=1, column=0)
address_label = Label(frm_databases, text="Address:")
address_label.grid(row=2, column=0)
city_label = Label(frm_databases, text="City:")
city_label.grid(row=3, column=0)
state_label = Label(frm_databases, text="State:")
state_label.grid(row=4, column=0)
zipcode_label = Label(frm_databases, text="Zipcode:")
zipcode_label.grid(row=5, column=0)
ent_delete_label = Label(frm_databases, text="Delete ID Number:")
ent_delete_label.grid(row=9, column=0, sticky="E")


# Submission Button
btn_submit = Button(frm_databases, text="Submit to Database", command=submit_address)
btn_submit.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Query Button
btn_query = Button(frm_databases, text="Open Records", command=query)
btn_query.grid(row=8, column=0, columnspan=2, pady=2, padx=10, ipadx=137)

# Delete Button
btn_delete = Button(frm_databases, text="Delete Record", command=delete_record)
btn_delete.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Commit changes to db
conn_AB.commit()

conn_AB.close()

# Row and Column Configurations
basic_window_size()  # NEED TO FIX FUNCTION FOR CALL TO WORK

# Frame Widgets
frm_buttons = tk.Frame(master_window, relief=tk.RIDGE, bd=3)
frm_entries = tk.Frame(master_window, relief=tk.RAISED, bd=3)
frm_calculator = tk.Frame(master_window, relief=tk.SUNKEN, bd=3)
frm_time = tk.Frame(master_window, relief=tk.SUNKEN, bd=3)

# Label Widgets
lbl_widget_welcome_message = tk.Label(frm_buttons, text="Welcome to Tristan's")
lbl_widget_message = tk.Label(frm_entries)
lbl_widget_testing = tk.Label(frm_entries, text="Name:", underline=0)
lbl_widget_current_time = tk.Label(frm_time, text=str(datetime.now().strftime("%H:%M:%S")))

# Button Widgets
btn_widget_message = tk.Button(frm_buttons, text="Click for message", width=15, height=1, command=click_me)
btn_widget_storage = tk.Button(frm_buttons, text="Click for storage", width=15, height=1)
btn_widget_quit = tk.Button(frm_buttons, text="QUIT", width=15, height=1, command=quit_program)
btn_widget_calc = tk.Button(frm_buttons, text="Calculator", width=15, height=1, command=open_calculator)
btn_widget_text_editor = tk.Button(frm_buttons, text="Text Editor", width=15, height=1, command=open_text)
btn_widget_img_viewer = tk.Button(frm_buttons, text="Img Viewer", width=15, height=1)

# New Windows
"""(9/9) To test a new method of creating windows without having to store them in a function, 
I am creating this section. It's going to be a work in progress for a while, but the aim
is to have less code on the top for a more pythonic(clean) look. Readability is going to be a big
concern as this project expands"""


def open_questions():
    """Questionnaire design goals
    - 5 pages of questions with 4 separate, weighted answers [ ]
    - Toplevel window design is clean & pleasant [ ]
    - Status bar tracking # of pages remaining & current page # [ ]
    - Final page showing results dependent on score [ ]

    (9/9)In the future, I want to shift this from a generic form for testing & learning purposes,
    into a more useful and fully-fledge relational-database management system for users to
    store relevant information.
    I will continue to expand this questionnaire if I can decide how to pair it with SQL"""
    profile_questionnaire = Toplevel()
    profile_questionnaire.title("Profile Questionnaire")
    frm_options = Frame(profile_questionnaire, relief=tk.RIDGE, bd=3)

    # A tkinter variable allows for the tracking of which button is selected
    # get() allows for dynamic updates to the differing variable selections

    # Questions should go above the answers
    Label(profile_questionnaire, text="How are you?").pack(anchor=N)

    # Index version of questions. Subject to change
    ANSWERS_WEIGHTS = [
        ("I'm doing Amazing!", "Great"),
        ("I am good", "Good"),
        ("I could be better ", "Okay"),
        ("I'm not okay", "Bad(Sorry...)"),
    ]

    # A dictionary might be a better way to set up the questions
    questionnaire_example = {
        "Today was Great: 5",
        "Today was good:4",
        "Today was fine:3",
        "Today was mediocre:2",
        "Today was bad:1",
    }

    response = StringVar()
    response.set("I am decent")

    for answer, weight in ANSWERS_WEIGHTS:
        Radiobutton(profile_questionnaire, text=answer, variable=response, value=weight).pack(anchor=W)

    btn_profiler_click = Button(profile_questionnaire, text="Submit!", command=lambda: select(response.get()))
    btn_profiler_click.pack()

    def select(value):
        messagebox.showinfo("Profile Results Message", f"Based on your answer you feel:\n{value.upper()}")

    # Message Box to display results
    def results_message():
        messagebox.showinfo("This is a test!", "Howdy!")

    Button(profile_questionnaire, text="Message Box Test", command=results_message).pack()


btn_profile = tk.Button(frm_buttons, text="Profiler", width=15, height=1, command=open_questions)

# Entry Widgets
ent_widget_desc = tk.Entry(frm_entries)
ent_widget_desc.insert(0, "Occupation")
ent_widget_desc.get()

ent_widget = tk.Entry(frm_entries)
ent_widget.insert(0, "First Name")
ent_widget.get()

ent_widget_store_message = tk.Entry(frm_entries)
ent_widget_store_message.insert(0, "Hobbies")
ent_widget_store_message.get()

ent_widget_testing = tk.Entry(frm_entries, width=12, bd=2)
ent_widget_testing.insert(0, "Message Box")
ent_widget_testing.get()

"""Below are the geometry managements for widget locations
    THESE ARE NOT THE WIDGETS THEMSELVES"""

# Sliders
"""Not sure if these will ever be used"""
# vertical = Scale(master_window, from_=0, to=200)
# vertical.grid()
# horizontal = Scale(master_window, from_=0, to=200, orient=HORIZONTAL)
# horizontal.grid()


# Frame Grids
frm_buttons.grid(row=0, column=0, sticky="N")
frm_entries.grid(row=0, column=1, sticky="N")
frm_calculator.grid(row=0, column=2, sticky="N")
frm_time.grid(row=0, column=3, sticky="N")

# Entry Grids
ent_widget.grid(row=0, column=1, sticky="NE", padx=0, pady=0)
ent_widget_store_message.grid(row=1, column=1, sticky="N", padx=0, pady=0)
ent_widget_desc.grid(row=2, column=1, sticky="N", padx=0, pady=0)
ent_widget_testing.grid(row=3, column=1, sticky="NE", padx=0, pady=0)

# Label Grids
lbl_widget_welcome_message.grid(row=0, column=0, sticky="E", padx=0, pady=2)
lbl_widget_message.grid(row=0, column=1, sticky="E")
lbl_widget_testing.grid(row=3, column=1, sticky="NW", padx=10, pady=0)
lbl_widget_current_time.grid(row=0, column=0, sticky="S")

# Button Grids
btn_widget_message.grid(row=2, column=0, sticky="E", padx=0, pady=0)
btn_widget_storage.grid(row=3, column=0, sticky="E", padx=0, pady=0)
btn_widget_calc.grid(row=4, column=0, sticky="E", padx=0, pady=0)
btn_profile.grid(row=5, column=0, sticky="E", pady=0, padx=0)

btn_widget_text_editor.grid(row=2, column=1, sticky="E", padx=0, pady=0)
btn_widget_img_viewer.grid(row=3, column=1, sticky="E", padx=0, pady=0)
btn_widget_quit.grid(row=4, column=1, sticky="S", padx=0, pady=0)

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

>>(9/8) I am trying to add some visual flair to the GUI, but tests so far have been tricky. I will keep
trying to make it work, but for now I will leave the code I have wrote down here.# Local system image widgets
        NON-FUNCTIONAL, NEED TO DO MORE RESEARCH
        img_widget_mast_win = ImageTk.PhotoImage(Image.open("waterfall5.png"))
        img_waterall = Label(image=img_widget_mast_win, width=5, height=2)
        img_waterall.grid(row=0, column=2)
        
>>(9/8) I have learned that Toplevel() acts as a lower position in the tkinter hierarchy. Tk() is the 
top level that initializes the whole thing, but Toplevel is used to denote the uppermost level. 

>>(9/9) I am nearing the point where I can finally integrate a database. I will be staying up late to 
get that started. I wish I could say how long this will take, but I am uncertain at this time. If I recall
correctly, SQL is very easy to read. Shouldn't be too hard to make this work.
"""
