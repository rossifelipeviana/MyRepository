'''
The text (pi number) must be extracted using it: http://www.numberworld.org/y-cruncher/#Download

I remove the function to do the verification, cause this spend resource to call function,
so to long tasks is better a linear script without function.
Maybe I should have taken a big piece and splitted it. But I didn't have time for it.

(1000000 letter in 2,5 seconds)
'''

import os
import sympy
import time
import threading
import concurrent.futures

path = r"C:\Users\rossi\Desktop\y-cruncher v0.7.10.9513\ycds\0.txt"
palindromo = 21

print('Hello')

# thread = threading.Thread(target=worker, args=(path, palindromo))
# thread.append(thread)
# thread.start()

with open(path, 'r') as texto:
    stretch = ''
    t0 = time.perf_counter()
    count = 0
    while True:
        # To sanity
        count += 1
        if count % 100000000 == 0:
            with open('checkpoint.txt', 'w') as checkpoint:
                checkpoint.write(f'Feito até {count}.\n')
            try:
                tf = time.perf_counter() - t0
                print(f'{count} em {tf/60:.2f} minutos [{count/10000000000:.2%}]')
                t0 = time.perf_counter()
            except:
                pass
        ##############################################################
        # Check if the stretch is least that 21.
        ##############################################################
        while len(stretch) <= palindromo:
            try:
                stretch += texto.read(1)
            except Exception as e:
                print('e')
                break
        # Check if the stretch is greater that 21.
        if len(stretch) > 21:
            stretch = stretch[1:]
        ##############################################################
        # # Sem chamar função (1000000 em 2,5 segundos)
        ##############################################################
        if stretch == stretch[::-1]:
            with open(f'Palindromos.txt', 'a') as reader:
                reader.write(f'O número {stretch} é um palíndromo.\n')
            num = int(stretch)
            # Check if number is prime.
            if sympy.isprime(num):
                # print(f'{num} é primo.')
                with open(f'Primos.txt', 'a') as reader:
                    reader.write(f' O número {stretch} é primo.\n')
