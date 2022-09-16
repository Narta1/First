from tkinter import *
from PIL import Image,ImageTk
import sqlite3

root=Tk()
root.geometry("500x500")
#databases

'''
#create table
c.execute("""CREATE TABLE adresses(
    first_name text,
    last_name text,
    zip_code integer

) """)
'''

def update():
    #create a database or connect to one
    conn=sqlite3.connect('adress_book.db')
    #create cursor
    c=conn.cursor()
    record_id=delete_en.get()
    c.execute("""UPDATE adresses SET 
    first_name=:first,
    last_name=:last,
    zip_code=:zip
    WHERE oid=:oid""",
    {'first':f_name_editor.get(),'last':l_name_editor.get(),'zip':zip_code_editor.get(),'oid': record_id
    
    
    
    }




    )

    
    #comit changes
    conn.commit()
    #close connetction
    conn.close()

    editor.destroy()

    







#create function to edit a record
def edit():
    global editor
    
    editor=Tk()
    editor.geometry("500x500")

    

    #create a database or connect to one
    conn=sqlite3.connect('adress_book.db')
    #create cursor
    c=conn.cursor()
    record_id=delete_en.get()
    

    #qyery the database
    sql_select_query="SELECT * FROM adresses WHERE oid= ?"
    c.execute(sql_select_query, (record_id,))
    records=c.fetchall()
    #create global
    global f_name_editor
    global l_name_editor
    global zip_code_editor

    


    #create boxes
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=10)
    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20,pady=10)
    zip_code_editor=Entry(editor,width=30)
    zip_code_editor.grid(row=2,column=1,padx=20,pady=10)
    
    #create labels
    f_label_editor=Label(editor,width=30,text="name")
    f_label_editor.grid(row=0,column=0)
    l_label_editor=Label(editor,width=30,text="surname")
    l_label_editor.grid(row=1,column=0)
    z_label_editor=Label(editor,width=30,text="zipcode")
    z_label_editor.grid(row=2,column=0)


    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        zip_code_editor.insert(0,record[2])

    #create submit button
    btn=Button(editor,text='Update',command=update)
    btn.grid(row=6,column=0,columnspan=20,padx=10,pady=10)
    
    

    



#Create function to delete a record
def delete():
    #create a database or connect to one
    conn=sqlite3.connect('adress_book.db')
    #create cursor
    c=conn.cursor()

    c.execute("DELETE FROM adresses WHERE oid="+delete_en.get())
    delete_en.delete(0,END)

    #comit changes
    conn.commit()
    #close connetction
    conn.close()






def submit():
    #create a database or connect to one
    conn=sqlite3.connect('adress_book.db')
    #create cursor
    c=conn.cursor()

    #insert into table
    c.execute("INSERT INTO adresses VALUES(:f_name,:l_name,:zip_code)",
    {
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'zip_code':zip_code.get()

    }
    
    )

    #comit changes
    conn.commit()
    #close connetction
    conn.close()




    
    f_name.delete(0,END)
    l_name.delete(0,END)
    zip_code.delete(0,END)

def query():
    #create a database or connect to one
    conn=sqlite3.connect('adress_book.db')
    #create cursor
    c=conn.cursor()

    #qyery the database
    c.execute("SELECT *,oid FROM adresses")
    records=c.fetchall()
    print_records=''
    #print(records)
    #for name,surname,zip,key in records:
     #   lbl=Label(root,text=name).grid(row=6,column=1)
      #  lbl1=Label(root,text=surname).grid(row=7,column=1)
       # lbl2=Label(root,text=zip).grid(row=8,column=1)
        #lbl3=Label(root,text=key).grid(row=9,column=1)
    for record in records:
        print_records+=str(record[0])+" "+str(record[1])+" "+ str(record[3])+ "\n"
    query_label=Label(root,text=print_records)
    query_label.grid(row=6,column=1)










    #comit changes
    conn.commit()
    #close connetction
    conn.close()
    return 


#create boxes
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=10)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20,pady=10)
zip_code=Entry(root,width=30)
zip_code.grid(row=2,column=1,padx=20,pady=10)
delete_en=Entry(root,width=30)
delete_en.grid(row=8,column=1,padx=20,pady=10)
#create labels
f_label=Label(root,width=30,text="name")
f_label.grid(row=0,column=0)
l_label=Label(root,width=30,text="surname")
l_label.grid(row=1,column=0)
z_label=Label(root,width=30,text="zipcode")
z_label.grid(row=2,column=0)
id_label=Label(root,width=30,text="Select ID number")
id_label.grid(row=8,column=0)

#create submit button
btn=Button(root,text='Submit',command=submit)
btn.grid(row=4,column=0,columnspan=20,padx=10,pady=10)

#create a query button
qyer=Button(root,text="show records",command=query)
qyer.grid(row=4,column=1,padx=20,pady=10,columnspan=2)

dele=Button(root,text="delete",command=delete)
dele.grid(row=9,column=0,padx=20,pady=10,columnspan=2,ipadx=137)
edit=Button(root,text="edit",command=edit)
edit.grid(row=10,column=0,padx=20,pady=10,columnspan=2,ipadx=137)



root.mainloop()