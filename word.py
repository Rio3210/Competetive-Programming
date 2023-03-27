txt=input()
lower=0
upper=0
for i in txt:
      if(i.islower()):
            lower+=1
      else:
            upper+=1
if lower>=upper:
    print(txt.lower())
else:
    print(txt.upper())
