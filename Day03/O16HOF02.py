
def bankFlow(fnc):
    print("=" * 60)
    print("login....")
    fnc()
    print("Logout....")
    print("-" * 60)

def deposit():
    print("credited.....")

def withdraw():
    print("debited.....")


bankFlow(deposit)
bankFlow(withdraw)