import threading,time
def primenum():
    for n in range(2,500):
        if n>1:
            for i in range(2,n):
                if n%i==0:
                    break
            else:
                time.sleep(1)
                print("prime:",n)

def palindrome():
    for i in range(10,500):
        t=i
        rev=0
        while(t>0):
            rem=t%10
            rev=(rev*10)+rem
            t=t//10
        if(i==rev):
            time.sleep(1)
            print("palindrome",i)

t1=threading.Thread(target=primenum,)
t2=threading.Thread(target=palindrome,)
t1.start()
t2.start()
t1.join()
t2.join()
print(".........")