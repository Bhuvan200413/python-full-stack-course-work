class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password= password
        self.posts=[]

    @property
    def myposts(self):
        return self.posts
    
    @myposts.setter
    def myposts(self,postname):
        self.posts.append(postname)




    def get_password(self):
        return self.__password
    
    def set_password(self,new_password):
        self.__password= new_password


bhuvan = Instagram('bhuvan','bhuvan@123')

print("Before updateing:",bhuvan.username)
bhuvan.username = 'kanukantibhuvan'
print("After updateing:",bhuvan.username)



print("Before updateing:",bhuvan.get_password())
bhuvan.set_password('kanukanti@123')
print("After updating:",bhuvan.get_password())


print(bhuvan.myposts)
bhuvan.myposts='sunset.png'
bhuvan.myposts='beach.mp4'
print(bhuvan.myposts)