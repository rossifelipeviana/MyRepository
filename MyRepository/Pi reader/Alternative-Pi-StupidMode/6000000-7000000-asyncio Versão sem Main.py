import requests
import json
import time
import os
import sympy
import threading
import concurrent.futures

import asyncio
import aiohttp
from aiolimiter import AsyncLimiter

count = 0

# último valor 100000000000001
async def worker():
    global de, ate, count

    palindromo = 21
    pack = 1000 // palindromo * palindromo

    # Headling with site
    async with aiohttp.ClientSession() as session:
        for requisicao in range(de, ate + 1):
            # Take the fraction of pi for test:
            ini = ((requisicao - 1) * pack) + 1
            site = f'https://api.pi.delivery/v1/pi?start={ini}&numberOfDigits={pack}&radix=10'
            while True:
                async with session.get(site) as resp:
                    try:
                        if resp.status == 200:
                            stretch = await resp.text()
                            break
                    except Exception as e:
                        print(e)
                        pass
            # To sanity
            count += 1
            if count % 10000 == 0:
                hora = time.ctime()
                print(f'{requisicao} às {hora}.')
                with open(f'Checkpoint {ate}.txt', 'a') as reader:
                    reader.write(f'Já verifiquei até {requisicao}.\n')

            # Loop in stretch
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
    ate = int(base[1])

    # Load
    txt_pi = f'last_pi{ate}.txt'
    try:
        with open(txt_pi) as reader:
            text = reader.readlines()
            ult_it = text[-1].split(' - ')[0]
            de = int(ult_it) + 1
    except FileNotFoundError:
        pass

    # Método 1
    # with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    #     gold = executor.map(worker, range(de, ate+1))

    # Método 2
    asyncio.run(worker())
