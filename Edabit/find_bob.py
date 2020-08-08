def find_bob(names):
    targetName = "Bob"
    
    if names.count("Bob") != 0:
        return names.index("Bob")
    else:
        return -1 

#Testing 
print(find_bob(["Jimmy", "Layla", "Mandy"]))
print(find_bob(["Bob", "Nathan", "Hayden"]))
print(find_bob(["Paul", "Layla", "Bob"]))
print(find_bob(["Garry", "Maria", "Bethany", "Bob", "Pauline"]))




