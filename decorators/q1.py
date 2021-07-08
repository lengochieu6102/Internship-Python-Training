def decor_check(func):
    def first_failure():
        print("You enter wrong password or user name. 2 attempts left")
    def second_failure():
        print("You enter wrong password or user name. 1 attempts left")
    def third_failure():
        print("You enter wrong password or user name. Please try later")

    
    def wrapper(username,password):
        if username=="hieu" and password=="123":
            print("Login successful")
            func()
            return True
        else:
            if  wrapper.failed==0:
                first_failure()
                wrapper.failed +=1
                return False
            elif wrapper.failed==1:
                second_failure()
                wrapper.failed +=1
                return False
            else:
                third_failure()
                return True
    wrapper.failed = 0
    return wrapper

@decor_check
def hello():
    print("Hello World")

while True:
    print("Enter username: ")
    username =input()
    print("Enter password: ")
    password=input()
    if hello(username,password):
        break