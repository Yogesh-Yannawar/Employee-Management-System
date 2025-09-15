# EmpAdd.py
import pickle

def uniquevalues(empno):
    with open("employee.data","rb")as rp:
        emplist=[]
        while True:
            try:
                record=pickle.load(rp)
                emplist.append(record)
            except EOFError:
                break
        duplicate=False
        for record in emplist:
            if record[0]==emplist:
                duplicate=True
        return duplicate

# Creating Class Of Exception -- providing Friendly Errors
class SpaceError(Exception):pass
class ZeroLengthNameError(BaseException):pass
class InvalidNameError(Exception):pass

# Now Validating the Name
def validation(name):
    if len(name)==0:
        raise ZeroLengthNameError
    elif name.isspace():
        raise SpaceError
    else:
        words=name.split()
        res=True
        for word in words:
            if not word.isalpha():
                res=False
                break
        if res:
            return name
        else:
            raise InvalidNameError

def addemp():
    with open("employee.data","ab")as fp:
        while True:
            try:
                print("-"*50)
                eno=int(input("Enter Employee Number : "))
                name=validation(input("Enter Employee Name : "))
                sal=float(input("Enter Employee Salary : "))
                print("-"*50)
                emplist=[]
                emplist.append(eno)
                emplist.append(name)
                emplist.append(sal)

                # Now verifying Duplicates data
                dup=uniquevalues(eno)
                if (not dup):
                    pickle.dump(emplist,fp)
                    print("\tEmp Record Saved in a File")
                    print("-"*50)
                else:
                    print("\t{} Employee Number Already Exist".format(eno))
                ch=input("Do you Want to Enter Another Employee Record(yes/no): ").lower()

                if ch=='no':
                    break

            except ValueError:
                print("Don't enter Alnums,Symbols,Str & Spaces")
            except SpaceError:
                print("Don't Enter Spaces for Name")
            except ZeroLengthNameError:
                print("Try to Enter a Name")
            except InvalidNameError:
                print("Invalid Name--Try Again")

