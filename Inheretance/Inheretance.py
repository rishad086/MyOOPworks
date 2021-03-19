class a:
    def feature1(self):
        print("feature1 is working")
class b(a):
    def feature2(self):
        print("feature1 is working")

    def feature3(self):
        print("feature1 is working")

c1=a()
c2=b()
c2.feature1()
    