import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

def names_in_common(list1, list2): # creating a function which will take in our 2 lists
    first_set = set(list1) # creating sets out of lists so we can use the set specific method later
    second_set = set(list2) 

    if len(first_set.intersection(second_set)) > 0: # using .intersection method (given by set) to check if their common values are greater than 0, if so run it
        return(first_set.intersection(second_set)) # return the common values of these arrays

duplicates = names_in_common(names_1, names_2) # use the function within this variable on our 2 lists

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

