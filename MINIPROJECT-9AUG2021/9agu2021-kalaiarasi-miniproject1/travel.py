import re
import logging
import csv
import time
import smtplib
try:
    headercontent=["name","address","mobilenum","emailid","tripdate","tripcost","tripid","tripplan"]
    travelist=[]
    def validation(name,emailid,mobilenum,tripdate):
        vname=re.search("^[A-Za-z]{2,25}$",name)
        vmail=re.search("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",emailid)
        vmob=re.search("^(\+91)?[0]?(91)?[6-9]\d{9}$",mobilenum)
        vdate=re.search("^[0-9]{2}\s[0-9]{2}\s[0-9]{4}",tripdate)
        if vname and vmail and vmob and tripdate:
            return True
        else:
            return False
    class Customerdetail:
        def __init__(self):
            name=''
            address=''
            mobilenum=''
            emailid=''
        def addcustomerdetail(self,name,address,mobilenum,emailid):
            name="name"
            address="address"
            mobilenum="mobilenum"
            emailid="emailid"
            return self.addcustomerdetail
    class Trip(Customerdetail):
        def __init__(self):
            tripid=''
            tripdate=''
            tripcost=''
            tripid=''
        def addtrip(self,tripdate,tripcost,tripplan,tripid):
            tripid="tripid"
            tripdate="tripdate"
            tripcost="tripcost"
            tripplan="tripplan"
        
            return self.addtrip

    obj=Trip()
    if(__name__=='__main__'):
        while(True):
            print("1. add trip")
            print("2. view the details")
            print("3. search using customer name")
            print("4. Display the customer details who have trip today")
            print("5. sort according to the date of trip")
            print("6. change the trip plan")
            print("7. Delete the trip")
            print("8. save to file")
            print("9. send an email")
            print("10. exit")

            choice=int(input("enter ur choice:"))
             
            if choice==1:
                name=input("enter your name:")
                address=input("enter your add:")
                mobilenum=input("enter your mobilenum:")
                emailid=input("enter your emailid:")
                
                tripid=int(input("enter your id:"))
                tripcost=int(input("enter your cost:"))
                tripplan=input("enter your pla:")
                tripdate=input("enter your date:")
                
            
                x=validation(name,emailid,mobilenum,tripdate)
                if x:
                    obj.addcustomerdetail(name,address,mobilenum,emailid)
                    obj.addtrip(tripdate,tripcost,tripplan,tripid)
                    dict1={"name":name,"address":address,"mobilenum":mobilenum,"emailid":emailid,"tripdate":tripdate,"tripcost":tripcost,"tripid":tripid,"tripplan":tripplan}
                    travelist.append(dict1)


                else:
                    logging.error("please enter valid data!")
            if choice==2:
                print(travelist)

            if choice==3:
                searchname=input("enter the name:")
                print(list(filter(lambda i:i["name"]==searchname,travelist)))
            
            
            if choice==4:
                currenttime=time.localtime()
                currentclock=time.strftime("%d %m %Y",currenttime)
                print(list(filter(lambda i: i["tripdate"]==currentclock,travelist)))
            
            if choice==5:
                x=sorted(travelist,key=lambda i:i["tripdate"])
                print(x)       
                
            if choice==6:
                old=input("enter old plan:")
                new=input("enter new plan:")
                for i in travelist: 
                    i.update((k,new) for k,v in i.items() if v==old)
                print(travelist) 
            
            if choice==7:
                tid=int(input("enter the id to remove:"))
                for i in range(len(travelist)):
                    if travelist[i]["tripid"]==tid:
                        del travelist[i]
                        break
                print(travelist)
                
            if choice==8:
                with open('travelfile.csv','w+',encoding='UTF8',newline='') as t:
                        writer=csv.DictWriter(t,fieldnames=headercontent)
                        writer.writeheader()
                        writer.writerows(travelist)
                print("saved to file")

            if choice==9:
                
                for i in travelist:
                        message="Thank for u choosing AB Travels.we make your travel memorable and fun."
                        connection =smtplib.SMTP("smtp.gmail.com",587)
                        connection.starttls()
                        connection.login("kalai.iprimed@gmail.com","Kalai@2404")
                        message="Thank for u choosing AB Travels.we make your travel memorable and fun."
                        print(message)
                        connection.sendmail("kalai.iprimed@gmail.com",i["emailid"],message)
                        connection.quit()
                        print("email send")
                    
            if choice==10:
                break
                                        
except:
    logging.error("please enter correct data")

     