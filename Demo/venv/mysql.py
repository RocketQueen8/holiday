import pymysql
db=pymysql.connect(
    host="106.14.249.165",
    port=3306,
    user="root",
    passwd="zlhr0SO1Dd",
    db="cash_loan",
    charset="utf8"
)
cur=db.cursor()
sql="select * from cash_app WHERE name='KreditNow';"
res=cur.execute(sql)
db.commit()
print(type(res))
print(res)