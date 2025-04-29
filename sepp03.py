beneficiary = {}

def add_beneficiary(name,account_number):
    if name in beneficiary:
        return "beneficiary already exists"
    else:
        beneficiary[name] = account_number
        return "beneficiary added"

def view_beneficiary(name):
    if name in beneficiary:
        return f"{name} : {beneficiary[name]}"
    return "not found"

def fund_transfer(name,amount):
    if name in beneficiary and amount > 0:
        return "Transfer successful"
    return "Transfer failed"

# if __name__=='__main__':
#     name = "abcd"
#     account = "63621111"
#     print(add_beneficiary(name,account))
#     name = "abcd"
#     print(view_beneficiary(name))
#     amount = -2
#     print(fund_transfer(name,amount))
