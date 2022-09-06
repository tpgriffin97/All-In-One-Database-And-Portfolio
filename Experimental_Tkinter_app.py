# Experimental Tkinter app meant for playing around and
# developing an app naturally
import tkinter as tk


# Functions
def click_me():
    """Create a label widget upon being called.
    Bound to another widget using command="""
    lbl_message = tk.Label(frm_entries, text="I was clicked!")
    lbl_message.grid(row=3, column=1, sticky="NSEW")


def quit_program():
    """Stops the loop after function is called
    Bound to 'quit' button using command="""
    quit()


# Window
window = tk.Tk()
window.title("Tristan's App Name")

# Row and Column Configurations
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)
window.resizable(width=False, height=False)

# Frame Widgets
frm_buttons = tk.Frame(window, relief=tk.RIDGE, bd=3)
frm_entries = tk.Frame(window, relief=tk.RAISED, bd=3)

# Label Widgets
lbl_widget = tk.Label(frm_buttons, text="Entry Box 1:")
lbl_widget_message = tk.Label(frm_entries)

# Button Widgets
btn_widget_message = tk.Button(frm_buttons, text="Click for message", width=15, height=1, command=click_me)
btn_widget_storage = tk.Button(frm_buttons, text="Click for storage", width=15, height=1)
btn_widget_quit = tk.Button(frm_buttons, text="QUIT", width=15, height=1, command=quit_program)

# Entry Widgets
ent_widget_desc = tk.Entry(frm_entries)
ent_widget = tk.Entry(frm_entries)
ent_widget_store_message = tk.Entry(frm_entries)

# Frame Grids
frm_buttons.grid(row=0, column=0, sticky="N")
frm_entries.grid(row=0, column=1, sticky="N")

# Entry Grids
ent_widget.grid(row=0, column=1, sticky="N", padx=0, pady=0)
ent_widget_store_message.grid(row=1, column=1, sticky="N", padx=0, pady=0)
ent_widget_desc.grid(row=2, column=1, sticky="N", padx=0, pady=0)

# Label Grids
lbl_widget.grid(row=1, column=0, sticky="E")
lbl_widget_message.grid(row=0, column=1, sticky="E")

# Button Grids
btn_widget_message.grid(row=2, column=0, sticky="E", padx=0, pady=0)
btn_widget_storage.grid(row=3, column=0, sticky="E", padx=0, pady=0)
btn_widget_quit.grid(row=4, column=0, sticky="S", padx=0, pady=0)

window.mainloop()

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

"""
