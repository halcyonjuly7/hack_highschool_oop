
def arrToNum(arr):
    out = 0
    for i in range(len(arr)):
        out += arr[i]
        if i < len(arr) - 1:
          out *= 10
    return out

def baseConverter(decNum, base):
    out = []
    while decNum > 0:
        out.append(decNum % base)
        decNum //=  base
    return arrToNum(out[::-1])

if __name__ == "__main__":
    number = input("Enter the decimal number: ")
    base = input("Enter the base: ")
    print(baseConverter(int(number), int(base)))
