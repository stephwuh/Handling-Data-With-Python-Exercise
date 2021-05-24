open_file = open("CupcakeInvoices.csv")

# number 3

for line in open_file:
    print(line)

# number 4 

for line in open_file:
    x = line.split(",")
    print(x[2])

# number 5

for line in open_file:
    x = line.split(",")
    y = float(x[3]) * float(x[4])
    print(y)

# number 6

sum = 0

for line in open_file:
    x = line.split(",")
    y = float(x[3]) * float(x[4])
    sum += y

print(sum)




# further study

chocolate = 0
vanilla = 0
strawberry = 0

for line in open_file:
    x = line.split(",")
    y = float(x[3]) * float(x[4])
    if x[2]=="Chocolate":
        chocolate+=y
    elif x[2]=="Vanilla":
        vanilla+=y
    elif x[2]=="Strawberry":
        strawberry+=y

print(chocolate)
print(vanilla)
print(strawberry)


open_file.close()