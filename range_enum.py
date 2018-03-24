# Francis Adepoju, 2018-2-28
# Discovered enumerate() function
# Create a list and use it
words = ['cat', 'window', 'defenestrate', 'knowledge', 'Python']

for w in words:
    print(w, len(words))
print("Exiting raw iteration")
print(" ")

for k in range( len(words)):
    print(k, words[k], len(words[k]))
print("Exiting Split function iteration")
print(" ")

for i, j in enumerate(words):
    print(i, j, len(j))
print("Exiting enumerate version...") 
print(" ")

