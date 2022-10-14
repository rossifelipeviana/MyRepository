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
import sympy
import threading
import concurrent.futures

# último valor 100.000.000.000.001
#                        1.000.000 milhão
#                    1.000         bilhão
# 
def worker(requisicao):
    global de, ate, count
    # To sanity
    if count % 10000 == 0:
        try:
            duracao = time.time() - time_init
            print(f'{count} em {duracao//60:.4f} [{(requisicao-de)/(ate-de):.4%}].')
        except UnboundLocalError:
            print(f'{count} as {time.ctime()}.')
        except Exception as e:
            print(e)
        with open(f'Checkpoint {ate}.txt', 'a') as reader:
            reader.write(f'Já verifiquei até {de+count}.\n')
        time_init = time.time()

    # Definitions
    palindromo = 21
    pack = 1000 // palindromo * palindromo

    # Take the fraction of pi for test:
    ini = (requisicao - 1) * pack + 1
    site = f'https://api.pi.delivery/v1/pi?start={ini}&numberOfDigits={pack}&radix=10'

    # Headling with site
    while True:
        try:
            resp = requests.get(site, headers={'User-Agent': 'Mozilla/5.0'})
            if resp.status_code == 200:
                break
        except:
            pass

    stretch = resp.json()['content']
    count += 1

    start = 0
    end = start + palindromo
    for i in range(0, len(stretch) - palindromo + 1):
        string = stretch[start:end]

        # Check and save if find a palindrome
        if string == string[::-1]:
            print(f'O {i+1}º valor inicia o palindromo = {string}')
            with open(f'palindromos ate {ate}.txt', 'a') as reader:
                reader.write(f'O número {string} é um palíndromo.\n')
            num = int(string)
            # Check if number is prime
            if sympy.isprime(num):
                print(f'{num} é primo.')
                with open(f'primos ate {ate}.txt', 'a') as reader:
                    reader.write(f' O número {num} é primo.\n')
        start = start + 1
        end = end + 1


if __name__ == '__main__':
    # Informações do arquivo
    base = os.path.basename(__file__).split('-')
    de = int(base[0])
    count = 0
    if len(base) == 2:
        ate = int(base[1][:-3])
    else:
        ate = int(base[1])
    # Load
    txt_pi = f'Checkpoint {ate}.txt'
    try:
        with open(txt_pi) as reader:
            text = reader.readlines()
            ult_lin = text[-1]
            ult_word = ult_lin.split(' ')[-1]
            ult_it = ult_word[:-2]
            de = int(ult_it) + 1
    except FileNotFoundError:
        pass

    # Método 1
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        gold = executor.map(worker, range(de, ate + 1))

    with open('result.txt', 'a') as result:
        result.write('a')
        result.write('#'.join(gold))
