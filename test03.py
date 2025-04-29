import sepp03 as s3

def add_beneficiary_valid():
    assert s3.add_beneficiary("abc","123456789") == "beneficiary added"

def view_beneficiary_invalid():
    assert s3.view_beneficiary("def") == "not found"

def fund_transfer_success():
    assert s3.fund_transfer("abc",30000) == "Transfer successful"