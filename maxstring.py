def findmajority(x,y):
    
    maxCount = 0
    index = -1 
    for i in range(y): 
      
        count = 0
        for j in range(y): 
          
            if(x[i] == x[j]): 
                count += 1

        if(count > maxCount): 
          
            maxCount = count 
            index = i 
      
    if (maxCount > y//2): 
        print("Majority element is ", x[index])
      
    else: 
        print("Majority Element does not exist")
    
    
    
    
x1=input("print array values")
x=x1.split()
print(x)

y=int(input("enter array length"))
findmajority(x,y)    
