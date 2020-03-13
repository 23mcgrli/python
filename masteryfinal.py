name = input("What is your first name? ")
namel = input("What is your last name? ")
ID = int(input("What is your Student ID? "))
x = 0
sche = f"*************************************************\n*                                               *\n*      {namel},{name}           ID:{ID}         *\n*                                               *\n*************************************************"
print (f"*************************************************\n*                                               *\n*      {namel},{name}           ID:{ID}         *\n*                                               *\n*************************************************")
while True:
    class1 = input ("what is you class ")
    if class1 == "stop":
        break
    rm1 = int(input ("what is the room number "))
    x += 1
    sche += (f"\n*\tblock {x}:{class1} room:{rm1}\t\t*")
    
print (sche)
print ("*                                               *\n*************************************************")