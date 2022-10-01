# Experimental Tkinter app meant for playing around and developing an app naturally
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from datetime import datetime
from tkinter import messagebox
import sqlite3
from time import strftime
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Principal Functions & New Windows
def click_me():
    pass
    """Create a label widget upon being called.
    Bound to another widget using command="""
    # lbl_message = tk.Label(frm_entries, text="Hello " + ent_widget_testing.get())
    # if ent_widget_testing.get() == "" or ent_widget_testing.get() == "Erase me!":
    #     return ent_widget_testing
    # lbl_message.grid(row=3, column=1, sticky="NSEW")


# Defines basic program shape
def basic_window_size():
    """NON-FUNCTION AT THE MOMENT"""
    master_window.rowconfigure(0, minsize=100, weight=1)
    master_window.columnconfigure(0, minsize=100, weight=1)
    master_window.resizable(width=False, height=False)


# Ends program
def quit_program():
    """Stops the loop after function is called
    Bound to 'quit' button using command="""
    quit()


# Controls time and updates every 1 second (1000 milliseconds)
def timeclock():
    """Continually updates time by setting it to a variable,
    updating it every 1 second"""
    display = strftime('%H:%M:%S %p')
    lbl_widget_current_time.config(text=display)
    lbl_widget_current_time.after(1000, timeclock)


# Opens Text editor
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
    frm_buttons = tk.Frame(text_editor_win, relief=tk.RAISED, bd=5)
    btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
    btn_save = tk.Button(frm_buttons, text="Save as...", command=save_file)

    # Assign widgets to grid locations
    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)
    frm_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")


# Access calculator window
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


# Submits user information to database
def submit_address():
    """When called, will initiate the process of connecting to the address database. This takes the
    data from the form on the master window (frm_databases) and stores the data into a .db file.
    """
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')  # Will create db if not already exists
    # Create cursor
    cr = conn.cursor()

    # Insert data into Table
    cr.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :Age, :address, :city, :state, :zipcode, :salary)",
               {
                   'f_name': f_name.get(),
                   'l_name': l_name.get(),
                   'Age': age.get(),
                   'address': address.get(),
                   'city': city.get(),
                   'state': state.get(),
                   'zipcode': zipcode.get(),
                   'salary': salary.get()
               })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    salary.delete(0, END)


# Query database to display names
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
        print_records += str(record[0]) + " " + str(record[1]) + "......................." + '[id]' + str(record[8]) + \
                         "\n"

    query_label = Label(frm_databases, relief=tk.RAISED, bd=3, text=print_records)
    query_label.grid(row=15, column=0, columnspan=8)  # (9/16) Need to make this more dynamic

    # Commit changes
    conn_address_query.commit()
    # Close connection
    conn_address_query.close()


# Remove record entry
def delete_record():
    # Create a database or connect to one
    conn_address_query = sqlite3.connect('address_book.db')  # Will create db if not already exists
    # Create cursor
    cr = conn_address_query.cursor()

    # Delete a record
    cr.execute("DELETE from addresses WHERE oid=" + ent_record_entry.get())  # Formatting is weird

    ent_record_entry.delete(0, END)

    # Commit changes
    conn_address_query.commit()
    # Close connection
    conn_address_query.close()


# Edit record
def change_record():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')  # Will create db if not already exists
    # Create cursor
    cr = conn.cursor()

    record_id = ent_record_entry.get()

    cr.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        Age = :Age,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode,
        salary = :salary

        WHERE oid = :oid""",
               {
                   'first': f_name_update.get(),
                   'last': l_name_update.get(),
                   'Age': age.get(),
                   'address': address_update.get(),
                   'city': city_update.get(),
                   'state': state_update.get(),
                   'zipcode': zipcode_update.get(),
                   'salary': salary_update.get(),
                   'oid': record_id
               })

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    updater.destroy()


# Update record function
def update_record():
    global updater
    updater = tk.Tk()
    updater.title("Update Record Credentials")

    updater.geometry("")

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')  # Will create db if not already exists
    # Create cursor
    cr = conn.cursor()

    record_id = ent_record_entry.get()
    cr.execute("SELECT * FROM addresses WHERE oid = " + record_id)  # The 'oid' part of this is the PRIMARY KEY
    records = cr.fetchall()

    global f_name_update
    global l_name_update
    global age_update
    global address_update
    global city_update
    global state_update
    global zipcode_update
    global salary_update

    # Entry Boxes - Address Book
    f_name_update = Entry(updater, width=30)
    f_name_update.grid(row=0, column=1, padx=0)
    l_name_update = Entry(updater, width=30)
    l_name_update.grid(row=1, column=1)
    age_update = Entry(updater, width=30)
    age_update.grid(row=2, column=1)
    address_update = Entry(updater, width=30)
    address_update.grid(row=3, column=1)
    city_update = Entry(updater, width=30)
    city_update.grid(row=4, column=1)
    state_update = Entry(updater, width=30)
    state_update.grid(row=5, column=1)
    zipcode_update = Entry(updater, width=30)
    zipcode_update.grid(row=6, column=1)
    salary_update = Entry(updater, width=30)
    salary_update.grid(row=7, column=1)

    # Textbox Labels
    f_name_label_update = Label(updater, text="First Name:")
    f_name_label_update.grid(row=0, column=0)
    l_name_label_update = Label(updater, text="Last Name:")
    l_name_label_update.grid(row=1, column=0)
    age_label_update = Label(updater, text="Age:")
    age_label_update.grid(row=2, column=0)
    address_label_update = Label(updater, text="Address:")
    address_label_update.grid(row=3, column=0)
    city_label_update = Label(updater, text="City:")
    city_label_update.grid(row=4, column=0)
    state_label_update = Label(updater, text="State:")
    state_label_update.grid(row=5, column=0)
    zipcode_label_update = Label(updater, text="Zipcode:")
    zipcode_label_update.grid(row=6, column=0)
    salary_label_udpate = Label(updater, text="Salary:")
    salary_label_udpate.grid(row=7, column=0)

    # Loop through results
    # This loops is structured beneath the labels to allow access
    for record in records:
        f_name_update.insert(0, record[0])
        l_name_update.insert(0, record[1])
        age_update.insert(0, record[2])
        address_update.insert(0, record[3])
        city_update.insert(0, record[4])
        state_update.insert(0, record[5])
        zipcode_update.insert(0, record[6])
        salary_update.insert(0, record[7])

    # Saves edited record
    btn_update_save = Button(updater, text="Save Updated Record", command=change_record)
    btn_update_save.grid(row=15, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


# Holds the basic template for user information
def credentials():
    pass


# Pulls user data and plots it onto graphs
"""The main idea of this is to implement a feature where the database's internal records
   are formatted into an easily readable file. This will take some time to figure out, but I believe it's
   doable within a few days of fiddling.
   - Select data from existing database
   - Store data to be formatted
   - Pull data and format it using matplotlib
   - Create a downloadable file for csv or png
   """
def user_data_graph():
    # Functions for the button widgets
    # Very basic text editor that can save files.
    # After reading some documents & re-watching tutorials, this makes more sense, but I want to revise it
    conn = sqlite3.connect("address_book.db")
    cr = conn.cursor()

    # Counts the number of time a name appears in database
    def plot_data():
        conn = sqlite3.connect("address_book.db")
        cr = conn.cursor()

        # Store data into list [20,30,40...]
        # DO NOT SELECT DISTINCT!!! - There needs to be equal number of elements in each list
        cr.execute("SELECT Age FROM addresses")
        age_query = cr.fetchall()
        age_list = []
        for a in age_query:
            age_list.append(a[0])

        # Store data into list [(20000),(30000),(40000)...]
        # DO NOT SELECT DISTINCT!!! - There needs to be equal number of elements in each list
        cr.execute("SELECT salary FROM addresses")
        salary_query = cr.fetchall()
        salary_list = []
        for s in salary_query:
            salary_list.append(s[0])

        # Plots the data (x, y)
        plt.plot(sorted(list(age_list)), sorted(list(salary_list)), marker='o')

        plt.title("Salary Over Time(Testing Database)")
        plt.xlabel("Age")
        plt.ylabel("Salary")

        plt.show()

    user_data_graph_window = Toplevel(master_window)
    user_data_graph_window.resizable(False, False)
    user_data_graph_window.title("User Data Visualizer")

    data_buttons = tk.Frame(user_data_graph_window, relief=tk.RIDGE, bd=2)
    data_buttons.grid(row=0, column=0)

    display_data = tk.Frame(user_data_graph_window, relief=tk.RIDGE, bd=2)
    display_data.grid(row=0, column=1)

    # Display first names in data frame
    cr.execute("SELECT DISTINCT first_name FROM addresses")
    first_names = cr.fetchall()
    f_name_label_data = Label(display_data, text=f"{first_names}", relief=tk.RAISED, bd=2, wraplength=300)
    f_name_label_data.grid(row=0, column=1, sticky="W", pady=4)

    # Display last names in data frame
    cr.execute("SELECT DISTINCT last_name FROM addresses")
    last_names = cr.fetchall()
    l_name_label_data = Label(display_data, text=f"{last_names}", relief=tk.RAISED, bd=2,wraplength=300)
    l_name_label_data.grid(row=1, column=1, sticky="W", pady=4)

    # Display ages in data frame
    cr.execute("SELECT Age FROM addresses")
    ages = cr.fetchall()
    ages_data = Label(display_data, text=f"{ages}", relief=tk.RAISED, bd=2, wraplength=300)
    ages_data.grid(row=2, column=1, sticky="W", pady=4)

    # Display address in data frame
    cr.execute("SELECT DISTINCT address FROM addresses")
    addresses = cr.fetchall()
    address_data = Label(display_data, text=f"{addresses}", relief=tk.RAISED, bd=2, wraplength=300)
    address_data.grid(row=3, column=1, sticky="W", pady=4)

    # Display Cities in data frame
    cr.execute("SELECT DISTINCT city FROM addresses")
    cities = cr.fetchall()
    city_data = Label(display_data, text=f"{cities}", relief=tk.RAISED, bd=2, wraplength=300)
    city_data.grid(row=4, column=1, sticky="W", pady=4)

    # Creates Window Showing Data For Areas in TN
    def display_median_income():
        plt.style.use("fivethirtyeight")
        tenn = pd.read_csv("Median_Household_Income.csv")
        plt.ylabel("Geography", rotation='vertical')
        plt.xlabel("Median Household Income")
        plt.barh(tenn.Geography[0:65], tenn.Income[0:65])
        plt.tight_layout()
        plt.show()

    # Display States in data frame
    cr.execute("SELECT DISTINCT state FROM addresses")
    states = cr.fetchall()
    states_data = Label(display_data, text=f"{states}", relief=tk.RAISED, bd=2, wraplength=300)
    states_data.grid(row=5, column=1, sticky="W", pady=4)

    # Display zipcodes
    cr.execute("SELECT DISTINCT zipcode FROM addresses")
    zipcodes = cr.fetchall()
    zipcode_data = Label(display_data, text=f"{zipcodes}", relief=tk.RAISED, bd=2, wraplength=200)
    zipcode_data.grid(row=6, column=1, sticky="W", pady=4)

    # Display Salaries
    cr.execute("SELECT DISTINCT salary FROM addresses")
    salary = cr.fetchall()
    salary_data = Label(display_data, text=f"{salary}", relief=tk.RAISED, bd=2, wraplength=200)
    salary_data.grid(row=7, column=1, sticky="W", pady=4)


    f_name_label = Button(data_buttons, text="Salary Graph Button", command=plot_data)
    f_name_label.grid(row=0, column=0, sticky="WE")
    l_name_label = Button(data_buttons, text="GRAPH SELECT", command=None)
    l_name_label.grid(row=1, column=0, sticky="WE")
    age_label = Button(data_buttons, text="CITIES", command=display_median_income)
    age_label.grid(row=2, column=0, sticky="WE")
    address_label = Button(data_buttons, text="YEARS", command=None)
    address_label.grid(row=3, column=0, sticky="WE")
    city_label = Button(data_buttons, text="MISC", command=None)
    city_label.grid(row=4, column=0, sticky="WE")
    state_label = Button(data_buttons, text="", command=None)
    state_label.grid(row=5, column=0, sticky="WE")
    zipcode_label = Button(data_buttons, text="", command=None)
    zipcode_label.grid(row=6, column=0, sticky="WE")
    ent_delete_label = Button(data_buttons, text="", command=None)
    ent_delete_label.grid(row=10, column=0, sticky="WE")
    salary_label = Button(data_buttons, text="", command=None)
    salary_label.grid(row=10, column=0, sticky="WE")

    conn.commit()
    conn.close()


"""THE FOLLOWING IS THE MASTER WINDOW FOR THE APPLICATION"""

# Window
master_window = tk.Tk()
master_window.title("Tristan's App Name")
width = master_window.winfo_screenwidth()
height = master_window.winfo_screenheight()
master_window.geometry("%dx%d" % (width, height))
style = ttk.Style(master_window)
style.theme_use('classic')

# Databases (sqlite3)
"""(9/10) Due to the nature of SQL being a major leap in this app's development, I will keep
SQL development notes in this section.

(9/10) I am very tired, but I have been productive! I think it's going to be worth it to 
focus on using the skills I learned from Codemy to develop my movie backlog database.

(9/16) After a brief break away from my coding marathon, I have returned to continue development
"""

# Create a database or connect to one
conn_AB = sqlite3.connect('address_book.db')  # Will create db if not already exists
# Create cursor(s)
cr_AB = conn_AB.cursor()

# Create Table
cr_AB.execute("""CREATE TABLE IF NOT EXISTS addresses (
        first_name text,
        last_name text,
        Age integer,
        address text,
        city text,
        state text,
        zipcode integer,
        salary integer
         )""")

frm_databases = Frame(master_window, relief=tk.RIDGE, bd=5, height=300)
frm_databases.grid(row=0, column=6, sticky="NE")

# Entry Boxes - Address Book
f_name = Entry(frm_databases, width=30)
f_name.grid(row=0, column=1, padx=0)
l_name = Entry(frm_databases, width=30)
l_name.grid(row=1, column=1)
age = Entry(frm_databases, width=30)
age.grid(row=2, column=1)
address = Entry(frm_databases, width=30)
address.grid(row=3, column=1)
city = Entry(frm_databases, width=30)
city.grid(row=4, column=1)
state = Entry(frm_databases, width=30)
state.grid(row=5, column=1)
zipcode = Entry(frm_databases, width=30)
zipcode.grid(row=6, column=1)
salary = Entry(frm_databases, width=30)
salary.grid(row=7, column=1)
ent_record_entry = Entry(frm_databases, width=30)
ent_record_entry.grid(row=13, column=1)

# Textbox Labels
f_name_label = Label(frm_databases, text="First Name:")
f_name_label.grid(row=0, column=0)
l_name_label = Label(frm_databases, text="Last Name:")
l_name_label.grid(row=1, column=0)
age_label = Label(frm_databases, text="Age:")
age_label.grid(row=2, column=0)
address_label = Label(frm_databases, text="Address:")
address_label.grid(row=3, column=0)
city_label = Label(frm_databases, text="City:")
city_label.grid(row=4, column=0)
state_label = Label(frm_databases, text="State:")
state_label.grid(row=5, column=0)
zipcode_label = Label(frm_databases, text="Zipcode:")
zipcode_label.grid(row=6, column=0)
salary_label = Label(frm_databases, text="Salary:")
salary_label.grid(row=7, column=0)
ent_delete_label = Label(frm_databases, text="Enter ID Number:")
ent_delete_label.grid(row=13, column=0, sticky="E")

# Submission Button
btn_submit = Button(frm_databases, text="Submit to Database", command=submit_address)
btn_submit.grid(row=16, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Query Button
btn_query = Button(frm_databases, text="Open Records", command=query)
btn_query.grid(row=8, column=0, columnspan=2, pady=2, padx=10, ipadx=137)

# Delete Button
btn_delete = Button(frm_databases, text="Delete Record", command=delete_record)
btn_delete.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Update Button
btn_update = Button(frm_databases, text="Update Record", command=update_record)
btn_update.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

conn_AB.commit()
conn_AB.close()

# Frame Widgets
frm_buttons = tk.Frame(master_window, relief=tk.RIDGE, bd=3)
frm_main_display = tk.Frame(master_window, relief=tk.RAISED, bd=5)
frm_calculator = tk.Frame(master_window, relief=tk.SUNKEN, bd=3)
frm_time = tk.Frame(master_window, relief=tk.SUNKEN, bd=3)

# Label Widgets
lbl_widget_welcome_message = tk.Label(frm_buttons, text="Tristan's Portfolio")
lbl_widget_message = tk.Label(frm_main_display)
lbl_widget_main_window = tk.Label(frm_main_display, text="Name:", underline=0)
lbl_widget_current_time = tk.Label(master_window, relief=tk.RAISED, font=("Arial", 25), bg="White", fg="Black")
timeclock()

# Button Widgets
btn_widget_message = tk.Button(frm_buttons, text="Click for message", width=15, height=1, command=click_me)
btn_widget_user_data = tk.Button(frm_buttons, text="User Info", width=15, height=1, command=user_data_graph)
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


"""Below are the geometry managements for widget locations
    THESE ARE NOT THE WIDGETS THEMSELVES"""

# Frame Grids
frm_buttons.grid(row=0, column=0, sticky="N")
frm_main_display.grid(row=0, column=1, sticky="N")
frm_calculator.grid(row=0, column=2, sticky="N")
frm_time.grid(row=0, column=3, sticky="N")



# Label Grids
lbl_widget_current_time.grid(row=0, column=0, sticky="N", padx=10, pady=900)
lbl_widget_welcome_message.grid(row=0, column=0, sticky="N", padx=25)
lbl_widget_message.grid(row=0, column=1, sticky="n")
lbl_widget_main_window.grid(row=0, column=1, sticky="N", padx=600, pady=frm_main_display.winfo_screenheight())

# Button Grids
btn_widget_message.grid(row=2, column=0, sticky="E", padx=0, pady=0)
btn_widget_user_data.grid(row=3, column=0, sticky="n", padx=0, pady=0)
btn_widget_calc.grid(row=4, column=0, sticky="n", padx=0, pady=0)
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

>>(9/17) First major update for about a week. I took some time off to regroup. Now that I have
had time to see how this app has evolved, as well as my basic skill set, the plan is to now
branch into more fundamentals of SQL. The main priority moving forward will be making major
additions by learning more intricate 

>> (9/26) I've shifted most of my notes to physcial ones, while doing more commenting and github documentation. This 
section has become redundant and I don't think it's needed much longer.
"""
