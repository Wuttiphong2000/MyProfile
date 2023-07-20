import random

print('your password: ')

chars = '12134567890qwertyuiopasdfghjklzxcvbnm'

password = ''
for x in range(10):
    password += random.choice(chars)

print(password)