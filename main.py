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

def add(*args: int) -> int:
    return sum(args)
def multiply(a: float, b: float) -> float:
    return a * b
if __name__ == "__main__":
    print(greet("Stranger"))
    print(parse_email("user@example.com"))
    print(add(5, 10))
    print(multiply(2.5, 4.0))
