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
check = read_n_lines(q)
printed = []
for line in check:
    if len(printed) == 0:
        printed.append(line)
    elif line in printed:
        print(line)
    else:
        i = 0
        flag = 0
        if len(parents[line]) != 0:
            while i < len(parents[line]):
                parent = parents[line][i]
                if parent in printed:
                    print(line)
                    flag = 1
                    break
                i += 1
        if flag == 0:
            printed.append(line)
