import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='your password ')
mycursor=mydb.cursor()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("##########################################################################")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(""" INDIAN LIBRARY welcomes YOU !!!!""")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("##########################################################################")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
a=int(input("ENTER YOUR CHOICE \n 1).Administration(1) \n 2).Customer(2)\n 3).EXIT(3)\n YOURC CHOICE ===>"))
while True:
        if a==1:
            print("YOU had selected ADMINISTRATION")
            b=int(input("ENTER YOUR PASSWORD ======> :"))

            if b==1234:
                print("@@@######YOU HAVE SUCCESSFULLY LOGGED INTO. ADMINISTRATION#######@@@")
                c1=int(input("""Enter your choices \n1).TO FIND REQUIRED INFORMATION FROM BOOKS.  2).TO FIND REQUIRES INFORMATION FROM STAFFS.\n 3)EXIT\n PLEASE ENTER YOUR CHOICE ======>"""))
                if c1==1:
                        I=int(input("""Enter your choice \n. 1).TO FIND THE TOTAL NUMBER OF BOOKS =>(1) \n 2).TO FIND THE BOOKS IN DIFFERENT CATEGORY =>(2)\n 3).TO ADD BOOKS =>(3)\n PLEASE ENTER YOUR CHOICE ========>"""))
                        if I==1:
                                print(('-')*20,"THE TOTAL NUMBER OF BOOKS",('-')*20)
                                mycursor.execute("use LIBRARY;")
                                mycursor.execute('select count(*) from BOOK;')
                                data=mycursor.fetchall()
                                for i in data:
                                        for j in i:
                                                print(j)
                        elif I==2:
                                mycursor.execute('use LIBRARY;')
                                print(('-')*20,"THE BOOKS IN DIFFERENT CATEGORY",('-')*20)
                                a=input("Enter your category:")
                                b="select count(*) from BOOK where TYPE=%s"
                                mycursor.execute("select count(*) from BOOK where  TYPE='{}'".format(a))
                                data=mycursor.fetchall()
                                for i in data:
                                        for j in i:
                                            print(j)
                        elif I==3:
                                mycursor.execute('use LIBRARY;')
                                print(('-')*20,"TO ADD BOOKS",('-')*20)
                                a=input("Enter the BOOK_CODE:")
                                b=input("Enter the BOOK_NAME:")
                                c=input("Enter the AUTHOR_NAME:")
                                d=input("Enter the PUBLISHER:")
                                e=input("Enter the TYPE:")
                                f=input("Enter the STOCK:")
                                m ='insert into BOOK values(%s,%s,%s,%s,%s,%s);'
                                n=[a,b,c,d,e,f]
                                mycursor.execute(m,n)
                                mydb.commit()
                                print("Book added succesfully")
                elif c1==2:
                        i=int(input("""Enter your choice : \n
                        1).To find the total number of staffs =>(1)
                        2).To find the number of staffs in different category =>(2)
                        3).To update the salary for a particular staff => (3)
                        Enter your choice =================>"""))
                        if i==1:
                                    mycursor.execute('use LIBRARY;')
                                    print(('-')*20,"The total number of staffs",('-')*20)
                                    mycursor.execute('select count(*) from STAFF;')
                                    data=mycursor.fetchall()
                                    for i in data:
                                            for j in i:
                                                    print(j)
                        elif i==2:
                                    mycursor.execute('use LIBRARY;')
                                    print(('-')*20,"The number of staffs in different category ",('-')*20)
                                    a=input("Enter the managment to find the number of staffs working there:")
                                    mycursor.execute("select count(*) from STAFF where DEPARTMENT='{}'".format(a))
                                    data=mycursor.fetchall()
                                    for i in data:
                                            for j in i:
                                                    print(j)
                        elif i==3:
                                    mycursor.execute('use LIBRARY;')
                                    print(('-')*20,"To find update the salary for a particular staff ",('-')*20)
                                    a=input("Enter the staff ID to update the salary:")
                                    c=int(input("Enter the salary:"))
                                    b="update STAFF set SALARY = {} where STAFF_ID='{}';".format(c,a)
                                    mycursor.execute(b)
                                    mydb.commit()
                                    print("Updated Succesfully")
                        else:
                                print("YOU HAD SELECTED EXIT")
                                break
            else:
                        print("""******************You had entered incorrect password*********************** !!!!!!!!!!!!!!!!!!!!!!!!!!!!PLEASE TRY AGAIN LATER!!!!!!!!!!!!!!!!!!!!!""")
                        break
        elif a==2:
                while True:
                        b=int(input("Enter Your Choice \n 1)New User(Sign Up) \n 2)Existing User(Log In)"))
                        mycursor.execute('use LIBRARY')
                        if b==1:
                                import random
                                j=""
                                full_name = input("Please enter your name: ")
                                fullname=full_name.lower().split()
                                first_letter = fullname[0][0]
                                three_letters_surname = fullname[-1][:3].rjust(3, ' ')
                                number = '{:03d}'.format(random.randrange (1,999))
                                login_id = '{}{}{}'.format(first_letter, three_letters_surname, number)
                                print('Your membership ID is:',login_id)
                                password=input('Create a password:')
                                address=input('Enter address:')
                                phone=int(input('Enter phone no.:'))
                                mycursor.execute("select curdate()")
                                i=str(mycursor.fetchall())
                                Type=input('Enter type of membership:')
                                print("Account sucessfully created")
                                if Type=='Silver':
                                        mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +3 MONTH)")
                                        j=str(mycursor.fetchall())
                                elif Type=='Gold':
                                        mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL  +6 MONTH)")
                                        j=str(mycursor.fetchall())
                                elif Type=='Platinum':
                                                mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +12 MONTH)")
                                                j=str(mycursor.fetchall())
                                                mycursor.execute('insert into MEMBERSHIP values("{}","{}","{}",{},"{}","{}","{}","{}")'.format(login_id,password,full_name,phone,address,i,j,Type))
                                                mydb.commit()
                                                break
                        elif b==2:
                                login_id1=input("enter the membership id:")
                                login_password=input("enter the password:")
                                d=mycursor.execute("select * from MEMBERSHIP;")
                                r=mycursor.fetchall()
                                l=[]
                                l1=[]
                                for i in r:
                                        for j in i:
                                                l.append(i[0])
                                                l1.append(i[1])
                                                if login_id1 in l:
                                                        if login_password in l1:
                                                                print("Sucessfully logged in")
                                                                searchbook=int(input("Enter the Choice:\n 1)Search & Borrow Books by Genre:\n 2)Search & Borrow Book by Book Name: \n 3)Search & borrow the books written by the author\n 4)Check the availability of Book\n 5)Return a book\n 6)Log out \n Enter your choice =========>"))
                                                                if searchbook==1:
                                                                        mycursor.execute('use LIBRARY')
                                                                        bookgenre=input(" enter the genre to be searched:")
                                                                        mycursor.execute("select* from BOOK where TYPE='{}'".format(bookgenre))
                                                                        data=mycursor.fetchall()
                                                                        for i in data:
                                                                                print(i)

                                                                        c=input("Enter Book name to borrow:")
                                                                        mycursor.execute("SELECT * FROM MEMBERSHIP WHERE MEMBERSHIP_ID=('{}')".format(login_id1))
                                                                        r=mycursor.fetchall()
                                                                        mycursor.execute("select curdate()")
                                                                        k=mycursor.fetchall()
                                                                        for z in r:
                                                                                lp=''
                                                                                if z[7]=='Silver':
                                                                                        mycursor.execute("select curdate()")
                                                                                        i=str(mycursor.fetchall())
                                                                                        mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +1 MONTH)")
                                                                                        lp=str(mycursor.fetchall())
                                                                                if z[7]=='Gold':
                                                                                        mycursor.execute("select curdate()")
                                                                                        i=str(mycursor.fetchall())
                                                                                        mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +2 MONTH)")
                                                                                        lp=str(mycursor.fetchall())

                                                                                if z[7]=='Platinum':
                                                                                        mycursor.execute("select curdate()")
                                                                                        i=str(mycursor.fetchall())
                                                                                        mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +3 MONTH)")
                                                                                        lp=str(mycursor.fetchall())
                                                                                mycursor.execute("INSERT INTO BORROWER VALUES('{}','{}','{}','{}')".format(login_id1,c,k,lp))
                                                                                mydb.commit()
                                                                                mycursor.execute("UPDATE BOOK SET STOCK=STOCK-1 WHERE BOOK_NAME=('{}')".format(c))
                                                                                mydb.commit()
                                                                                print("Book Borrowed Succesfully")
                                                                elif searchbook==2:
                                                                        c=input("enter the name of the book to be searched:")
                                                                        mycursor.execute("select* from BOOK where BOOK_NAME='{}'".format(c))
                                                                        data1=mycursor.fetchall()
                                                                        for row1 in data1:
                                                                                print(row1)
                                                                        mycursor.execute("SELECT * FROM MEMBERSHIP WHERE MEMBERSHIP_ID=('{}')".format(login_id1))
                                                                        r=mycursor.fetchall()
                                                                        mycursor.execute("select curdate()")
                                                                        k=mycursor.fetchall()
                                                                        for z in r:
                                                                                                lp=''
                                                                                                if z[7]=='Silver':
                                                                                                        mycursor.execute("select curdate()")
                                                                                                        i=str(mycursor.fetchall())
                                                                                                        mycursor.execute("SELECT DATE_ADD(curdate(),INTERVAL +1 MONTH)")
                                                                                                        lp=str(mycursor.fetchall())
                                                                                                if z[7]=='Gold':
                                                                                                        mycursor.execute("select curdate()")
                                                                                                        i=str(mycursor.fetchall())

                                                                                                        mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +2 MONTH)")
                                                                                                        lp=str(mycursor.fetchall())
                                                                                                if z[7]=='Platinum':
                                                                                                                mycursor.execute("select curdate()")
                                                                                                                i=str(mycursor.fetchall())
                                                                                                                mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +3 MONTH)")
                                                                                                                lp=str(mycursor.fetchall())
                                                                                                mycursor.execute("INSERT INTO BORROWER VALUES('{}','{}','{}','{}')".format(login_id1,c,k,lp))
                                                                                                mydb.commit()
                                                                                                mycursor.execute("UPDATE BOOK SET STOCK=STOCK-1 WHERE BOOK_NAME=('{}')".format(c))
                                                                                                mydb.commit()
                                                                                                print("Book Borrowed Succesfully")
                                                                elif searchbook==3:
                                                                                search_author=input("enter the author to be searched:")
                                                                                mycursor.execute("select* from BOOK where AUTHOR_NAME='{}'".format(search_author))
                                                                                data2=mycursor.fetchall()

                                                                                for row2 in data2:
                                                                                                print(row2)
                                                                                                c=input("Enter Book name to borrow:")
                                                                                                mycursor.execute("SELECT * FROM MEMBERSHIP  WHERE MEMBERSHIP_ID=('{}')".format(login_id1))
                                                                                                r=mycursor.fetchall()
                                                                                                mycursor.execute("select curdate()")
                                                                                                k=mycursor.fetchall()
                                                                                                for z in r:
                                                                                                        lp=''
                                                                                                        if z[7]=='Silver':
                                                                                                                mycursor.execute("select curdate()")
                                                                                                                i=str(mycursor.fetchall())
                                                                                                                mycursor.execute("SELECT DATE_ADD(curdate(),INTERVAL +1 MONTH)")
                                                                                                                lp=str(mycursor.fetchall())
                                                                                                        if z[7]=='Gold':
                                                                                                                mycursor.execute("select curdate()")
                                                                                                                i=str(mycursor.fetchall())

                                                                                                                mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +2 MONTH)")
                                                                                                                lp=str(mycursor.fetchall())
                                                                                                        if z[7]=='Platinum':
                                                                                                                mycursor.execute("select curdate()")
                                                                                                                i=str(mycursor.fetchall())
                                                                                                                mycursor.execute("SELECT DATE_ADD(curdate(), INTERVAL +3 MONTH)")
                                                                                                                lp=str(mycursor.fetchall())
                                                                                                        mycursor.execute("INSERT INTO BORROWER VALUES('{}','{}','{}','{}')".format(login_id1,c,k,lp))
                                                                                                        mydb.commit()
                                                                                                        mycursor.execute("UPDATE BOOK SET STOCK=STOCK-1 WHERE BOOK_NAME=('{}')".format(c))
                                                                                                        mydb.commit()
                                                                                                        print("Book Borrowed Succesfully")
                                                                elif searchbook==4:
                                                                                c=input("enter the name of the book to check the no of books availability :")
                                                                                mycursor.execute("select* from BOOK where BOOK_NAME='{}'".format(c))
                                                                                data4=mycursor.fetchall()

                                                                                for j in data4:
                                                                                                if int(j[5])<=0:
                                                                                                        print("Out of Stock")
                                                                                                else:
                                                                                                        print("In Stock")
                                                                elif searchbook==5:
                                                                                rid=input("Enter your membership id:")
                                                                                rname=input("Enter the book name to be returned:")
                                                                                mycursor.execute("select curdate()")
                                                                                brd=str(mycursor.fetchall())
                                                                                mycursor.execute("insert into RETURNBOOK VALUES('{}','{}','{}')".format(rid,rname,brd))
                                                                                mycursor.execute('use LIBRARY;')
                                                                                mycursor.execute("SELECT TYPE FROM MEMBERSHIP WHERE MEMBERSHIP_ID=('{}')".format(rid))
                                                                                k=mycursor.fetchall()
                                                                                mycursor.execute("SELECT BOOK_RETURN_DATE FROM RETURNBOOK WHERE MEMBERSHIP_ID=('{}') AND BOOK_NAME=('{}')".format(rid,rname))
                                                                                y=mycursor.fetchall()
                                                                                t=()
                                                                                for i in k:

                                                                                        for j in i:
                                                                                                        if j=='Silver':
                                                                                                                z=mycursor.execute("SELECT * FROM BORROWER")
                                                                                                                l=mycursor.fetchall()
                                                                                                                fine=0
                                                                                                                l1=[]
                                                                                                                for i in l:
                                                                                                                        for j in i:
                                                                                                                                t+=(i[2],)
                                                                                                                                l1.append(t)
                                                                                                                                break
                                                                                                                        break
                                                                                                                if y<=l1:
                                                                                                                                fine=0
                                                                                                                else:
                                                                                                                        fine=150
                                                                                                                print("Fine",fine)
                                                                                                        if j=='Gold':
                                                                                                                z=mycursor.execute("SELECT * FROM BORROWER")

                                                                                                                l=mycursor.fetchall()
                                                                                                                fine=0
                                                                                                                l1=[]
                                                                                                                for i in l:
                                                                                                                                for j in i:
                                                                                                                                        t+=(i[2],)
                                                                                                                                        l1.append(t)
                                                                                                                                        break
                                                                                                                                break
                                                                                                                if y<=l1:
                                                                                                                        fine=0
                                                                                                                else:
                                                                                                                        fine=100
                                                                                                                print("Fine",fine)
                                                                                                        if j=='Platinum':
                                                                                                                        z=mycursor.execute("SELECT * FROM BORROWER")
                                                                                                                        l=mycursor.fetchall()
                                                                                                                        fine=0
                                                                                                                        l1=[]
                                                                                                                        for i in l:
                                                                                                                        
                                                                                                                                        for j in i:
                                                                                                                                                t+=(i[2],)
                                                                                                                                                l1.append(t)
                                                                                                                                                break
                                                                                                                                        break
                                                                                                                        if y<=l1:
                                                                                                                                fine=0
                                                                                                                        else:
                                                                                                                                fine=50
                                                                                                                        print("Fine",fine)
                                                                elif searchbook==6:
                                                                                 print('-'*10,"THANK YOU!!",'-'*10)
                                                                                 print('-'*10,"VIST AGAIN!!",'-'*10)
                                                                                 break
                                                        else:
                                                                print('Incorrect password or User ID')
                                                                break
                                                else:

                                                                print("Invalid Login ID")
                                                                break
                                                break
                        break
        else:
                        print('*'*50)
                        print('-'*25,'THANK YOU','-'*25)
                        print('-'*25,'FOR VISITING US ','-'*25)
                        break



   
