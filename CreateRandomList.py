import random
def randomList(countUser):
    userList = []
    for i in range(countUser):
        userList.append(random.randint(0,10))
    return userList
