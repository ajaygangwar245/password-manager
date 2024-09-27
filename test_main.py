from main import login, encrypt, decrypt, show, add, delete

def test_login():
    assert login("ajay@2405") == True
    assert login("ajay@123") == False


def test_encrypt():
    assert encrypt("ajay") == "0{0n"
    assert encrypt("ajay2") == "0{0nT"
    assert encrypt("ajay3") == "0{0n*"
    assert encrypt("ajay4") == "0{0ni"


def test_decrypt():
    assert decrypt("0{0n") == "ajay"
    assert decrypt("0{0nT") == "ajay2"
    assert decrypt("0{0n*") == "ajay3"
    assert decrypt("0{0ni") == "ajay4"


def test_show():
    assert show("ajay") == "ajay"
    assert show("ajay2") == "ajay2"
    assert show("ajay6") == "User doesn't exists!"
    assert show("ajay7") == "User doesn't exists!"


def test_add():
    assert add("ajay", "ajay") == "Added successfully"
    assert add("ajay2", "ajay2") == "Added successfully"


def test_delete():
    assert delete("ajay3") == "User deleted successfully"
    assert delete("ajay4") == "User deleted successfully"
    assert delete("ajay5") == "User doesn't exists!"
    assert delete("ajay6") == "User doesn't exists!"
