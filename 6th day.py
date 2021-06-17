print("\n----------------------------------------------------- 1 ----------------------------------------------------")

# Write a Python script to merge two Python dictionaries
K = {'o': 400, 'p': 500, 'q': 600}
G = {'r': 700, 's': 800, 't': 900}
print("\n1st Dictionary is K: ", K)
print("\n2nd Dictionary is G: ", G)

K.update(G)
print("\nUpdated Dictionary is :", K)

print("\n----------------------------------------------------- 2 ----------------------------------------------------")
# Write a Python program to remove a key from a dictionary

A = {'ITC': 207, 'IOC': 115, 'WIPRO': 500, 'M&M': 800, 'GAIL': 160, 'TATA POWER': 122}
print("\nDictionary A Before Removing Key :", A)
del A['ITC']
print("\nUpdated Dictionary After Removing Key is :", A)

print("\n----------------------------------------------------- 3 ----------------------------------------------------")

# Write a Python program to map two lists into a dictionary
K = ["ITC", "IOC", "WIPRO", "M&M", "GAIL", "TATA POWER"]
V = [207, 115, 500, 800, 160, 122]
print("K List:", K)
print("\nV List:", V)
D = dict(zip(K, V))
dict(D)
print("\nList To Dictionary :", D)
print("\n----------------------------------------------------- 4 ----------------------------------------------------")

# Write a Python program to find the length of a set
Set = {"ITC", "IOC", "WIPRO", "M&M", "GAIL", "TATA POWER"}
print("Set:", Set)
Set1 = len(Set)
print("\nLength Of A Given Set :", Set1)
print("\n----------------------------------------------------- 5 ----------------------------------------------------")

# Write a Python program to remove the intersection of a 2nd set from the 1st set
volt_meter_reading1 = {350, 480, 208, 570, 640, 790}
volt_meter_reading2 = {640, 790, 450, 370, 250, 530}
print("\nBefore Removing Intersection")
print("\n1 Volt Meter Reading :", volt_meter_reading1)
print("\n2 Volt Meter Reading :", volt_meter_reading2)
volt_meter_reading1 .update(volt_meter_reading2)
volt_meter_reading1 -= volt_meter_reading2
print("\nAfter Removing Intersection")
print(" 1 Volt Meter Reading :", volt_meter_reading1)
print(" 2 Volt Meter Reading :", volt_meter_reading2)
