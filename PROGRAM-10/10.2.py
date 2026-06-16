try:
    num=int(input("enter a number:"))
    result=10/num
    print("result:", result)
except valuerror:
    print("error:invalid input!please enter a valid number")
except zerodivisionerror:
    print("error:Division by zero!")
                                    
