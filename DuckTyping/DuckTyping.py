class Pycharm:
    def execute(self):
        print("compiling")
        print("runnoing")
class MyEditor:
    def execute(self):
        print("spell check")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=Pycharm()
lap1=Laptop()
lap1.code(ide)