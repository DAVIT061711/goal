name = "hell my name is daviti"
arr = ""
all = []
for i in name:
    if i != " ":
        arr+=i
    else:
        all.append(arr)
        arr = ""

print(all)