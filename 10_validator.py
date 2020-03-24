if __name__ == '__main__':
    s = input()
    an=a=n=lo=up=False
    for x in range(len(s)):
        ch=s[x]
        if(ord(ch)>=65 and ord(ch)<=90):
            an=True
            a=True
            up=True
        elif(ord(ch)>=97 and ord(ch)<=122):
            an=True
            a=True
            lo=True
        elif(ord(ch)>=48 and ord(ch)<=57):
            an=True
            n=True
    print(an,a,n,lo,up,sep='\n')        
