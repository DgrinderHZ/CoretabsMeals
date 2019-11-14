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
        return posts
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
        return result

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

