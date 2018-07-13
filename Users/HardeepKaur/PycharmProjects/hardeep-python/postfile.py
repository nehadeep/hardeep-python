from models.post import Post

from database import Database


Database.intialize()

#post = Post(blog_id="123",title="another great post2", content="my content2", author="nehadeol")
# post.content = "hardeep"  you can overrirde the content of class
posts = Post.from_blog('123')

for post in posts:
 print(posts)
#post.save_to_mongo()
