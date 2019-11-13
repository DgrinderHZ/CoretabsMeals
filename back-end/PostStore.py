class Post:
    def __init__(self, id, photo_url, name, body):
        self.id = id
        self.photo_url = photo_url
        self.name = name
        self.body = body

posts = []

class PostStore:
    def get_all(self):
        # get all posts
        for item in posts:
            print(item.id, item.name, item.body)
            print("_______________________________")

    def add(self, post):
        # append post 
        posts.append(post)

    def get_by_id(self, id):
        # search for post by 
        result = None
        for item in posts:
            if item.id == id:
                result = item
                break
        if result == None:
            print("Post not found!")
        else:
            print(result.id, result.name, result.body)
            print("_______________________________")

    def update(self, id, photo_url, name, body):
       # update post data 
       for i in range(len(posts)):
            if posts[i].id == id:
                posts[i].photo_url = photo_url
                posts[i].name = name
                posts[i].body = body
                break


    def delete(self, id):
        # delete post by id
        result = None
        for i in range(len(posts)):
            if posts[i].id == id:
                result = i
                break
        if result == None:
            print("Post not found!")
        else:
            posts.remove(posts[result])

store = PostStore()
p1 = Post(1, "fghj", "Hassan", "okkkkkkkay")
p2 = Post(2, "hdfsv", "Zekkouri", "hhhhhhhh ")
p3 = Post(3, "bcvjkl", "Zeek Zone", "finaally")

store.add(p1)
store.add(p2)
store.add(p3)
print("Geting all:")
store.get_all()
print("Geting id = 3:")
store.get_by_id(3)
print("Edeting 1:")
store.update(1, "none", "Hassan ZEKKOURI", "Thank you Coretabs!")
print("Geting id = 1:")
store.get_by_id(1)

