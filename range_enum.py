# Francis Adepoju, 2018-2-28
# Discovered enumerate() function

# Create a list and use it
words = ['cat', 'window', 'defenestrate', 'knowledge', 'Python']

# Iterate through the List object in a natural way
for w in words:
    print(w, len(words))
print("Exiting raw iteration")
print(" ")

# Using the range keyword to iterate between a list object
for k in range( len(words)):
    print(k, words[k], len(words[k]))
print("Exiting Split function iteration")
print(" ")

# Yet another way of achieving the above result using inbuilt function enumerate
for i, j in enumerate(words):
    print(i, j, len(j))
print("Exiting enumerate version...") 
print(" ")

