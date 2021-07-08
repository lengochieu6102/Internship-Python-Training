def bold(func):
    def wrapper(str):
        return '\033[1m'+ func(str) +'\033[0m'
    return wrapper
def italic(func):
    def wrapper(str):
        return '\033[3m' + func(str) +'\033[0m'
    return wrapper
def underline(func):
    def wrapper(str):
        return '\033[4m' + func(str) +'\033[0m'
    return wrapper

@underline
@italic
@bold
def chain(str):
    return str

print(chain("abc"))