employee={}
while True:
    name= input("Enter employee name, and 'exit' to stop: ")
    if name.lower ()== "exit":
        break
    while True:
        age= input ("Provide employee age: ")
        if age.isdigit ():
            age=int(age)
            break
        else:
            print ("Enter a valid age: ")
    role= ("Provide the employee position: ")
    if role not in employee:
        employee[role]=[]
    employee[role].append({"name":name, "age":age})

    print (employee)

total_employee=sum (len (x)for x in employee.values())
print (f"The total numbers of employees in this company is: {total_employee}")
