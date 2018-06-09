def isBalanced(input_string):
    opening = "[{("
    closing = "]})"
    mappings = dict(zip(opening, closing))
    stack = []
    for i in input_string:
        if i in opening:
            stack.append(mappings[i])
        elif i in closing:
            if not stack or stack.pop() != i:
                return False
    return not stack

if __name__ == "__main__":
    data = input("Enter the sequence: ")
    print(isBalanced(data))
