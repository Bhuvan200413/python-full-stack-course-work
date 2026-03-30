likes = 0
comments = []

def addlike():
    global likes
    likes += 1
    return likes

def addcomments(com):
    comments.append(com)
    return comments