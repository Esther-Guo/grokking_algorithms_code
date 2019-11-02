vote = {}
def check(name):
    if vote.get(name):
        print(f"{name}, u already voted")
    else:
        vote[name]=True
        print(f"{name}, pls vote")

check("jack")
check("trismile")
check("trismile")