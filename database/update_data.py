#
from libs.db.dbconn import getconn

def update_data():
    conn=getconn()
    cur=conn.cursor()
    sql="update member set age=35 where name='이몽룡'"
    cur.execute(sql)

    conn.commit()
    conn.close()

if __name__=='__main__':
    update_data()