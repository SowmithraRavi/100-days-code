t=int(input())
for i in range(t):
    salary=int(input())
    if(salary<1500): 
        hra=salary*(10/100)
        da=salary*(90/100)  
        gross_salary=salary+hra+da
        print(gross_salary)
    else:
        hra=500
        da=salary*(98/100) 
        gross_salary=salary+hra+da
        print(gross_salary)
