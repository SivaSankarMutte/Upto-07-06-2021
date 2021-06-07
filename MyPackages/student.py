class student:
    def __init__(self,rno,name):
        self.name=name
        self.rno=rno
        print("ROLL NO is:",self.rno)
        print("Name is:",self.name)
    def getFName(self,name):
        return name.split()[0]
def details(r,n):
    obj=student(r,n)
    print("First Name is:",obj.getFName(n))