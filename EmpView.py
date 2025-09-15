# EmpView.py

import pickle
def viewall():
    try:
        with open("employee.data","rb")as fp:
            print("="*50)
            print("\t\t\tContent of Employee")
            print("="*50)
            while True:
                try:
                    emplist=pickle.load(fp)
                    for record in emplist:
                        print("\t",record,end="\t")
                    print()
                except EOFError:
                    print("="*50)
                    break
    except FileNotFoundError:
        print("File Does Not Exist")


def viewemp():
    try:
        with open("employee.data","rb")as fp:
            emplist=[]
            while True:
                try:
                    record=pickle.load(fp)
                    emplist.append(record)
                except EOFError:
                    break
            try:
                eno=int(input("Enter Employee Number to View The Records : "))
                res=False
                for record in emplist:
                    if record[0]==eno:
                        res=True
                        break
                if res:
                    print("-"*50)
                    print("\t Employee Number : ",record[0])
                    print("\t Employee Name : ",record[1])
                    print("\t Employee Salary : ",record[2])
                    print("-"*50)
                else:
                    print("\t{} Number Number Does not Exist".format(eno))
            except ValueError:
                print("Don't enter Alnums,Strs,Symbols and Spaces")

    except FileNotFoundError:
        print("File Does Not Exist")

