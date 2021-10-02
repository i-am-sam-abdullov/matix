matrica1 = []
while True:
    s = input()
    if s == 'end':
        break
    matrica1.append([int(i) for i in s.split(' ')])

height = len(matrica1)
width = len(matrica1[0])
for i in range(0, height):
    top = i - 1 if i - 1 >= 0 else height - 1
    bottom = i + 1 if i + 1 < height else 0

    for j in range(0, width):
        left = j - 1 if j - 1 >= 0 else width - 1
        right = j + 1 if j + 1 < width else 0
        s = matrica1[top][j] + matrica1[bottom][j] + matrica1[i][left] + matrica1[i][right]
        print(s, end=' ')
    print()