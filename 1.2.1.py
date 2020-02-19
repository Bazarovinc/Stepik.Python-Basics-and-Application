objects = [int(i)for i in input().split()]
doubles = 0
for i in range(len(objects)):
    for j in range(len(objects)):
        if objects[i] == objects[j] and j != i:
            doubles += 1
print(doubles)
print(len(objects))
print(len(objects) - doubles)
