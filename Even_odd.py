evencount = 0
oddcount = 0
squaresum = 0
cubesum = 0

for i in range(1, 11):
    if i % 2 == 0:
        print("even")
        print(i, i*i, i*i*i)

        squaresum = squaresum + i*i
        cubesum = cubesum + i*i*i

        evencount = evencount + 1

    else:
        print("odd")
        print(i, i*i, i*i*i)

        squaresum = squaresum + i*i
        cubesum = cubesum + i*i*i

        oddcount = oddcount + 1

