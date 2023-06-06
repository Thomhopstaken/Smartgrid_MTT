rows, cols = (50, 50)
arr = [["_" for i in range(cols)] for j in range(rows)]

arr[0][1] = "A"
for row in arr:
    print(*row)

