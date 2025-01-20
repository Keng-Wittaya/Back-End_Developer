import tkinter 
import database
mycursor = database.mydb.cursor()

def selectdb():
    table = table_input.get()
    mycursor.execute(f'SELECT * FROM {table}')
    show = mycursor.fetchall()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,output_label.configure(text=show)

def deletedb():
    table = table_input.get()
    id = id_input.get()
    sql = f"DELETE FROM {table} WHERE user_id = %s"
    val = (id,)
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None


program = tkinter.Tk()
program.title('โปรแกรมจัดการข้อมูล')
program.minsize(width=400,height=400)

program_label = tkinter.Label(master=program , text="ร")
program_label.pack()

table_input = tkinter.Entry(master=program)
table_input.pack()

program_label = tkinter.Label(master=program , text="พิมพ์IDที่ต้องการ")
program_label.pack()

id_input = tkinter.Entry(master=program)
id_input.pack()

search_button = tkinter.Button(master=program,text='ค้นหา',command=selectdb)
search_button.pack()

del_button = tkinter.Button(master=program,text='ลบ',command=deletedb)
del_button.pack()

output_label = tkinter.Label(master=program,text='ผลการค้นหา')
output_label.pack()

program.mainloop()
