def read_n_lines(n):
    lines = []
    while n != 0:
        lines.append(input())
        n -= 1
    return lines


n = int(input())
lines = read_n_lines(n)
parents = {}
for line in lines:
    l = line.split()
    if len(l) == 1:
        parents[l[0]] = []
    elif len(l) >= 3:
        i = 2
        while i < len(l):
            if l[0] not in parents:
                parents[l[0]] = []
            if l[i] not in parents[l[0]]:
                parents[l[0]].append(l[i])
            i += 1
q = int(input())
print(parents)
check = read_n_lines(q)
for line in check:
    par, cl = line.split()
    if par in parents[cl] or par == cl:
        print("Yes")
    else:
        while i < len(parents[cl]):
            search = parents[cl][i]
            if par in parents[search]:
                print("Yes")
                break
            else:
                i += 1
        if i == len(parents[cl]):
            print("No")


