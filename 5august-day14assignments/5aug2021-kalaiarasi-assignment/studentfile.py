import re
import csv
import logging
try:
    headercontent=["totalmarks","name","rollno","admin","eng","tamil","math","sci","soc"]
    studentlist=[]
    def validation(name):
        vname=re.search("^[A-Za-z]{2,25}$",name)
        if vname:
            return True
        else:
            return False
    class Studentdetail:

        def addstudentdetail(self,name,rollno,admin,eng,tamil,math,sci,soc):
            totalmarks=eng+tamil+math+sci+soc
            dict1={"totalmarks":totalmarks,"name":name,"rollno":rollno,"admin":admin,"eng":eng,"tamil":tamil,"math":math,"sci":sci,"soc":soc}
            studentlist.append(dict1)
    
    obj1=Studentdetail()
    while(True):
        print("1. add student")
        print("2. display student like api")
        print("3. search student using rollno")
        print("4. ranking")
        print("5. save to file")
        print("6. exit")
        choice=int(input("enter ur choice:"))
        #obj1=Studentdetail()
        if choice==1:
            name=input("enter your name:")
            rollno=int(input("enter your rollno:"))
            admin=int(input("enter your admin:"))
            eng=int(input("enter your eng:"))
            tamil=int(input("enter your tamil:"))
            math=int(input("enter your math:"))
            sci=int(input("enter your sci:"))
            soc=int(input("enter your soc:"))
            x=validation(name)
            if x:
                obj1.addstudentdetail(name,rollno,admin,eng,tamil,math,sci,soc)
            else:
                logging.error("please enter valid data!")
        if choice==2:
            print(studentlist)
        
        if choice==3:
            srollno=int(input("enter your rollno:"))
            print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
        
        if choice==4:
            print(sorted(studentlist,key=lambda i:i["totalmarks"],reverse=True))
        if choice==5:
            with open('studentf.csv','w+',encoding='UTF8',newline='') as s:
                writer=csv.DictWriter(s,fieldnames=headercontent)
                writer.writeheader()
                writer.writerows(studentlist)

        if choice==6:
            break
except:
    logging.error("please enter correct data")

