# EmpSearch.py

import pickle
def searchemp():

    empno=int(input("Enter Employee Number : "))
    emplist=[]
    with open("employee.data","rb")as fp:
        while True:
            try:
                record=pickle.load(fp)
                emplist.append(record)
            except EOFError:
                break

        res="NotFound"
        for emprec in emplist:
            if emprec[0]==empno:
                res="Found"
                break
        if res=="Found":
            print("\t{} Employee Number Exist".format(empno))
        else:
            print("\t{} Employee NUmber Does Not Exist".format(empno))

