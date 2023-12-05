import ast 

with open("data.txt") as f: 
    lines = f.read().split("\n\n")

max_val = 0
vals = []
for line in lines: 
    line = line.replace("\n", ",")
    line = ast.literal_eval(line)
    val = line if isinstance(line, int) else sum(list(line))
    vals.append(val)
    max_val = max(max_val, val)

print(max_val)
print(sum(sorted(vals)[-3:]))