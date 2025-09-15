# EmpUpdate.py
import pickle

from EmpAdd import validation,SpaceError,ZeroLengthNameError,InvalidNameError

def updateemp():
    try:
        print("-"*40)
        eno=int(input("Enter Employee Number to Update emp Name and Sal:"))
        ename=validation(input("Enter Ur Correct Name : "))
        esal=float(input("Enter ur New Salary : "))
        print("-"*40)
        try:
            with open("employee.data","rb")as fp:
                emplist=[]
                while True:
                    try:
                        record=pickle.load(fp)
                        emplist.append(record)
                    except EOFError:
                        break
            res = "NotFound"
            for ind in range(len(emplist)):
                if (emplist[ind][0] == eno):
                    index = ind
                    res = "Found"
                    break
            if (res):
                emplist[index][1] = ename
                emplist[index][2] = esal
                print("\tEmployee Data Updated Verify")
                print('-'*40)
                with open("employee.data", "wb") as fp:
                    for record in emplist:
                        pickle.dump(record, fp)
            else:
                print("\tEmployee Number Does Not Exist-Can't Update")

        except FileNotFoundError:
            print("File Does Not Exist")
    except ValueError:
        print("Don't enter Alnums,Symbols,Str & Spaces")
    except SpaceError:
        print("Don't Enter Spaces for Name")
    except ZeroLengthNameError:
        print("Try to Enter a Name")
    except InvalidNameError:
        print("Invalid Name--Try Again")







