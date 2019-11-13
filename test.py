# allowed papers: 100, 50, 10, 5, and rest of request
'''money = 500
request = 277
papers = [100, 50, 10, 5]

if request <= money:
    money -= request
    paper = 0
    while request > 0:
        while(request >= papers[paper]):
            print("give", papers[paper])
            request -= papers[paper]
        paper += 1
        if paper == len(papers) and request != 0:
            print("give", request)
            request = 0
else:
    print("Request less!")'''

def withdraw(balance, request):
    # allowed papers: 100, 50, 10, 5, and cents
    if request > balance:
        print("Can't give you all this money !!")
    elif request < 0:
        print("More than zero plz!")
    else:
        balance = balance-request
        while request > 0:
            if request >= 100:
                request -= 100
                print("give 100")
            elif request >= 50:
                request -= 50
                print("give 50")
            elif request >= 10:
                request -= 10
                print("give 10")
            elif request >= 5:
                request -= 5
                print("give 5")
            elif request < 5:
                print("give " + str(request))
                request = 0
    return balance

# Execution
balance = 500
print("fisrt call________________")
balance = withdraw(balance, 277)
print("second call________________")
balance = withdraw(balance, 30)
print("third call________________")
balance = withdraw(balance, 5)
print("fourth call________________")
balance = withdraw(balance, 500)
