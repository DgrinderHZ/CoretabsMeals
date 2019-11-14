from PostStore import *
store = PostStore()
p1 = Post(1, "fghj", "Hassan", "okkkkkkkay")
p2 = Post(2, "hdfsv", "Zekkouri", "hhhhhhhh ")
p3 = Post(3, "bcvjkl", "Zeek Zone", "finaally")

store.add(p1)
store.add(p2)
store.add(p3)
print("Geting all:")
result = store.get_all()
for item in result:
    print(item.id, item.name, item.body)
    print("_______________________________")

print("Geting id = 3:")
result = store.get_by_id(3)
if result == None:
    print("Post not found!")
else:
    print(result.id, result.name, result.body)
    print("_______________________________")

print("Edeting 1:")
store.update(1, "none", "Hassan ZEKKOURI", "Thank you Coretabs!")
print("Geting id = 1:")
result = store.get_by_id(1)
if result == None:
    print("Post not found!")
else:
    print(result.id, result.name, result.body)
    print("_______________________________")

