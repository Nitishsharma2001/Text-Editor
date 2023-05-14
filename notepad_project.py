from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
import win32api
import webbrowser
# Title of window.
root = Tk(className="Notepad")

# Giving dimensions||size to create a window.
root.geometry("400x400")

# Creating area for typing in Notepad.
# It helps for typing any number of lines.
textpad = scrolledtext.ScrolledText(root, width=800, height=580, undo=True)

global selected
selected = False

root.iconbitmap("C:\\Users\\nitis\\Downloads\\notes.ico")


# Creating Functions.
def work():
    print("this work!")


# Creating a funtion for Menubar option 'Open' inside 'File'.
def open_command():
    # opening a file in binary mode for reading 'rb'.
    file = filedialog.askopenfile(parent=root, mode='rb', title='select a file')

    # Checking whether user select a file or not if not then it return nothing.
    if file != None:
        # Reading content and copying text to contents string_variable.
        contents = file.read()

        # Inserting content to textpad.
        textpad.insert('1.0', contents)

        # Closing a File(good practice).
        file.close()


# Creating a function for menubar option 'Save' inside 'File' option.
def save_command():
    # 'w' mode is used to write in a file.
    file = filedialog.asksaveasfile(mode='w')

    # Checking File exsist or not!.
    if file != None:
        # collecting data  in 'data' which is being written by user in textpad.
        data = textpad.get('1.0', END + '-1c')

        # writeing data to save updated file.
        file.write(data)

        # Closing a File(good practice).
        file.close()


# Creating a function for menubar option 'Saveas' inside 'File' option
def saveas_command():
    # Writing in a file.
    file = filedialog.asksaveasfile(mode='w')

    # Checking whether file exsist or not.
    if file != None:
        contents = file.writelines()
        # Insert content into textpad.
        textpad.insert('1.0', contents)
        file.close()


# Creating a function for exit.
def exit_command():
    if messagebox.askokcancel("Quit", "do you really want to quit?"):
        # Destroying window named as 'root'.
        root.destroy()


def about_command():
    label = messagebox.showinfo("about", "Created by Nitish")
    menu = Menu(root)
    root.config(menu=menu)


def delete_text(e):
    if textpad.selection_get():
        textpad.delete("sel.first", "sel.last")


def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if textpad.selection_get():
            selected = textpad.selection_get()
            textpad.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e):
    global selected

    # check to see if we used keyboard shortcuts or not.
    if e:
        selected = root.clipboard_get()
    if textpad.selection_get():
        selected = textpad.selection_get()
        # clear the clipboard and then append
        root.clipboard_clear()
        root.clipboard_append(selected)


def paste_text(e):
    global selected
    # check to see if keyboard shortcut is used
    if e:
        selected = root.clipboard_get()
    if selected:
        position = textpad.index(INSERT)
        textpad.insert(position, selected)


def newFile(e):
    root.title("Untitled - Notepad")
    file = None
    textpad.delete(1.0, END)
    file = filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])


def print_file(e):
    # Ask for file (Which you want to print)
    file_to_print = filedialog.askopenfilename(
        initialdir="/", title="Select file",
        filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

    if file_to_print:
        # Print Hard Copy of File
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)

def view_help(e):
     webbrowser.open('https://docs.google.com/document/d/1tTE2w1Mfkz3NTFXzvFjK7X4F1FCQEFkM/edit?usp=sharing&ouid=100354182388395617989&rtpof=true&sd=true')

# Creating menubaras option.
menu1 = Menu(root)
root.config(menu=menu1)
Submenu = Menu(menu1)
Editmenu = Menu(menu1)
Helpmenu = Menu(menu1)

# Comprising all menubar options with functions decribed above.
menu1.add_cascade(label="File", menu=Submenu)
menu1.add_cascade(label="Edit", menu=Editmenu)

menu1.add_cascade(label="Help", menu=Helpmenu)
Submenu.add_command(label="new", command=lambda: newFile(False))
Submenu.add_command(label="open...", command=open_command)
Submenu.add_command(label="save", command=save_command)
Submenu.add_command(label="save as", command=saveas_command)
Submenu.add_separator()
Submenu.add_command(label="print...", command=lambda: print_file(False))
Submenu.add_command(label="Exit", command=exit_command)
Editmenu.add_command(label="Undo", command=textpad.edit_undo)
Editmenu.add_command(label="Redo", command=textpad.edit_redo)
Editmenu.add_command(label="Cut", command=lambda: cut_text(False))
Editmenu.add_command(label="Copy", command=lambda: copy_text(False))
Editmenu.add_command(label="paste", command=lambda: paste_text(False))
Editmenu.add_command(label="Delete", command=lambda: delete_text(False))


Helpmenu.add_command(label="View Help", command=lambda:view_help(False))
Helpmenu.add_command(label="About Notepad", command=about_command)

# root.bind('<control-key-x>',cut_text)
# root.bind('<control-key-c>',copy_text)
# root.bind('<control-key-v>',paste_text)
# Packs all the widgets one after the other in a window.
textpad.pack()

# Tells Python to run the Tkinter event loop.
root.mainloop()
