"""
Problem:  Python program that generates the random password

Platform : SelfStudy

Difficulty: hard

"""


import secrets
import string


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(chars) for _ in range(length))


print("Generated Password:", generate_password())
# Example Output: Generated Password: k9#P2m$vL8xQ