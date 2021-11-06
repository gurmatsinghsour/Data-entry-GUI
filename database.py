import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *


#backend
def Delete(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(9, select['PatientId'])
    e2.insert(9, select['Name'])
    e3.insert(9, select['NutritionalDefficiency'])
    e4.insert(9, select['Age'])



def Add():
    patientId = e1.get()
    patientName = e2.get() 
    nutrition = e3.get()
    fee = e4.get()


    mysqldb = mysql.connector.connect(host='localhost', user = 'root', password='', database='pbl')
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO nutritionalsecurity (PatientId, Name, NutritionalDefficiency, Age) VALUES (%s, %s, %s, %s)"
        val = (patientId, patientName, nutrition, fee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record inserted sucessfully....")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    patientId = e1.get()
    patientName = e2.get()
    nutrition = e3.get()
    age = e4.get()
    mysqldb = mysql.connector.connect(host='localhost', user = 'root', password='', database='pbl')
    mycursor=mysqldb.cursor()

    try:
        sql = "Update nutritionalsecurity set Name = %s, NutritionalDefficiency = %s, Age = %s where PatientId = %s"
        val = (patientName, nutrition, age, patientId)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record updated sucessfully!")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    patientId = e1.get()

    mysqldb = mysql.connector.connect(host='localhost', user = 'root', password='', database='pbl')
    mycursor=mysqldb.cursor()

    try:
        sql = "delete from nutritionalsecurity where PatientId = %s"
        val = (patientId,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record deleted sucessfully!")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

        
def show():
    mysqldb = mysql.connector.connect(host='localhost', user = 'root', password='', database='pbl')
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT PatientId, Name, NutritionalDefficiency, Age FROM NutritionalSecurity")
    records = mycursor.fetchall()
    print(records)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))

#  GUI

root = Tk()
root.geometry("825x500")
root.resizable(False, False)
root.config(bg="lightgreen")
global e1
global e2
global e3

tk.Label(root, text="Database", fg = "black", font=(None, 38)).place(x=400, y=5)
Label(root, text="Patient ID: ").place(x=10, y=10)
Label(root, text="Name: ").place(x=10, y=40)
Label(root, text="Nutritional Defficiency: ").place(x=10, y=70)
Label(root, text="Age: ").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=150, y=10)    
    
e2 = Entry(root)
e2.place(x=150, y=40)

e3 = Entry(root)
e3.place(x=150, y=70)


e4 = Entry(root)
e4.place(x=150, y=100)

Button(root, text="Add", command = Add, height=3, width=13).place(x=30, y=130)
Button(root, text="Update", command = update, height=3, width=13).place(x=140, y=130)
Button(root, text="Delete", command = delete, height=3, width=13).place(x=250, y=130)

cols = ('PatientId', 'Name', 'NutritionalDefficiency', 'Age')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column = 0, columnspan = 2)
    listBox.place(x = 10, y=200)

show()
listBox.bind('<Double-Button-1>', Delete)

if __name__ == "__main__":
    root.mainloop()

    