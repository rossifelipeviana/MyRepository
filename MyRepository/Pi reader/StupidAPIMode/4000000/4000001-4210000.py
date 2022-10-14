'''
First mission was check 9 prime palindrome, its is easy, all method you get the answer. So this code work.
But its not recommend by check 21 prime palindrome.

We receive the information that all number can be get by a API, so I attempted use this API.
But, of course, that have limit problem with request, mas I has thought that is ok if i just wait.
But, I gave up later...

Here exist another problem, I use the stupid brutal force to check if is prime.
'''

import requests
import json
import time
import os

# último valor 100000000000001

def check_palindrome(text, div, checkprime=False):
    pi = text
    palindromo = div
    start = 0
    end = start + palindromo
    for i in range(0, len(pi) - palindromo):
        string = pi[start:end]

        # Check and save if find a palindrome
        if string == string[::-1]:
            print(f'O {i+1}º valor inicia o palindromo = {string}')
            with open(f'palindromos ate {ate}.txt', 'a') as reader:
                reader.write(f'O número {string} é um palíndromo.\n')

            if checkprime:
                num = int(string)
                check_prime(num)
        start = start + 1
        end = end + 1


def check_prime(number):
    num = number
    if all(num % j != 0 for j in range(2, num // 2 + 1)):
        print('Esse número é primo.')
        with open(f'primos ate {ate}.txt', 'a') as reader:
            reader.write(f' O número {num} é primo.\n')
    else:
        print(f'Que pena...{num} não é primo.')

pi = ''
palindromo = 21
pack = 1000 // palindromo * palindromo

base = os.path.basename(__file__).split('-')
de = int(base[0])
ate = int(base[1][:-3])

txt_pi = f'last_pi{ate}.txt'

try:
    with open(txt_pi) as reader:
        text=reader.readlines()
        ult_it=text[-1].split(' - ')[0]
        de = int(ult_it)+1
except FileNotFoundError:
    pass

tempo_ini = time.time()

for i in range(de, ate):
    # Control to sanity
    if i % 1000 == 0:
        tempo_fin = time.time()
        print(f'{i} - {(tempo_fin-tempo_ini)//60}min - [{(i-de)/(ate-de):.4%}]')
        tempo_ini = tempo_ini = time.time()
    # Take the number for test:
    ini = (i-1)*pack+1
    site = f'https://api.pi.delivery/v1/pi?start={ini}&numberOfDigits={pack}&radix=10'
    proxy={ "https":"https://47.91.124.200:22106"}
    while True:
        try:
            resp = requests.get(site, headers={'User-Agent': 'Mozilla/5.0'}, proxies=proxy)
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

    # Try again:
    resp = None
