import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = tk.Tk()
root.title('Murunga.com - Learn to code')
# root.iconbitmap('c:/gui/murunga.ico')
root.geometry("400x400")

# Create table
c.execute(""" CREATE TABLE addresses(
                first_name TEXT,
                last_name TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                zipcode INTEGER)""")
# Create Submit Function For database
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a Cursor -  to send to the database and come out with some stuff
    c = conn.cursor() 
    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid="+delete_box.get())
    delete_box.delete(0,END)
    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()
    
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a Cursor -  to send to the database and come out with some stuff
    c = conn.cursor() 
    # Insert into the table
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
             {
                'f_name':f_name.get(),
                 'l_name':l_name.get(),
                 'address':address.get(),
                 'city':city.get(),
                 'state':state.get(),
                 'zipcode':zipcode.get()
             })
    
    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()
    # clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

# Create a Query Button
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create a Cursor -  to send to the database and come out with some stuff
    c = conn.cursor() 
    # Query the database
    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    
    print_records=""
    for record in records:
        print_records += str(record[0])+" "+str(record[1])+"  "+str(record[6]) + "\n"
        
    query_label = Label(root,text=print_records)
    query_label.grid(row=11,column=0,columnspan=2)
    
    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()

# Create Text Boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
address = Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city = Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state = Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)
delete_box = Entry(root,width=30)
delete_box.grid(row=9,column=1,pady=5)
# Create Text Box Labels

f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))
l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)
address_label = Label(root,text="Address")
address_label.grid(row=2,column=0)
city_label = Label(root,text="City")
city_label.grid(row=3,column=0)
state_label = Label(root,text="State")
state_label.grid(row=4,column=0)
zipcode_label = Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)
delete_box_label = Label(root,text="Delete ID")
delete_box_label.grid(row=9,column=0,pady=5)

# Create Submit Button
submit_btn = Button(root,text="Add Record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
# Create a Query Butto
query_btn = Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=132)
# Create a Delete button
delete_btn = Button(root,text="Delete Records",command=delete)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=127)
root.mainloop()