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
updated_fields = {'name': 'Maryam',
                  'photo_url': 'https://images.pexels.com/photos/736716/pexels-photo-736716.jpeg?auto=compress&cs=tinysrgb&dpr=1&h=100&w=100',
                  'body': 'Lorem Ipsum'}
store.update(1, updated_fields)
print("Geting id = 1:")
result = store.get_by_id(1)
if result == None:
    print("Post not found!")
else:
    print(result.id, result.name, result.body)
    print("_______________________________")

print("Deleting 2")
store.delete(2)
print("After Deletion:")
print("Geting all:")
result = store.get_all()
for item in result:
    print(item.id, item.name, item.body)
    print("_______________________________")

