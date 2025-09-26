import random
print("-----------------------------------------------------------------")
print("|                  WELCOME TO CHEMISTRY WALLAH                  |")
print("-----------------------------------------------------------------")
print("          1. LOGIN                         2. SIGN UP             ")
i = True 
while i == True:
    query1 = int(input("how would you like to start? "))
    def login():
        import pymysql as connector
        db = connector.connect(host = 'localhost',user = 'root',password = 'password',database = 'chemwallah')
        c = db.cursor()
        i = True
        while i == True:
            user = input("enter your username: ")
            password = input("enter your password: ")
            try:
                c.execute("select A.name, B.user from record A, users B where B.user = '%s' and B.password = '%s' and A.user = B.user"%(user, password))
                data = c.fetchall()
                print('logged in as ',data[0][1])
                i = False
                return user 
            except: 
                print('userid and password is incorrect')
                i = True
    def signup():
        import pymysql as connector
        db = connector.connect(host = 'localhost',user = 'root',password = 'password',database = 'chemwallah')
        c = db.cursor()
        name = input('enter your name: ')
        clas = int(input("enter your class: "))
        phone = int(input("enter your phone number: "))
        guardian = input('enter your guardian name: ')
        if clas == 11:
            sub = input("enter your subjects(P/C/M/B): ")
        elif clas == 12:
            sub = input("enter your subjects(P/C/M/B): ")
        else: 
            sub = 'non'
        user = "CWS"+name+str(random.randint(0, 1000))
        k = 0                
        while k == 0:
            newpassword = input("create new password: ")
            confirm = input("confirm password: ")
            if newpassword == confirm :
                password = newpassword
                k = 1
            else:
                print("passwords don't match")
        c.execute("insert into users values('%s', '%s')"%(user,password))
        c.execute("insert into record values('%s', '%s', %s, '%s', NULL, NULL, %s, '%s')"%(user,name,phone,guardian,clas,sub))
        db.commit()
        print('logged in as ',user)
        return user
    if query1 == 1:
        user = login()
        i = False

    elif query1 == 2:
        i = False
        user = signup()
    

#---------------------------------------------------------------------------------------------------

import pymysql as connector
db = connector.connect(host = 'localhost',user = 'root',password = 'password',database = 'chemwallah')
c = db.cursor()
c.execute("select * from record where user = '%s'"%(user,))
data = c.fetchall()
name = data[0][1]
print("welcome to chem wallah, "+name)
while True:
    c = db.cursor()
    c.execute("select * from record where user = '%s'"%(user,))
    data = c.fetchall()
    name = data[0][1]
    data = data[0]
    print("+--------------------------------------------------------+")
    print("|                                                        |")
    print("|   (1)  View Profile                                    |")
    print("|   (2)  View Available Courses                          |")
    print("|   (3)  Enroll For A Course                             |")
    print("|   (4)  View Batch                                      |")
    print("|   (5)  Change Personal Details                         |")
    print("|   (6)  Give Feedback                                   |")
    print("|   (7)  EXIT                                            |")
    print("|                                                        |")
    print("+--------------------------------------------------------+")
    query = int(input("> "))
    if query == 1:
        print("-------------------------------------")
        print(f"UserName     :  {data[0]}")
        print(f"Name         :  {data[1]}")
        print(f"Batch        :  {data[5]}")
        print(f"Phone Number :  {data[2]}")
        print(f"Guardian     :  {data[3]}")
        print(f"class        :  {data[6]}")
        print(f"Course       :  {data[4]}")
    elif query == 2:
        clas = data[-2]
        if clas == 9: 
            print("PRARAMBH            Rs.5000/year")
            print("PRARAMBH 2.0        Rs.4500/year")
            print("PRARAMBH(offline)   Rs.50000/year")
            print("(for more details contact us)")
        elif clas == 10: 
            print("ARAMBH            Rs.5000/year")
            print("ARAMBH 2.0        Rs.4500/year")
            print("ARAMBH(offline)   Rs.50000/year") 
            print("(for more details contact us)")
        elif clas == 11 and data[-1].upper() == 'PCM': 
            print("ARJUNA JEE            Rs.6000/year")
            print("ARJUNA JEE 2.0        Rs.5500/year")
            print("ARJUNA JEE(offline)   Rs.70000/year")
            print("MANZIL FASTRACK(JEE)  Rs.4000/year") 
            print("(for more details contact us)")  
        elif clas == 11 and data[-1].upper() == 'PCB': 
            print("ARJUNA NEET            Rs.6000/year")
            print("ARJUNA NEET 2.0        Rs.5500/year")
            print("ARJUNA NEET(offline)   Rs.70000/year")
            print("MANZIL FASTRACK(NEET)  Rs.4000/year") 
            print("(for more details contact us)")
        elif clas == 12 and data[-1].upper() == 'PCB': 
            print("LAKSHYA NEET            Rs.6000/year")
            print("LAKSHYA NEET 2.0        Rs.5500/year")
            print("LAKSHYA NEET(offline)   Rs.70000/year")
            print("MANZIL FASTRACK(NEET)   Rs.4000/year") 
            print("(for more details contact us)")
        elif clas == 12 and data[-1].upper() == 'PCM': 
            print("LAKSHYA JEE            Rs.6000/year")
            print("LAKSHYA JEE 2.0        Rs.5500/year")
            print("LAKSHYA JEE(offline)   Rs.70000/year")
            print("MANZIL FASTRACK(JEE)   Rs.4000/year") 
            print("(for more details contact us)") 

    elif query == 3:
        clas = data[-2]
        course = input('In which course do you want to enroll? (enter full name): ')
        c.execute("update record set course = '%s' where user = '%s'"%(course,user))
        db.commit()
        batches = [101,102,103]
        batch = None
        if clas == 9:
            if course.lower() == 'prarambh':
                batch = "PR"+"101"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
                c.execute('insert into pr101 values(NULL,"%s", %s)'%(user,data[2]))
                db.commit()
            elif course.lower()=='prarambh 2.0':
                batch = 'PR'+"101_2"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
                c.execute('insert into pr101_2 values(NULL, "%s", %s)'%(user,data[2]))
                db.commit()
            elif course.lower()=='prarambh offline':
                batch = 'PR'+str(random.choice(batches))+"_OFFLINE"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
                c.execute('insert into pr101_offline values(NULL, "%s", "%s")'%(user,data[2]))
                db.commit()
        elif clas == 10:
            if course.lower() == 'aramabh':
                batch = "AR101"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
                c.execute('insert into ar101 values(NULL, "%s", %s)'%(user,data[2]))
                db.commit()
            elif course.lower() == 'aramabh 2.0':
                batch = 'AR101_2' 
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
                c.execute('insert into ar101_2 values(NULL, "%s", %s)'%(user,data[2]))
                db.commit()
            elif course.lower() == 'aramabh offline':
                batch = 'AR'+"101_OFFLINE"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
                c.execute('insert into ar101_offline values(NULL, "%s", %s)'%(user,data[2]))
                db.commit()
        elif clas == 11 and data[-1].upper() == 'PCM':
            if course.lower() == 'arjuna jee':
                batch = "AJ101"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
            elif course.lower() == 'arjuna jee 2.0':
                batch = 'AJ' + "101_2"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
            elif course.lower() == 'arjuna jee offline':
                batch = 'AJ' + "101_OFFLINE"
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
            elif course.lower() == 'manzil fastrack(jee)':
                batch = 'MJ101'
                c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
                db.commit()
                c.execute('insert into %s values(NULL, "%s", %s)'%(batch,user,data[2]))
                db.commit()
        elif clas == 11 and data[-1].upper() == 'PCB':
            if course.lower() == 'arjuna neet':
                batch = "AN101"
            elif course.lower() == 'arjuna neet 2.0':
                batch = 'AN101'+"_2"
            elif course.lower() == 'arjuna neet offline':
                batch = 'AN' +"101_OFFLINE"
            elif course.lower() == 'manzil fasttrack(neet)':
                batch = 'MN101'  
            c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
            db.commit()
            c.execute('insert into %s values(NULL, "%s", "%s")'%(batch,user,data[2]))
            db.commit()

        elif clas == 12 and data[-1].upper() == 'PCM':
            if course.lower() == 'lakshya jee':
                batch = "LJ101"
            elif course.lower() == 'lakshya jee 2.0':
                batch = 'LJ' + "101_2"
            elif course.lower() == 'lakshya jee offline':
                batch = 'LJ' + "101_OFFLINE"
            elif course.lower() == 'manzil fasttrack(jee)':
                batch = 'MJ' + str(random.choice(batches))
            c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
            db.commit()
            c.execute('insert into %s values(NULL, "%s", "%s")'%(batch,user,data[2]))
            db.commit()

        elif clas == 12 and data[-1].upper() == 'PCB':
            if course.lower() == 'lakshya neet':
                batch = "LN101"
            elif course.lower() == 'lakshya neet 2.0':
                batch = 'LN101' + "_2"
            elif course.lower() == 'lakshya neet offline':
                batch = 'LN101' + "_OFFLINE"
            elif course.lower() == 'manzil fasttrack(neet)':
                batch = 'MN101'
            c.execute("update record set batch = '%s' where user = '%s'"%(batch,user))
            db.commit()
            c.execute('insert into %s values(NULL, "%s", "%s")'%(batch,user,data[2]))
            db.commit()
        
        else:
            print('no such batch available')

    elif query == 4:
        c.execute('select batch from record where user = "%s"'%(user,))
        d = c.fetchone()
        c.execute('select * from %s'%(d[0],))
        d2 = c.fetchall()
        for i in d2:
            print(i)

    elif query == 5 :
        name = input('enter new name: ')
        phone = int(input("enter new phone number: "))
        guardian = input('enter new guardian name: ')
        c.execute("update record set name = '%s', phone = '%s', guardians = '%s' where user = '%s'"%(name,phone,guardian,user))
        db.commit()
        print('profile updated!')

    elif query == 6:
        feedback = input("give your feedback please: ")
        c.execute('insert into feedback values("%s", "%s")'%(user, feedback))
        db.commit()

    elif query == 7:
        print("Thank you for Visiting!")
        quit()