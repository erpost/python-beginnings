data = "From stephen.marguard@uct.ac.za Sat Jan 5 09:14:16 2008"

atposition = data.find("@")
print(atposition)

spaceposition = data.find(" ", atposition) # finds the next space after the @ sign
print(spaceposition)

print(data[atposition + 1 : spaceposition])