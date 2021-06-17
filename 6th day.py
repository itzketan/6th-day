print("\n----------------------------------------------------- 1 ----------------------------------------------------")

# Write a Python script to merge two Python dictionaries
K = {'o': 400, 'p': 500, 'q': 600}
G = {'r': 700, 's': 800, 't': 900}
print("\n 1st Dictionary is K: ", K)
print("\n 2nd Dictionary is G: ", G)

K.update(G)
print("\n Updated Dictionary is :", K)

print("\n----------------------------------------------------- 2 ----------------------------------------------------")
# Write a Python program to remove a key from a dictionary

A = {'ITC': 207, 'IOC': 115, 'WIPRO': 500, 'M&M': 800, 'GAIL': 160, 'TATA POWER': 122}
print("\n Dictionary A Before Removing Key :", A)
del A['ITC']
print("\n Updated Dictionary After Removing Key is :", A)

print("\n----------------------------------------------------- 3 ----------------------------------------------------")

# Write a Python program to map two lists into a dictionary
K = ["ITC", "IOC", "WIPRO", "M&M", "GAIL", "TATA POWER"]
V = [207, 115, 500, 800, 160, 122]
print("K List:", K)
print("\n V List:", V)
D = dict(zip(K, V))
dict(D)
print("\n List To Dictionary :", D)
print("\n----------------------------------------------------- 4 ----------------------------------------------------")

# Write a Python program to find the length of a set
Set = {"ITC", "IOC", "WIPRO", "M&M", "GAIL", "TATA POWER"}
print("Set:", Set)
Set1 = len(Set)
print("\n Length Of A Given Set :", Set1)
print("\n----------------------------------------------------- 5 ----------------------------------------------------")

# Write a Python program to remove the intersection of a 2nd set from the 1st set
volt_meter_reading1 = {350, 480, 208, 570, 640, 790}
volt_meter_reading2 = {640, 790, 450, 370, 250, 530}
print("\n Before Removing Intersection")
print("\n 1 Volt Meter Reading :", volt_meter_reading1)
print("\n 2 Volt Meter Reading :", volt_meter_reading2)
volt_meter_reading1 .update(volt_meter_reading2)
volt_meter_reading1 -= volt_meter_reading2
print("\n After Removing Intersection")
print(" 1 Volt Meter Reading :", volt_meter_reading1)
print(" 2 Volt Meter Reading :", volt_meter_reading2)
