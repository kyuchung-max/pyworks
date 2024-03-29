#mydb 에 member table 생성
from libs.db.dbconn import getconn

def create_table():
    conn = getconn()    #dbconn module에서 getconn 객체 생성
    cur = conn.cursor() #db 작업 객체

    sql = '''
        create table member(
            name char(20),
            age int
        
        )
    
    
    '''

    cur.execute(sql)

    conn.commit()   #트랜잭션 완료(수행)
    conn.close()    #네트워크 종료
if __name__=='__main__':
    create_table()