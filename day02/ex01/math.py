
def total(stack):
    return len(stack)

def _sum(stack):
    return sum(stack)

def _product(stack):
    prod = 1
    for i in stack:
        prod *= i
    return prod

def _mean(stack):
    return len(stack) // 2


def _min(stack):
    return min(stack)

def _max(stack):
    return max(stack)



if __name__ == "__main__":
    data = input("Enter the numbers: ")
    stack = [int(i) for i in data.split(",")]
    print(f"""
    Total Count = {total(stack)}
    Sum = {_sum(stack)}
    Product = {_product(stack)}
    Mean = {_mean(stack)}
    Min = {_min(stack)}
    Max = {_max(stack)}
    """)


