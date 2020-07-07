
dicpe = {"part" : "a",
"vendor" : "python",
"product" : "python",
"version" : 3.6,
"Update" : "",
"Edition" : "",
"Language" : "",
"Software" : "",
"Target_Software" : "",
"Target_Hardware" : "",
"Other" : ""}

for x in dicpe:
    if dicpe[x] == "":
        dicpe[x] = "*"
print(dicpe)
cpe23 = "cpe:2.3:"+ ':'.join(str(x) for x in dicpe.values())

print(cpe23)
