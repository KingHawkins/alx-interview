def pascal_triangle(n):
    """
    Calculates the pascal triangle
    """
    if n <= 0:
        return []
    else:
        (array, fib) = ([], [[1]])
        while len(fib) < n:
            (arr, item) = ([1], fib[-1])
            for i in range(0, len(item)):
                if i+1 != len(item):
                    arr.append(item[i] + item[i + 1])
            arr.append(1)
            fib.append(arr)
        return fib
