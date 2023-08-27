# D.E.Penta - GUI Edition (v1.0)
# Read file 'patches.md' to get a better idea of what this program does
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

DB_CREATE = True # I have this in case the database gets deleted, but otherwise this remains True to stop there from being duplicate databases

def startup():
    if DB_CREATE == False:
        conn = sql.connect('database_store.db')
        c = conn.cursor()

        c.execute("CREATE TABLE dataStore (data text)")
        conn.commit()
        conn.close()
    else:
        pass

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
    startup()

    mainWin = tk.Tk()
    mainWin.title("Database Editor PentaFunction - v1.0")
    mainWin.resizable(False, False)

    window_height = 400
    window_width = 813

    screen_width = mainWin.winfo_screenwidth()
    screen_height = mainWin.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    mainWin.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def add_data():
        def add_to_list():
            conn = sql.connect('database_store.db')
            c = conn.cursor()

            c.execute("INSERT INTO dataStore VALUES (:data)",
                      {'data' : add_data_entry.get()}
                      )
            add_data_entry.delete(0, 'end')
            conn.commit()
            conn.close()
        
        addWin = tk.Tk() # 230 x 160
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
            c = conn.cursor()
            c.execute("DELETE FROM dataStore")
            conn.commit()
            conn.close()
            returning = messagebox.showinfo('Returning to Main Program', 'All data has been deleted, returning to main program')
        else:
            returning = messagebox.showinfo('Returning to Main Program', 'No data deleted, returning to main program')

    def close_app():
        mainWin.destroy()

    close_program = tk.Button(mainWin, text='Close Program', command=close_app)
    close_program.grid(row=0, column=0, padx=20, pady=20)

    editor_title = tk.Label(mainWin, text='Database Editor QuadFunction', font=('Arial', 20), anchor='center')
    editor_title.grid(row=0, column=1, columnspan=2, pady=20)

    program_ver = tk.Label(mainWin, text='Version 1.0')
    program_ver.grid(row=0, column=4, padx=20, pady=20)

    frame = tk.LabelFrame(mainWin, text='Your Database', labelanchor='n')
    frame.grid(row=1, column=1, padx=(100, 0), pady=10)

    data_show = tk.Text(frame, wrap='word', width=40, height=10, font=('Arial', 10))
    conn = sql.connect('database_store.db')
    c = conn.cursor()
    db = c.execute("SELECT * FROM dataStore")

    for data in db:
        data = str(data)
        data = data.replace('(', '').replace("'", "").replace(')', '').replace(',', '') # remove all of these characters "( ' ) ," from the output (just the words left)
        data_show.insert('end', f'{data}\n')

    data_show.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    scrollbar = tk.Scrollbar(frame, command=data_show.yview)
    scrollbar.grid(row=0, column=1, sticky='ns', padx=(0, 10), pady=10)

    data_show.config(yscrollcommand=scrollbar.set)

    def update_textbox():
        conn = sql.connect('database_store.db')
        c = conn.cursor()

        updated_db = c.execute("SELECT * FROM dataStore")
        data_show.delete(1.0, 'end')

        for data in updated_db:
            data = str(data)
            data = data.replace('(', '').replace("'", "").replace(')', '').replace(',', '') # remove all of these characters "( ' ) ," from the output (just the words left)
            data_show.insert('end', f'{data}\n')
        
        conn.commit()
        conn.close()

        data_show.after(1000, update_textbox)

    add_data_button = tk.Button(mainWin, text='Add Data', command=add_data)
    add_data_button.grid(row=2, column=1, sticky='w', padx=20, pady=20)

    clear_data_button = tk.Button(mainWin, text='Clear Database', command=clear_data)
    clear_data_button.grid(row=2, column=2, sticky='e', padx=20, pady=20)

    update_textbox()
    mainWin.mainloop()

main()
