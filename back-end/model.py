class Post:
    def __init__(self, name, photo, content):
        self.name = name
        self.photo_url = photo
        self.content = content
    def toString(self):
        print("[Name:", self.name, ", Photo url:", self.photo_url, ",\nContent:", self.content, ", Type:", type(self), "]")


class App:
    posts = []
    def __init__(self, name, logo):
        self.name = name
        self.logo_url = logo
    def add_new_post(self, post):
        self.posts.append(post)
    def show_posts(self):
        for item in self.posts:
            item.toString()
            print("____________________________________________________")


# Post test
post1 = Post("Hassan Zekkouri", "http://bit.ly/34TIVNW", 
            "I am learning to become a Full Stack web developper with Coretabs Academy.")
# App test
blog = App("Facebook like", "logo")
blog.add_new_post(post1)
blog.add_new_post(post1)
blog.show_posts()
print(blog.posts)

