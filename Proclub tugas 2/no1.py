def sekali(x):
    dict1 = {}
    arr = []
    for i in x:
        dict1[i] = dict1.get(i, 0) + 1
    for k,v in dict1.items():
        if v == 1:
            arr.append(k)
    return arr

print(sekali("76523752"))
print(sekali("1122"))
print(sekali("1234123"))