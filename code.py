from tabulate import tabulate
import mysql.connector as mysql
def tupleconverter(n):
    for i in n:
        a=i
    return a
# my sql connection
cm = mysql.connect(host="localhost", username="root", password="Pr@nJ@l2020##", database="bank_management_system")
cu=cm.cursor()
print( "==================================================       WELCOME TO BANK       ====================================================")
try:
    while True:
        print( " BANK MANAGEMENT SYSTEM",'\n',"1. Customer login",'\n',"2. Agent Login",'\n',"3. Quit")
        a=int(input("enter your choice : "))
        # if customer login was choosen
        if a==1:
            b=int(input("Enter your account number : "))
            # Check existance of account number in a table
            hi="SELECT EXISTS(SELECT * FROM customer WHERE account_number={});".format(b)
            cu.execute(hi)
            hey=cu.fetchone()
            convert0 = tupleconverter(hey)
            # if exists
            if convert0==1:
                password=int(input("Enter your password : "))
                c="select password from customer where account_number={}".format(b)
                cu.execute(c)
                d=cu.fetchone()
                converter = tupleconverter(d)
                # password match
                if password==converter:
                    f="select name from customer where account_number={}".format(b)
                    cu.execute(f)
                    g=cu.fetchone()
                    convert2= tupleconverter(g)
                    print("Welcome ",convert2,",")
                    while a==1:
                        print(" Account Menu",'\n',"1. Check Balance ",'\n',"2. Deposit ",'\n',"3. Withdraw ",'\n',"4. Fund Transfer")
                        print(" 5. Change password ",'\n',"6. Log out")
                        h=int(input("Enter your choice number : "))
                        # if check balance was choosen
                        if h==1:
                            j= "select balance from customer where account_number={}".format(b)
                            cu.execute(j)
                            k=cu.fetchone()
                            convert3 =  tupleconverter(k)
                            print("Your balance : ₹", convert3,sep='')
                        
                        # if deposit was choosen
                        if h==2:
                            v="deposite"+str(b)
                            check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(v)
                            cu.execute(check)
                            fetch=cu.fetchone()
                            # if table not exist
                            if fetch is None:
                                new=f"create table {v} (deposit decimal(10,2) not null, time timestamp default current_timestamp);"
                                cu.execute(new)
                                l=int(input("Enter amount to be deposited : "))
                                i="insert into {} (deposit) values({})".format(v,l)
                                cu.execute(i)
                                add=" update customer set balance=balance+{}".format(l)
                                cu.execute(add)
                                h="select balance from customer where account_number={}".format(b)
                                cu.execute(h)
                                o=cu.fetchone()
                                convert4= tupleconverter(o)
                                print("Deposited ₹",l," Successfully",sep='')
                                print("Your current balance ₹",convert4,sep='')
                                cm.commit()
                            # if table already exist
                            else:
                                newl=int(input("Enter amount to be deposited : "))
                                newi="insert into {} (deposit) values({})".format(v,newl)
                                cu.execute(newi)
                                newadd="update customer set balance=balance+{}".format(newl)
                                cu.execute(newadd)
                                newh="select balance from customer where account_number={}".format(b)
                                cu.execute(newh)
                                newo=cu.fetchone()
                                newconvert4=tupleconverter(newo)
                                print("Deposited ₹",newl," Successfully",sep='')
                                print("Your current balance ₹",newconvert4,sep='')
                                cm.commit()
                            # want to see all transaction list
                            choose=input("Did you want to transaction timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                s=f"select * from {v}"
                                cu.execute(s)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                                
                        # if withdraw was coosen
                        if h==3:
                            ve="withdraw"+str(b)
                            t="select balance from customer where account_number={}".format(b)
                            cu.execute(t)
                            fetch2=cu.fetchone()
                            convert = tupleconverter(fetch2)
                            inputstr=int(input("Enter amount to be withdraw :"))
                            # if withdraw amount is less than total balance
                            if convert > inputstr:
                                check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(ve)
                                cu.execute(check)
                                fetch=cu.fetchone()
                                 # if table not exist
                                if fetch is None:
                                    new=f"create table {ve} (withdraw decimal(10,2) not null, time timestamp default current_timestamp);"
                                    cu.execute(new)
                                    i="insert into {} (withdraw) values({})".format(ve,inputstr)
                                    cu.execute(i)
                                    add=" update customer set balance=balance-{}".format(inputstr)
                                    cu.execute(add)
                                    h="select balance from customer where account_number={}".format(b)
                                    cu.execute(h)
                                    o=cu.fetchone()
                                    convert4=tupleconverter(o)
                                    print("Withdrawed ₹",inputstr," Successfully", sep='')
                                    print("Your current balance ₹",convert4,sep='')
                                    cm.commit()
                                # if table already exist
                                else:
                                    newi="insert into {} (withdraw) values({})".format(ve,inputstr)
                                    cu.execute(newi)
                                    newadd=" update customer set balance=balance-{} where account_number={}".format(inputstr,b)
                                    cu.execute(newadd)
                                    newh="select balance from customer where account_number={}".format(b)
                                    cu.execute(newh)
                                    newo=cu.fetchone()
                                    newconvert4=tupleconverter(newo)
                                    print("Witdrawed ₹",inputstr," Successfully",sep='')
                                    print("Your current balance ₹",newconvert4)
                                    cm.commit()
                            else:
                                print("Insufficient balance")
                            # want to see all transaction list
                            choose=input("Did you want to transaction timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                select="select * from {};".format(ve)
                                cu.execute(select)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))

                        # if fund transfer is choosen
                        if h==4:
                            t=int(input("Enter recipient account number :"))
                            u=int(input("Enter amount to be transfered :"))
                            v="select balance from customer where account_number={}".format(b)
                            cu.execute(v)
                            ve="transaction"+str(b)
                            w=cu.fetchone()
                            convert = tupleconverter(w)
                            # if transfer amount is less than total balance 
                            if convert > u:
                                imp="select name from customer where account_number={}".format(t)
                                cu.execute(imp)
                                raw=cu.fetchone()
                                check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(ve)
                                cu.execute(check)
                                fetch=cu.fetchone()
                                if fetch is None:
                                    nw="create table {} (transfered decimal(10,2),givento int(30), time timestamp default current_timestamp);".format(ve)
                                    cu.execute(nw)
                                    i="insert into {} (transfered) values({},{},)".format(ve,u,t)
                                    cu.execute(i)
                                    x="update customer set balance=balance-{} where account_number={}".format(u,b)
                                    cu.execute(x)
                                    y="update customer set balance=balance+{} where account_number={}".format(u,t)
                                    cu.execute(y)
                                    z="select balance from customer where account_number={}".format(b)
                                    cu.execute(z)
                                    aa=cu.fetchone()
                                    convert3 = tupleconverter(aa)
                                    print("SUCCESSFULLY TRANSFERED",'\n',"Amount = ₹",u,sep='')
                                    print("Your current balance = ₹",convert3,sep='')
                                    cm.commit()
                                else:
                                    i="insert into {} (transfered) values({})".format(ve,u,t)
                                    cu.execute(i)
                                    x="update customer set balance=balance-{} where account_number={}".format(u,b)
                                    cu.execute(x)
                                    y="update customer set balance=balance+{} where account_number={}".format(u,t)
                                    cu.execute(y)
                                    z="select balance from customer where account_number={}".format(b)
                                    cu.execute(z)
                                    aa=cu.fetchone()
                                    convert3 = tupleconverter(aa)
                                    print("SUCCESSFULLY TRANSFERED",'\n',"Amount = ₹",u,sep='')
                                    print("Your current balance = ₹",convert3,sep='')
                                    cm.commit()
                            else:
                                print("Insufficient balance in your account")
                                                                # if user wants to see transaction timing
                            choose=input("Did you want to transaction timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                select="select * from {};".format(ve)
                                cu.execute(select)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                            
                        # if reset password is choosen
                        if h==5:
                            ab=input("Enter new password :")
                            ac=input("Re-enter new password :")
                            # if both password matches
                            if ab==ac:
                                ad="update customer set password={} where account_number={}".format(ac,b)
                                cu.execute(ad)
                                ve="password"+str(b)
                                check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(ve)
                                cu.execute(check)
                                fetch=cu.fetchone()
                                if fetch is None:
                                    new=f"create table {ve} (new_password varchar(30) not null,time timestamp default current_timestamp);"
                                    cu.execute(new)
                                    i="insert into {} (new_password) values({})".format(ve,ac)
                                    cu.execute(i)
                                    print("Password changed SUCCESSFULLY!")
                                else:
                                    i="insert into {} (new_password) values({})".format(ve,ac)
                                    cu.execute(i)
                                    print("Password changed SUCCESSFULLY!")

                            # if both password doesn't matches
                            else:
                                print("Both password doesn't matches")
                            # if user wants to see password changing timing
                            choose=input("Did you want to password changing timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                select="select * from {};".format(ve)
                                cu.execute(select)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                                
                        # if quit was choosen
                        if h==6:
                            print(" Logout successfully")
                            break
                        # if user write no. that is not in menu
                        if h>6:
                            print("please enter a valid operation number")
                # if password doesn't match
                else:
                    print("password doesn't matches")
            # if account number doesn't exist
            else:
                print("Account number doesn't exists")
        if a==2:
            b=int(input("Enter your agent id : "))
            # Check existance of agent account number in a table
            hi="SELECT EXISTS(SELECT * FROM agent WHERE agent_id={});".format(b)
            cu.execute(hi)
            hey=cu.fetchone()
            convert0 = tupleconverter(hey)
            # if exists
            if convert0==1:
                password=int(input("Enter agent id password : "))
                c="select password from agent where agent_id={}".format(b)
                
                cu.execute(c)
                d=cu.fetchone()
                converter = tupleconverter(d)
                # password match
                if password==converter:
                    f="select name from agent where agent_id={}".format(b)
                    cu.execute(f)
                    g=cu.fetchone()
                    convert2=tupleconverter(g)
                    print("Welcome ",convert2,",",sep='')
                    while a==2:
                        print(" Admin Menu",'\n',"1. Create Account ",'\n',"2. Update Account ",'\n',"3. Delete Account ")
                        print(" 4. Search Account",'\n',"5. View All Account ",'\n',"6. Log out")
                        h=int(input("Enter your choice number : "))
                        # if create account is choosen
                        if h==1:
                            aa="SELECT max(account_number) FROM customer"
                            cu.execute(aa)
                            fa=cu.fetchone()
                            convert = tupleconverter(fa)
                            convert3=convert+1
                            print("ACCOUNT NUMBER:",convert3)
                            ca=input("Enter account holder's name :")
                            da=input("Enter password :")
                            ea="INSERT into customer values({},'{}',0,'{}')".format(convert3,ca,da)
                            cu.execute(ea)
                            print("ACCOUNT MADE")
                            cm.commit()
                        # if update account is choosen
                        if h==2:
                            print("Update Menu",'\n',"1. Update Account Name",'\n',"2. Update Password ")
                            ia=int(input("Enter your choice number :"))
                            zb=int(input("Enter account number :"))
                            # if account name has to update
                            if ia==1:
                                ac=input("Enter new account name :")
                                bc="update customer set name='{}' where account_number={}".format(ac,zb)
                                cu.execute(bc)
                            # if password has to update 
                            if ia==2:
                                ac=input("Enter new account password :")
                                bc="update customer set password='{}' where account_number={}".format(zb,ac)
                                cu.execute(bc)
                            print("Changes Done")
                            cm.commit()
                        # if account number to be deleted
                        if h==3:
                            ia=int(input("Enter new account number :"))
                            bc="delete from customer where account_number={}".format(ia)
                            cu.execute(bc)
                            cm.commit()
                        # if account to be search
                        if h==4:
                            ia=int(input("Enter account number to be searched :"))
                            hi="SELECT EXISTS(SELECT * FROM customer WHERE account_number={});".format(ia)
                            cu.execute(hi)
                            hey=cu.fetchone()
                            convert0 = tupleconverter(hey)
                            # if account exists
                            if convert0==1:
                                bc="SELECT * from customer where account_number={}".format(ia)
                                cu.execute(bc)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                            # if account doesn't exist
                            else:
                                print("Account doesn't exists")
                        # if all account to be print
                        if h==5:
                            bc="SELECT * from customer"
                            cu.execute(bc)
                            fetch=cu.fetchall()
                            headers=[i[0] for i in cu.description]
                            print(tabulate(fetch,headers=headers))
                        # logout code
                        if h==6:
                            print("LOGOUT SUCCESSFULLY")
                            break
                        # if user write no. that is not in menu
                        if h>6:
                            print("please enter a valid operation number")
                # password doesn't match
                else:
                    print("Password doesn't match")
            # account doesn't exist
            else:
                print("Account doesn't exist")
        # if user want to close code
        if a==3:
            print("Thanks for giving us opportunity to help you.")
            print("Have a Good Day.","Visit us again!!",sep='\n')
            break
        # if user write no. that is not in menu
        if a>3:
            print("please enter a valid operation number")
except ValueError:
    print("You enter a invalid Value ")

    
from tabulate import tabulate
import mysql.connector as mysql
def tupleconverter(n):
    for i in n:
        a=i
    return a
# my sql connection
cm = mysql.connect(host="localhost", username="root", password="Pr@nJ@l2020##", database="bank_management_system")
cu=cm.cursor()
print( "==================================================       WELCOME TO BANK       ====================================================")
try:
    while True:
        print( " BANK MANAGEMENT SYSTEM",'\n',"1. Customer login",'\n',"2. Agent Login",'\n',"3. Quit")
        a=int(input("enter your choice : "))
        # if customer login was choosen
        if a==1:
            b=int(input("Enter your account number : "))
            # Check existance of account number in a table
            hi="SELECT EXISTS(SELECT * FROM customer WHERE account_number={});".format(b)
            cu.execute(hi)
            hey=cu.fetchone()
            convert0 = tupleconverter(hey)
            # if exists
            if convert0==1:
                password=int(input("Enter your password : "))
                c="select password from customer where account_number={}".format(b)
                cu.execute(c)
                d=cu.fetchone()
                converter = tupleconverter(d)
                # password match
                if password==converter:
                    f="select name from customer where account_number={}".format(b)
                    cu.execute(f)
                    g=cu.fetchone()
                    convert2= tupleconverter(g)
                    print("Welcome ",convert2,",")
                    while a==1:
                        print(" Account Menu",'\n',"1. Check Balance ",'\n',"2. Deposit ",'\n',"3. Withdraw ",'\n',"4. Fund Transfer")
                        print(" 5. Change password ",'\n',"6. Log out")
                        h=int(input("Enter your choice number : "))
                        # if check balance was choosen
                        if h==1:
                            j= "select balance from customer where account_number={}".format(b)
                            cu.execute(j)
                            k=cu.fetchone()
                            convert3 =  tupleconverter(k)
                            print("Your balance : ₹", convert3,sep='')
                        
                        # if deposit was choosen
                        if h==2:
                            v="deposite"+str(b)
                            check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(v)
                            cu.execute(check)
                            fetch=cu.fetchone()
                            # if table not exist
                            if fetch is None:
                                new=f"create table {v} (deposit decimal(10,2) not null, time timestamp default current_timestamp);"
                                cu.execute(new)
                                l=int(input("Enter amount to be deposited : "))
                                i="insert into {} (deposit) values({})".format(v,l)
                                cu.execute(i)
                                add=" update customer set balance=balance+{}".format(l)
                                cu.execute(add)
                                h="select balance from customer where account_number={}".format(b)
                                cu.execute(h)
                                o=cu.fetchone()
                                convert4= tupleconverter(o)
                                print("Deposited ₹",l," Successfully",sep='')
                                print("Your current balance ₹",convert4,sep='')
                                cm.commit()
                            # if table already exist
                            else:
                                newl=int(input("Enter amount to be deposited : "))
                                newi="insert into {} (deposit) values({})".format(v,newl)
                                cu.execute(newi)
                                newadd="update customer set balance=balance+{}".format(newl)
                                cu.execute(newadd)
                                newh="select balance from customer where account_number={}".format(b)
                                cu.execute(newh)
                                newo=cu.fetchone()
                                newconvert4=tupleconverter(newo)
                                print("Deposited ₹",newl," Successfully",sep='')
                                print("Your current balance ₹",newconvert4,sep='')
                                cm.commit()
                            # want to see all transaction list
                            choose=input("Did you want to transaction timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                s=f"select * from {v}"
                                cu.execute(s)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                                
                        # if withdraw was coosen
                        if h==3:
                            ve="withdraw"+str(b)
                            t="select balance from customer where account_number={}".format(b)
                            cu.execute(t)
                            fetch2=cu.fetchone()
                            convert = tupleconverter(fetch2)
                            inputstr=int(input("Enter amount to be withdraw :"))
                            # if withdraw amount is less than total balance
                            if convert > inputstr:
                                check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(ve)
                                cu.execute(check)
                                fetch=cu.fetchone()
                                 # if table not exist
                                if fetch is None:
                                    new=f"create table {ve} (withdraw decimal(10,2) not null, time timestamp default current_timestamp);"
                                    cu.execute(new)
                                    i="insert into {} (withdraw) values({})".format(ve,inputstr)
                                    cu.execute(i)
                                    add=" update customer set balance=balance-{}".format(inputstr)
                                    cu.execute(add)
                                    h="select balance from customer where account_number={}".format(b)
                                    cu.execute(h)
                                    o=cu.fetchone()
                                    convert4=tupleconverter(o)
                                    print("Withdrawed ₹",inputstr," Successfully", sep='')
                                    print("Your current balance ₹",convert4,sep='')
                                    cm.commit()
                                # if table already exist
                                else:
                                    newi="insert into {} (withdraw) values({})".format(ve,inputstr)
                                    cu.execute(newi)
                                    newadd=" update customer set balance=balance-{} where account_number={}".format(inputstr,b)
                                    cu.execute(newadd)
                                    newh="select balance from customer where account_number={}".format(b)
                                    cu.execute(newh)
                                    newo=cu.fetchone()
                                    newconvert4=tupleconverter(newo)
                                    print("Witdrawed ₹",inputstr," Successfully",sep='')
                                    print("Your current balance ₹",newconvert4)
                                    cm.commit()
                            else:
                                print("Insufficient balance")
                            # want to see all transaction list
                            choose=input("Did you want to transaction timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                select="select * from {};".format(ve)
                                cu.execute(select)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))

                        # if fund transfer is choosen
                        if h==4:
                            t=int(input("Enter recipient account number :"))
                            u=int(input("Enter amount to be transfered :"))
                            v="select balance from customer where account_number={}".format(b)
                            cu.execute(v)
                            ve="transaction"+str(b)
                            w=cu.fetchone()
                            convert = tupleconverter(w)
                            # if transfer amount is less than total balance 
                            if convert > u:
                                imp="select name from customer where account_number={}".format(t)
                                cu.execute(imp)
                                raw=cu.fetchone()
                                check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(ve)
                                cu.execute(check)
                                fetch=cu.fetchone()
                                if fetch is None:
                                    nw="create table {} (transfered decimal(10,2),givento int(30), time timestamp default current_timestamp);".format(ve)
                                    cu.execute(nw)
                                    i="insert into {} (transfered) values({},{},)".format(ve,u,t)
                                    cu.execute(i)
                                    x="update customer set balance=balance-{} where account_number={}".format(u,b)
                                    cu.execute(x)
                                    y="update customer set balance=balance+{} where account_number={}".format(u,t)
                                    cu.execute(y)
                                    z="select balance from customer where account_number={}".format(b)
                                    cu.execute(z)
                                    aa=cu.fetchone()
                                    convert3 = tupleconverter(aa)
                                    print("SUCCESSFULLY TRANSFERED",'\n',"Amount = ₹",u,sep='')
                                    print("Your current balance = ₹",convert3,sep='')
                                    cm.commit()
                                else:
                                    i="insert into {} (transfered) values({})".format(ve,u,t)
                                    cu.execute(i)
                                    x="update customer set balance=balance-{} where account_number={}".format(u,b)
                                    cu.execute(x)
                                    y="update customer set balance=balance+{} where account_number={}".format(u,t)
                                    cu.execute(y)
                                    z="select balance from customer where account_number={}".format(b)
                                    cu.execute(z)
                                    aa=cu.fetchone()
                                    convert3 = tupleconverter(aa)
                                    print("SUCCESSFULLY TRANSFERED",'\n',"Amount = ₹",u,sep='')
                                    print("Your current balance = ₹",convert3,sep='')
                                    cm.commit()
                            else:
                                print("Insufficient balance in your account")
                                                                # if user wants to see transaction timing
                            choose=input("Did you want to transaction timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                select="select * from {};".format(ve)
                                cu.execute(select)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                            
                        # if reset password is choosen
                        if h==5:
                            ab=input("Enter new password :")
                            ac=input("Re-enter new password :")
                            # if both password matches
                            if ab==ac:
                                ad="update customer set password={} where account_number={}".format(ac,b)
                                cu.execute(ad)
                                ve="password"+str(b)
                                check="SHOW TABLE STATUS FROM bank_management_system WHERE Name = '{}';".format(ve)
                                cu.execute(check)
                                fetch=cu.fetchone()
                                if fetch is None:
                                    new=f"create table {ve} (new_password varchar(30) not null,time timestamp default current_timestamp);"
                                    cu.execute(new)
                                    i="insert into {} (new_password) values({})".format(ve,ac)
                                    cu.execute(i)
                                    print("Password changed SUCCESSFULLY!")
                                else:
                                    i="insert into {} (new_password) values({})".format(ve,ac)
                                    cu.execute(i)
                                    print("Password changed SUCCESSFULLY!")

                            # if both password doesn't matches
                            else:
                                print("Both password doesn't matches")
                            # if user wants to see password changing timing
                            choose=input("Did you want to password changing timings :")
                            choose1=choose.lower()
                            # if yes
                            if choose1=="yes":
                                select="select * from {};".format(ve)
                                cu.execute(select)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                                
                        # if quit was choosen
                        if h==6:
                            print(" Logout successfully")
                            break
                        # if user write no. that is not in menu
                        if h>6:
                            print("please enter a valid operation number")
                # if password doesn't match
                else:
                    print("password doesn't matches")
            # if account number doesn't exist
            else:
                print("Account number doesn't exists")
        if a==2:
            b=int(input("Enter your agent id : "))
            # Check existance of agent account number in a table
            hi="SELECT EXISTS(SELECT * FROM agent WHERE agent_id={});".format(b)
            cu.execute(hi)
            hey=cu.fetchone()
            convert0 = tupleconverter(hey)
            # if exists
            if convert0==1:
                password=int(input("Enter agent id password : "))
                c="select password from agent where agent_id={}".format(b)
                
                cu.execute(c)
                d=cu.fetchone()
                converter = tupleconverter(d)
                # password match
                if password==converter:
                    f="select name from agent where agent_id={}".format(b)
                    cu.execute(f)
                    g=cu.fetchone()
                    convert2=tupleconverter(g)
                    print("Welcome ",convert2,",",sep='')
                    while a==2:
                        print(" Admin Menu",'\n',"1. Create Account ",'\n',"2. Update Account ",'\n',"3. Delete Account ")
                        print(" 4. Search Account",'\n',"5. View All Account ",'\n',"6. Log out")
                        h=int(input("Enter your choice number : "))
                        # if create account is choosen
                        if h==1:
                            aa="SELECT max(account_number) FROM customer"
                            cu.execute(aa)
                            fa=cu.fetchone()
                            convert = tupleconverter(fa)
                            convert3=convert+1
                            print("ACCOUNT NUMBER:",convert3)
                            ca=input("Enter account holder's name :")
                            da=input("Enter password :")
                            ea="INSERT into customer values({},'{}',0,'{}')".format(convert3,ca,da)
                            cu.execute(ea)
                            print("ACCOUNT MADE")
                            cm.commit()
                        # if update account is choosen
                        if h==2:
                            print("Update Menu",'\n',"1. Update Account Name",'\n',"2. Update Password ")
                            ia=int(input("Enter your choice number :"))
                            zb=int(input("Enter account number :"))
                            # if account name has to update
                            if ia==1:
                                ac=input("Enter new account name :")
                                bc="update customer set name='{}' where account_number={}".format(ac,zb)
                                cu.execute(bc)
                            # if password has to update 
                            if ia==2:
                                ac=input("Enter new account password :")
                                bc="update customer set password='{}' where account_number={}".format(zb,ac)
                                cu.execute(bc)
                            print("Changes Done")
                            cm.commit()
                        # if account number to be deleted
                        if h==3:
                            ia=int(input("Enter new account number :"))
                            bc="delete from customer where account_number={}".format(ia)
                            cu.execute(bc)
                            cm.commit()
                        # if account to be search
                        if h==4:
                            ia=int(input("Enter account number to be searched :"))
                            hi="SELECT EXISTS(SELECT * FROM customer WHERE account_number={});".format(ia)
                            cu.execute(hi)
                            hey=cu.fetchone()
                            convert0 = tupleconverter(hey)
                            # if account exists
                            if convert0==1:
                                bc="SELECT * from customer where account_number={}".format(ia)
                                cu.execute(bc)
                                fetch=cu.fetchall()
                                headers=[i[0] for i in cu.description]
                                print(tabulate(fetch,headers=headers))
                            # if account doesn't exist
                            else:
                                print("Account doesn't exists")
                        # if all account to be print
                        if h==5:
                            bc="SELECT * from customer"
                            cu.execute(bc)
                            fetch=cu.fetchall()
                            headers=[i[0] for i in cu.description]
                            print(tabulate(fetch,headers=headers))
                        # logout code
                        if h==6:
                            print("LOGOUT SUCCESSFULLY")
                            break
                        # if user write no. that is not in menu
                        if h>6:
                            print("please enter a valid operation number")
                # password doesn't match
                else:
                    print("Password doesn't match")
            # account doesn't exist
            else:
                print("Account doesn't exist")
        # if user want to close code
        if a==3:
            print("Thanks for giving us opportunity to help you.")
            print("Have a Good Day.","Visit us again!!",sep='\n')
            break
        # if user write no. that is not in menu
        if a>3:
            print("please enter a valid operation number")
except ValueError:
    print("You enter a invalid Value ")
    