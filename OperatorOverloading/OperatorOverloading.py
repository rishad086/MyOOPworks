class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self, other):
        if s3.m1 > s3.m2:
            return True


s1=student(34,45)
s2=student(32,37)
s3=s1+s2

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")



print(s3.m1)

