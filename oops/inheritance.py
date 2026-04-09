class InstagramV1:
    def reel(Self):
        print("You can post the reel")

class InstagramV2(InstagramV1):
    def story(Self):
        print("You can post the story")

class InstagramV3(InstagramV2):
    def note(Self):
        print("You can post the thoughts")

class meta:
    def ai(Self):
        print("You can use AI to create content")

class crossplatform:
    def integrating(self):
        print("You can integrate with whatsapp and facebook")

class InstagramV4(meta,crossplatform,InstagramV3):
    def repost(Self):
        print("You can repost the content")

print('Prudhvi - InstagramV1---------------')
prudhvi = InstagramV1()
prudhvi.reel()

print('Nandhan - InstagramV2---------------')
nandhan = InstagramV2()
nandhan.reel()
nandhan.story()

print('Bhuvan - InstagramV3---------------')
bhuvan = InstagramV3()
bhuvan.reel()
bhuvan.story()
bhuvan.note()

print('Sumanth - InstagramV4---------------')
sumanth = InstagramV4()
sumanth.reel()
sumanth.story()
sumanth.note()
sumanth.ai()
sumanth.integrating()
sumanth.repost()  