t = [42, 89, 91, 89]
d = [308, 1170, 1291, 1467]

def solve (t, d, res):
    res = 1
    counter_1 = 0
    for j in range(t+1):
        if j * (t - j) > d:
            counter_1 += 1
    res *= counter_1
    return res

res = 1
for (i, k) in zip(t, d):
   res = solve(i, k, res)

t_p1 = int("".join([str(t) for t in t]))
d_p1 = int("".join([str(d) for d in d]))
res = 1 
print(solve(t_p1, d_p1, res))