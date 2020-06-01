import time
import os
import webbrowser
print('Welcome to the login centre')
time.sleep(2)
sam=input('enter a name to signup: ')
dam=input('Enter a password: ')
print('Wait were registering your information')
time.sleep(2)
print('Ok registered')
os.system('clear')
print('Welcome to your login page')
time.sleep(1)
while True:
    dd=input('Enter your username: ')
    ss=input('Enter your pssd: ')
    if dd==sam and ss==dam:
        print('succes')
        webbrowser.open('https://d-was.github.io/Cheems/')
        break

    print('try again')


    
