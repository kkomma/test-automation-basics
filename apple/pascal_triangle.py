def print_pascals_triangle(n):
    triangle = [[1 for _ in range(i+1)] for i in range(n)]
    print(triangle)

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    for row in triangle:
        print(' '.join(str(num) for num in row))

print_pascals_triangle(5)