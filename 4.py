import random
fileContent = open("pythonascii.txt", "r")
with open("pythonascii.txt","r") as f:
    txt=f.readlines()
txt=str(txt)
Text=txt.split()
repeats=(len(Text))
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
    Text[i]=Text[i].rstrip("\n")
words=[]
space=" "
for i in range(repeats):
    for j in range(repeats-1):
        words.append(Text[i]+space+Text[j]+space+Text[j+1])

newrepeats=len(words)
finaltext=[]
c=0

i=0
while i<=newrepeats and c<=200:
    randomwords=random.choice(words)
    last2words=randomwords.split()[-2:]
    j=0
    while (j<=newrepeats-1):
        first2words = words[j].split()[:2]
        if (last2words == first2words):
            finaltext.append(words[j])
            c=c+1

        j+=1
i+=1
finaltxt= finaltext[0]
for i in range(1,c):
    finaltxt=finaltxt+space+finaltext[i]
print(finaltxt)

