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
            if l[i] in parents:
                parents[l[i]].append(l[0])
            else:
                parents[l[i]] = []
                parents[l[i]].append(l[0])
            i += 1
        if l[0] not in parents:
            parents[l[0]] = []
q = int(input())
check = read_n_lines(q)
for line in check:
    cl_par = line.split()
    if cl_par[1] in parents[cl_par[0]]:
        print("Yes")
    else:
        print('No')
