import multiprocessing,time
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
if(__name__=='__main__'):
    p1=multiprocessing.Process(target=primenum,)
    p2=multiprocessing.Process(target=palindrome,)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(".........")