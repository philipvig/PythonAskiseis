fileContent = open("pythonascii.txt", "r")
with open("pythonascii.txt","r") as f:
    txt=f.readlines()
txt=str(txt)
Text=txt.split()
c=0
repeats=len(Text)-1
for i in range(repeats):
    Text[i] = Text[i].replace(".","")
    Text[i] = Text[i].replace("!", "")
    Text[i] = Text[i].replace(",", "")
    Text[i] = Text[i].replace("...", "")
    Text[i] = Text[i].replace("?", "")
    Text[i] = Text[i].replace("-", "")
    Text[i] = Text[i].replace("[", "")
    Text[i] = Text[i].replace("]", "")
    Text[i] = Text[i].replace("'", "")
    Text[i] = Text[i].replace("(", "")
    Text[i] = Text[i].replace(")", "")
    Text[i] = Text[i].replace("«", "")
    Text[i] = Text[i].replace("»", "")
    Text[i] = Text[i].rstrip("\n")
for i in range(repeats):
    j=repeats
    while j>1:
        if len(Text[i])+len(Text[j])==20:
            print(Text[i],Text[j])
            c+=1
        j=j-1
print(c)

