import mysql.connector

class dbman:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="database"
  )
  mycursor = mydb.cursor()
  def checkexam(self,user_id):
    print(user_id)
    sql2 = "SELECT * FROM reserved_exams WHERE user_id = %s  AND done ='2'"
    adr = (user_id,)
    self.mycursor.execute(sql2, adr)
    myresult2 = self.mycursor.fetchall()
    if myresult2:
      return True

###################################
  def checkemail(self, email):


    sql = "SELECT * FROM users WHERE email =%s"
    email = (email,)
    self.mycursor.execute(sql,email)

    myresult = self.mycursor.fetchall()

    if myresult:
      user_id = myresult[0][0]
      return user_id
##################################
  def checknational_id(self, national_id):


    sql = "SELECT * FROM users WHERE national_id =%s"
    national_id = (national_id,)
    self.mycursor.execute(sql,national_id)

    myresult = self.mycursor.fetchall()

    if myresult:
      user_id = myresult[0][0]
      return user_id
#######################################
  def canHaveOne(self,email,national_id):
    isokay = False
    if email is not False:
      user_id = self.checkemail(email)
      if user_id :
        isokay = self.checkexam( user_id)
    if national_id is not False:
      user_id = self.checknational_id(national_id)
      if user_id:
        isokay = self.checkexam(user_id)
    return isokay



#mw = dbman()
#print( mw.canHaveOne('abdullahsoultan525@gmail.comxx','284072601ss03804'))
