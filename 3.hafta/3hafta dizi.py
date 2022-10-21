
list = ["as", True, 1.9, 5, ["asdsa", "sdf", "asssadsa"]]
for i in list:
    print(i)
for i in list[4]:
    print(i)

#*********************************

for i in range(0, 3):
    print(i)
else:
    print("for bitti")


#**********************************
for i, eleman in enumerate(list):
    print(i+1, ". eleman :", eleman, sep="")

