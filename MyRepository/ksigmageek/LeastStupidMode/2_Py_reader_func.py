'''
The text (pi number) must be extracted using it: http://www.numberworld.org/y-cruncher/#Download

Second attempt, here I attempt a easy method, but slower.
I open the file and get 1 letter and check the palindrome.
Maybe I should have taken a big piece and splitted it. But I didn't have time for it.

1000000 letter in 4 segundos.
'''

import os
import sympy
import time
import threading
import concurrent.futures

def check_palinprime(number):
    # Check if palindrome.
    print(number)
    stretch = number
    # Check if number is palindrome and save if it.
    if stretch == stretch[::-1]:
        with open(f'Palindromos.txt', 'a') as reader:
            reader.write(f'O número {stretch} é um palíndromo.\n')
        num = int(stretch)
        # Check if number is prime and save if it.
        if sympy.isprime(num):
            # print(f'{num} é primo.')
            with open(f'Primos.txt', 'a') as reader:
                reader.write(f' O número {stretch} é primo.\n')


path = r"C:\Users\rossi\Desktop\y-cruncher v0.7.10.9513\ycds\0.txt"
palindromo = 21

print('Hello')
with open(path, 'r') as texto:
    stretch = ''
    t0 = time.perf_counter()
    count = 0
    while True:
        # To sanity
        count += 1
        if count % 10000000 == 0:
            try:
                tf = time.perf_counter() - t0
                print(f'{count} em {tf:.2f} segundos [{count/10000000000:.2%}]')
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
        # # Chamando função (1000000 letter in 4 segundos)
        ##############################################################
        check_palinprime(stretch)