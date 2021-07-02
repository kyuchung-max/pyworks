#특정 회원 검색
from libs.db.dbconn import getconn

def select_one(num):
    conn=getconn()
    cur=conn.cursor()

    sql="select * from member where name='성춘향'"
    cur.execute(sql)
    print('이름으로 검색')
    #rs=cur.fetchmany(num)
    rs=cur.fetchone()
    '''
    for i in rs:
        print(i)
    '''
    print(rs)
    conn.close()

if __name__=='__main__':
    select_one(1)