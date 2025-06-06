def arithmetic_operation(n):
    items = n.split()
    if items[1] == "+":
        return int(items[0]) + int(items[2])
    elif items[1] == "-":
        return int(items[0]) - int(items[2])
    elif items[1] == "*":
        return int(items[0]) * int(items[2])
    elif items[1] == "//":
        return int(items[0]) // int(items[2]) if items[2] != 0 else -1

print(arithmetic_operation(str(input("Enter an operation: "))))
