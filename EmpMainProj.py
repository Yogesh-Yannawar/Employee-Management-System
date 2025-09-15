# EmpMainProj.py
from EmpSearch import searchemp
from EmpView import viewemp,viewall
from EmpDelete import deleteemp
from EmpAdd import addemp
from EmpMenu import menu
from EmpUpdate import updateemp

while True:
    menu()
    ch=int(input("Enter Your Choice : "))
    match ch:
        case 1:
            addemp()
        case 2:
            deleteemp()
        case 3:
            updateemp()
        case 4:
            viewemp()
        case 5:
            viewall()
        case 6:
            searchemp()
        case 7:
            print("Thanks for Using This Application")
            break
        case _:
            print("Your Selection of Operation Was Wrong try Again")


