a=5
b=0
try:
    print("program is opened")
    print(a/b)
except ZeroDivisionError as e:
    print(" Can not divide a Number by zero")
except ValueError as e:
    print("Invalid Input")
except Exception as e:
    print("something is wrong")
finally:
    print("program is closed")