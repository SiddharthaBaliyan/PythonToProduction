#test
from typing import TypedDict
class UserInfo(TypedDict):
    name:str
    age:int

user = UserInfo(name="Alice", age=30)
print(user["name"])  
print(user["age"])
def greet(name):
    return f"Hello, {name}!"
##Type HINTING SYNTAX
def parse_email(email_address: str) -> str | None:
    if "@" in email_address:
        username, domain = email_address.split("@")
        return username
    return None
if __name__ == "__main__":
    print(greet("Stranger"))
    print(parse_email("user@example.com"))
