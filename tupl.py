tuple=("Happy", ["Quirky", "Excited", "Disgusted"], "Sad", "Angry", "Depressed", "Mad")

# tuple[1]="Nervous"
tuple[1][2]="Weird"
# feeling=tuple[1:3]

print(tuple)

print("----------------------------------------------------------------------------------------------------------------------------")

# list=["Mahindra and Mahindra", "Tata", "Toyota", "Nissan", "Tata"]
# sed=set(list)

# sed1={"Mitsubishi", "Hundai", "Ford", "Volkswagen", "Rolls Royce", "Bentley", "Nissan", "Toyota"}

#Union of two sets
# compiled=sed|sed1
# print(compiled)

#---------------------------------------------------------------------------------

#Intersection of two sets
# common=sed&sed1
# print(common)

#---------------------------------------------------------------------------------

#Difference of two sets

# different=sed1-sed
# print(different)

#---------------------------------------------------------------------------------

#Systemic Difference of both sets

# complete_uncommon=sed^sed1
# print(complete_uncommon)

#---------------------------------------------------------------------------------

#adding data to a set
# sed.add("Mercedes Benz")
# print(sed)

#---------------------------------------------------------------------------------

#removing data from a set

# sed.remove("Nissan")
# print(sed)

#---------------------------------------------------------------------------------

#removing random data from a set

# sed.discard("Tata")
# print(sed)

#---------------------------------------------------------------------------------