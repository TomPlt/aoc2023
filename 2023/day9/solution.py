seq = open("data.txt").read().split("\n")
seqs = [[int(j) for j in i.split()] for i in seq]

res_p1 = 0
res_p2 = 0
for seq in seqs: 
    temp_seq = [seq]
    while sum(temp_seq[-1]) != 0: 
        seq = [j-i for i, j in zip(seq[:-1], seq[1:])]
        temp_seq.append(seq)
    extrapolated = 0
    for i in temp_seq[::-1]:
        extrapolated = i[0] - extrapolated
    res_p2 += extrapolated
    res_p1 += temp_seq[0][-1] + sum([i[-1] for i in temp_seq[1:]])
print(res_p1, res_p2)

# part 2


