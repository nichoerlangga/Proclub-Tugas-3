def mostAppear(x):
    dict1 = {}
    a = ""
    for i in x:
        dict1[i] = dict1.get(i, 0) + 1
    dict1 = sorted(dict1.items(), key = lambda kv: kv[1])
    for k,v in dict1:
        a += k + ": " + str(v) + "\n"
    return a

print(mostAppear(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
print(mostAppear(["danu", "danu", "alif", "indra", "indra", "kurniadi", "indra"]))