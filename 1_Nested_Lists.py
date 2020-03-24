if __name__ == '__main__':
    check=[];
    for _ in range(int(input())):
        name = input()
        score = float(input())
        check.append([name,score])
    first=second=100;
    for x in range(len(check)):
        if(check[x][1]>first and check[x][1]<second):
            second=check[x][1];
        elif(check[x][1]<first):
            second=first;
            first=check[x][1];
    printlist=[check[x][0] for x in range(len(check))if(check[x][1]==second)]   
    printlist.sort()    
    for name in printlist:     
        print(name)    
