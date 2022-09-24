import requests
import json
import time
import os
import sympy

import asyncio
import aiohttp

count = 0

# último valor 100000000000001
async def main():
    global de, ate
    semaphore = asyncio.Semaphore(value=5)
    tasks = []
    async with aiohttp.ClientSession() as session:
        for requisicao in range(de, ate + 1):
            tasks.append(worker(session, i))
            # tasks.append(asyncio.ensure_future(worker(session, requisicao, semaphore)))
        palin = await asyncio.gather(*tasks)
        print(palin)
        return palin


async def worker(session, requisicao, semaphore):
    global base, ate, count

    palindromo = 21
    pack = 1000 // palindromo * palindromo

    # Take the fraction of pi for test:
    ini = (requisicao - 1) * pack + 1
    site = f'https://api.pi.delivery/v1/pi?start={ini}&numberOfDigits={pack}&radix=10'

    # Headling with site
    await semaphore.acquire()
    while True:
        async with session.get(site) as resp:
            try:
                if resp.status == 200:
                    stretch = await resp.text()
                    break
            except Exception as e:
                print(e)
                pass
    semaphore.release()

    # To sanity
    count += 1
    if count % 10000 == 0:
        hora = time.ctime()
        print(f'{requisicao} às {hora}.')
        with open(f'Checkpoint {ate}.txt', 'a') as reader:
            reader.write(f'Já verifiquei até {requisicao}.\n')

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
    return


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

    asyncio.run(main())
