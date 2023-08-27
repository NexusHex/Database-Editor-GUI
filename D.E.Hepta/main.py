# D.E.Hepta - GUI Edition (v1.1)
# Read file 'patches.md' to get a better idea of what this program does
# This version of the code is based off of the Database Editor DecaFunction v1.6.6 (https://github.com/NexusHex/Database-Editor-Series/tree/main/Editors/1.6.6%20-%20DecaFunction)

import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
import csv

def startup():
    startWin = tk.Tk()
    startWin.title('Entering the Editor...')
    startWin.resizable(False, False)

    window_height = 200
    window_width = 400

    screen_width = startWin.winfo_screenwidth()
    screen_height = startWin.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    startWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    startup = tk.Label(startWin, text='Entering the Database Editor...', anchor='center', pady=200, font=('Arial', 20))
    startup.pack()

    startWin.after(2000, lambda: startWin.destroy())

    startWin.mainloop()

def main():
    #startup()

    mainWin = tk.Tk()
    mainWin.title("Database Editor HeptaFunction")
    mainWin.resizable(False, False)

    window_height = 600
    window_width = 930

    screen_width = mainWin.winfo_screenwidth()
    screen_height = mainWin.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    mainWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def add_data():
        def add_to_list():
            conn = sql.connect('database_store.db')
            with conn:
                c = conn.cursor()

                c.execute("INSERT INTO dataStore VALUES (:data)",
                        {'data' : add_data_entry.get()}
                        )
                add_data_entry.delete(0, 'end')
        
        addWin = tk.Tk()
        addWin.resizable(False, False)

        window_height = 160
        window_width = 250

        screen_width = addWin.winfo_screenwidth()
        screen_height = addWin.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        addWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
        addWin.title('Add values to the database')

        def close_win():
            addWin.destroy()

        frame = tk.LabelFrame(addWin, text='Add a new value(s) to the database', labelanchor='n')
        frame.grid(row=0, column=0, padx=10, pady=10)
        
        add_data_entry = tk.Entry(frame)
        add_data_entry.grid(row=1, column=1, padx=40, pady=20, columnspan=3)

        add_button = tk.Button(frame, text='Add data', command=add_to_list)
        add_button.grid(row=2, column=1, padx=20, pady=20)

        close = tk.Button(frame, text='Close Window', command=close_win)
        close.grid(row=2, column=2, padx=20, pady=20)
    
        addWin.mainloop()

    def clear_data():
        ask_del = messagebox.askyesno('Delete all values?', 'Would you like to clear the database of all values?')
        if ask_del == 1:
            conn = sql.connect('database_store.db')
            with conn:
                c = conn.cursor()
                c.execute("DELETE FROM dataStore")
            returning = messagebox.showinfo('Returning to Main Program', 'All data has been deleted, returning to main program')
        else:
            returning = messagebox.showinfo('Returning to Main Program', 'No data deleted, returning to main program')

    def close_app():
        mainWin.destroy()
    
    close_button_frame = tk.Frame(mainWin, width=100, height=30, highlightbackground='black', highlightthickness=1)
    close_button_frame.grid(row=0, column=0, padx=(20, 218), pady=20)
    close_program = tk.Button(close_button_frame, text='Close Program', command=close_app)
    close_program.grid(row=0, column=0, padx=10, pady=10)

    editor_title = tk.Label(mainWin, text='Database Editor HeptaFunction', font=('Arial', 20), anchor='center')
    editor_title.grid(row=0, column=1, columnspan=2, padx=(20, 40), pady=20)

    ver_frame = tk.Frame(mainWin, width=65, height=20, highlightbackground='black', highlightthickness=1)
    ver_frame.grid(row=0, column=4, padx=(0, 42), pady=20)
    program_ver = tk.Label(ver_frame, text='Version 1.1')
    program_ver.grid(padx=10, pady=10)

    data_frame = tk.Frame(mainWin, highlightbackground='black', highlightthickness=1)
    data_frame.grid(row=1, column=0, padx=(20, 0), pady=10)
    data_show = tk.Text(data_frame, wrap='word', width=40, height=10, font=('Arial', 10))

    conn = sql.connect('database_store.db')
    with conn:
        c = conn.cursor()
        db = c.execute("SELECT * FROM dataStore")

        for data in db:
            data = f'N/A | {data[0]}'
            data = data.replace('(', '').replace("'", "").replace(')', '').replace(',', '') # remove all of these characters "( ' ) ," from the output (just the words left)
            data_show.insert('end', f'{data}\n')

    data_show.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    scrollbar = tk.Scrollbar(data_frame, command=data_show.yview)
    scrollbar.grid(row=0, column=1, sticky='ns', padx=(0, 10), pady=10)

    #data_show.config(yscrollcommand=scrollbar.set)
    data_show['yscrollcommand'] = scrollbar.set

    def update_textbox():
        conn = sql.connect('database_store.db')
        with conn:
            c = conn.cursor()
            updated_db = c.execute("SELECT *, oid FROM dataStore")
            data_show.delete(1.0, 'end')

            for data in updated_db:
                data = f'{data[1]} | {data[0]}'
                data = data.replace('(', '').replace("'", "").replace(')', '').replace(',', '') # remove all of these characters "( ' ) ," from the output (just the words left)
                data_show.insert('end', f'{data}\n')

        data_show.after(1000, update_textbox)

    def del_vals():
        conn = sql.connect('database_store.db')
        with conn:
            c = conn.cursor()
            c.execute(f"DELETE FROM dataStore WHERE oid={str(del_vals_entry.get())}")
        del_vals_entry.delete(0, 'end')

    def save_to_csv():
        conn = sql.connect('database_store.db')
        with conn:
            c = conn.cursor()
            export = c.execute("SELECT * FROM dataStore")
        with open('database_output.csv', 'w', newline='') as file:
            convert = csv.writer(file)
            convert.writerows(export)
            messagebox.showinfo("Data Saved", "Data has been saved to a CSV (Excel) file. Check the directory of the program to see the exported data")

    del_vals_frame = tk.Frame(mainWin, highlightbackground='black', highlightthickness=1)
    del_vals_frame.grid(row=1, column=2, padx=(80, 20), pady=(20, 200))
    del_vals_header = tk.Label(del_vals_frame, text='Item Number')
    del_vals_header.grid(row=0, column=0, padx=10, pady=10)
    del_vals_entry = tk.Entry(del_vals_frame)
    del_vals_entry.grid(row=1, column=0, padx=20, pady=20)
    del_vals_button = tk.Button(del_vals_frame, text='Delete Value', command=del_vals)
    del_vals_button.grid(row=2, column=0, padx=20, pady=20)

    save_file_frame = tk.Frame(mainWin, highlightbackground='black', highlightthickness=1)
    save_file_frame.grid(row=2, column=0, padx=20, pady=20)
    save_file_button = tk.Button(save_file_frame, text='Save to CSV file', command=save_to_csv)
    save_file_button.grid(row=0, column=0, padx=10, pady=10)

    add_data_frame = tk.Frame(mainWin, highlightbackground='black', highlightthickness=1)
    add_data_frame.grid(row=2, column=1, sticky='w', padx=20, pady=20)
    add_data_button = tk.Button(add_data_frame, text='Add Data', command=add_data)
    add_data_button.grid(row=0, column=0, padx=10, pady=10)

    clear_data_frame = tk.Frame(mainWin, highlightbackground='black', highlightthickness=1)
    clear_data_frame.grid(row=2, column=2, sticky='e', padx=20, pady=20)
    clear_data_button = tk.Button(clear_data_frame, text='Clear Database', command=clear_data)
    clear_data_button.grid(row=0, column=0, padx=10, pady=10)

    update_textbox()
    mainWin.mainloop()

main()