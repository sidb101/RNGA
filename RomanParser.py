import re
def validity(S):
    pattern = r'M{0,3}(CD|CM|D?C{0,3})(XL|XC|L?X{0,3})(IV|IX|V?I{0,3})'
    return True if re.search(pattern,src) else False

if __name__=='__main__':
    src = input("Enter input string: ")
    print("A valid Roman string!" if validity(src) else "Invalid Roman string")
    x = input("Press Enter to exit: ")
