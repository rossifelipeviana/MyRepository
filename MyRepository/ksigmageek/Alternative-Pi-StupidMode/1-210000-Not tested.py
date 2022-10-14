import requests
import json
import time
import os
import sympy
import threading

# último valor 100000000000001

def check_palindrome(text, div):
    pi = text
    palindromo = div
    start = 0
    end = start + palindromo
    for i in range(0, len(pi) - palindromo+1):
        string = pi[start:end]

        # Check and save if find a palindrome
        if string == string[::-1]:
            print(f'O {i+1}º valor inicia o palindromo = {string}')
            with open(f'palindromos ate {ate}.txt', 'a') as reader:
                reader.write(f'O número {string} é um palíndromo.\n')
            num = int(string)
            # Check if number is prime
            if sympy.isprime(num):
                print('Esse número é primo.')
                with open(f'primos ate {ate}.txt', 'a') as reader:
                    reader.write(f' O número {num} é primo.\n')
        start = start + 1
        end = end + 1

# Definições
pi = ''
palindromo = 21
pack = 1000 // palindromo * palindromo

# Informações do arquivo
base = os.path.basename(__file__).split('-')
de = int(base[0])
ate = int(base[1][:-3])

txt_pi = f'last_pi{ate}.txt'

# Load
try:
    with open(txt_pi) as reader:
        text=reader.readlines()
        ult_it=text[-1].split(' - ')[0]
        de = int(ult_it)+1
except FileNotFoundError:
    pass

# Good luck
tempo_ini = time.time()
for i in range(de, ate):
    # Control to sanity
    if i % 1000 == 0:
        tempo_fin = time.time()
        print(f'{i} - {(tempo_fin-tempo_ini)//60}min - [{(ate-i)/(ate-de):.4%}]')
        tempo_ini = tempo_ini = time.time()

    thread = threading.Thread(target=download, args=(image,))  
    thread.start()


    # Take the number for test:
    ini = (i-1)*pack+1
    site = f'https://api.pi.delivery/v1/pi?start={ini}&numberOfDigits={pack}&radix=10'
    while True:
        try:
            resp = requests.get(site)
            if resp.status_code == 200:
                break
        except:
            pass
    stretch = resp.json()['content'][::-1]

    # Save the number and the iterate:
    with open(f'last_pi{ate}.txt', 'a') as reader:
        reader.write(f'{i} - {stretch}\n')

    # Verify if exist palindromo:
    check_palindrome(stretch, palindromo, checkprime=True)


    sympy.isprime(num)

    # Try again:
    resp = None
