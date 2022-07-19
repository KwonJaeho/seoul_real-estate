import pandas as pd
import pymysql as SQL
import numpy as np
from datetime import datetime
##csv 가져오기
def read_csv():
    csv = pd.read_csv("./test1.csv",encoding='utf_8',low_memory=False)
    csv = csv.replace({np.nan:None})
    return csv
## DB연결
def DB_connect():
    conn = SQL.connect(host='IP입력',user='사용자',password='비밀번호',db='DB명',charset='utf8',port=포트번호)
    return conn
## 건물 테이블 데이터 삽입
def insert_data_building(conn):
    csv = read_csv()
    csv1 = csv['자치구코드']
    csv2 = csv['자치구명']
    csv3 = csv['법정동명']
    csv4 = csv['본번']
    csv5 = csv['부번']
    csv6 = csv['건물명']
    csv7 = csv['물건금액(만원)']
    csv8 = csv['건물면적(㎡)']
    csv9 = csv['토지면적(㎡)']
    csv10 = csv['층']
    csv11 = csv['건축년도']
    csv12 = csv['건물용도']
    
    cur = conn.cursor()
    sql = """INSERT INTO 건물 (자치구코드,자치구명,법정동명,본번,부번,건물명,물건금액,건물면적,토지면적,층,건축년도,건물용도)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    for i in range(len(csv)):
        cur.execute(sql,(csv1[i],csv2[i],csv3[i],csv4[i],csv5[i],csv6[i],csv7[i],csv8[i],csv9[i],csv10[i],csv11[i],csv12[i]))

    conn.commit()
## 지도 테이블 데이터 삽입
def insert_data_map(conn):
    csv = read_csv()
    csv1 = csv['자치구코드']
    csv2 = csv['자치구명']
    csv3 = csv['본번']
    csv4 = csv['부번']
    csv5 = csv['건물명']
    csv6 = csv['x']
    csv7 = csv['y']
    cur = conn.cursor()
    sql = "INSERT INTO 지도(자치구코드,자치구명,본번,부번,건물명,위도,경도) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    for i in range(len(csv)):
        cur.execute(sql,(csv1[i],csv2[i],csv3[i],csv4[i],csv5[i],csv6[i],csv7[i]))
    conn.commit()
## 실거래 테이블 데이터 삽입
def insert_data_deal(conn):
    csv = read_csv()
    
    csv1 = csv['접수연도']
    csv2 = csv['본번']
    csv3 = csv['부번']
    csv4 = csv['건물명']
    csv5 = csv['계약일']
    csv6 = csv['물건금액(만원)']
    cur = conn.cursor()
    sql = "INSERT INTO 실거래(접수년도,본번,부번,건물명,계약일,물건금액) VALUES(%s,%s,%s,%s,%s,%s)"
    for i in range(len(csv)):
        cur.execute(sql,(csv1[i],csv2[i],csv3[i],csv4[i],csv5[i],csv6[i]))
    conn.commit()
##메인코드
def main():
    conn = DB_connect()
    print('연결완료')
    insert_data_building(conn)
    insert_data_map(conn)
    insert_data_deal(conn)
    conn.close()
    print('연결해제')
    
if __name__=="__main__":
    print('start time:',str(datetime.now())[10:19])
    main()
    print('end time:',str(datetime.now())[10:19])
    
