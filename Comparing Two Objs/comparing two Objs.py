class computer:
    def __init__(self):
        self.name="rishad"
        self.age=21
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=computer()
c2=computer()

#c2.age=34

if c1.compare(c2):
    print("they are same")
else:
    print("they are not same")