from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from sqlite3 import *


root = Tk()
root.title("Pesquisar Nome")
largura, altura = 750, 580
posx = (root.winfo_screenwidth() - largura) / 2
posy = (root.winfo_screenheight() - altura) / 2 - 25
root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
root.resizable(0, 0)


conn = None
conn = connect("data1.db")

curs = conn.cursor()

try:
    db = "create table student(id_name int primary key, name text)"
    curs.execute(db)

    if conn is not None:
        conn.close()

    conn = None
    conn = connect("data1.db")

    curs = conn.cursor()

    nomes = [
        'Pauline', 'Dexter', 'Melba', 'Roxanne', 'Mary', 'Andrew', 'Renata', 'Jonas', 'Adriele', 'Manoel', 'Carlos', 'Igor', 'Victor', 'Edson', 'Diego', 'Jesus', 'Airton', 'Norberto', 'Cleudes', 'Reginaldo', 'Rodrigo', 'Raphael', 'Jorge', 'Valdir', 'Laura', 'Roberto', 'Antonio', 'Edinaldo', 'Fabricio', 'Valdineia', 'Erica', 'Daniele', 'Vanessa']

    for i, j in enumerate(nomes):
        valor = f"insert into student values({i+1},'{j}')"
        curs.execute(valor)

    conn.commit()

except:
    pass

if conn is not None:
    conn.close()


def show():
    ws_ent.delete(0, END)
    ws_ent.focus()
    treeview.selection()
    conn = None
    try:
        conn = connect("data1.db")
        cursor = conn.cursor()
        db = "select * from student"
        cursor.execute(db)

        fetchdata = treeview.get_children()
        for elements in fetchdata:
            treeview.delete(elements)

        data = cursor.fetchall()
        for d in data:
            treeview.insert("", END, values=d)

        conn.commit()
    except Exception as e:
        showerror("Falha", e)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


def search():
    treeview.selection()
    fetchdata = treeview.get_children()
    for f in fetchdata:
        treeview.delete(f)
    conn = None
    try:
        conn = connect("data1.db")
        core = conn.cursor()
        db = "select * from student where name = '%s' "
        name = ws_ent.get()
        if (len(name) < 2) or (not name.isalpha()):
            showerror("Falha", "Nome inválido")
            show()
        else:
            core.execute(db % (name))
            data = core.fetchall()
            for d in data:
                treeview.insert("", END, values=d)

    except Exception as e:
        showerror("issue", e)

    finally:
        if conn is not None:
            conn.close()


def reset():
    show()


scrollbary = ttk.Scrollbar(root, orient=VERTICAL)
treeview = ttk.Treeview(root, columns=(
    "rollno", "name"), show='headings', height=15)
treeview.pack(padx=50, pady=20)
treeview.heading('rollno', text="ID", anchor=CENTER)
treeview.column("rollno", stretch=NO, width=100)
treeview.heading('name', text="Nome", anchor=CENTER)
treeview.column("name", stretch=NO)
scrollbary.config(command=treeview.yview)
scrollbary.place(x=526, y=40)
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")


ws_lbl = Label(root, text="Nome", font=('calibri', 12, 'normal'))
ws_lbl.place(x=290, y=488)
ws_ent = Entry(root,  width=20, font=('Arial', 15, 'bold'))
ws_ent.place(x=220, y=510)
ws_btn1 = Button(root, text='Pesquisar',  width=8, font=(
    'calibri', 12, 'normal'), command=search)
ws_btn1.place(x=480, y=510)
ws_btn2 = Button(root, text='Resetar',  width=8, font=(
    'calibri', 12, 'normal'), command=reset)
ws_btn2.place(x=600, y=510)


show()
root.mainloop()
