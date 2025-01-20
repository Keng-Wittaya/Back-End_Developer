import database
mycursor = database.mydb.cursor()

def selectdb(table):
    mycursor.execute(f'SELECT * FROM {table}')
    show = mycursor.fetchall()
    if len(show) <= 0:
        return False,None
    else:
        return True,show
    
def deletedb(table,id,id_name):
    sql = f"DELETE FROM {table} WHERE {id_name} = %s"
    val = (id,)
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None
    
def update(table,call,id_name,vall,id):
    sql = f'UPDATE {table} SET {call} = %s WHERE {id_name} = %s'
    val = (vall,id)
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None
    
def ins_ctgr(id,name):
    sql = " INSERT INTO categories VALUES ( %s , %s ) "
    val = ( id , name )
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None


def ins_order(od_id,usr_id,date,total,status,pd_id):
    sql = " INSERT INTO orders VALUES ( %s , %s , %s , %s , %s , %s ) "
    val = (od_id,usr_id,date,total,status,pd_id )
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None
    
def ins_product(pd_id,pd_name,dct,price,stock,ct_id):
    sql = " INSERT INTO products VALUES ( %s , %s , %s , %s , %s , %s ) "
    val = (pd_id,pd_name,dct,price,stock,ct_id)
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None

def ins_user( usr_id , usr_name , pw , email , us_role ):
    sql = " INSERT INTO users VALUES ( %s , %s , %s , %s , %s ) "
    val = ( usr_id , usr_name , pw , email , us_role )
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None
    