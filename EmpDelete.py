# EmpDelete.py
import pickle

def deleteemp():
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
                eno=int(input("Enter Employee Number to Delete: "))

                res="NotFound"
                for ind in range(0,len(emplist)):
                    if emplist[ind][0]==eno:
                        index=ind
                        res="Found"
                        break
                if res=="Found":
                    emplist.pop(index)
                    print("\tEmp Record Removed---Verify")
                    with open("employee.data","wb")as tp:
                        for record in emplist:
                            pickle.dump(record,tp)
                else:
                    print("\tEmployee Number Does not Exist")
            except ValueError:
                print("Don't enter alnums,strs,symbols and spaces")
    except FileNotFoundError:
        print("File Does Not Exist")

