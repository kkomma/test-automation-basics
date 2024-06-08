import string
import random

def generate_pwd(pwdLength):
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ''.join(random.choice(chars) for i in range(pwdLength))
    return pwd

# Example usage
pwdLength = 16
pwd = generate_pwd(pwdLength)
print(pwd)