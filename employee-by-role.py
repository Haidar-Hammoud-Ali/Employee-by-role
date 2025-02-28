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
            