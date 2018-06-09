

def revKElements(input_string, k):
    if input_string:
        casted_items = [int(i) for i in items.split(",")]
        revved = list(reversed(casted_items[:k]))
        return ",".join([str(i) for i in revved + casted_items[k:]])


if __name__ == "__main__":
    items = input("Enter the list of numbers: ")
    items_to_reverse = int(input("Enter k: "))
    print(revKElements(items, items_to_reverse))
