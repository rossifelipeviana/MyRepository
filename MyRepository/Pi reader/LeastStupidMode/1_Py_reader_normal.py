'''
First attempt to extract palindrome prime of pi by '.txt' file. I'm don't know if its work.
The text (pi number) must be extracted using it: http://www.numberworld.org/y-cruncher/#Download
'''


import os
import sympy
import time
import threading
import concurrent.futures


def palinpri(chunck):
    '''Check if chunk is palindrome and prime.'''
    global count, t0, palindromo
    inicio = 0
    final = palindromo
    stretch = chunck[inicio:final]
    ##############################################################
    # Work with stretch
    ##############################################################
    while len(stretch) >= palindromo:
        # To sanity
        if count % 100000000 == 0:
            with open('checkpoint.txt', 'w') as checkpoint:
                checkpoint.write(f'Feito até {count}.\n')
            try:
                tf = time.perf_counter() - t0
                print(f'{count} em {tf/60:.2f} minutos [{count/10000000000:.2%}]')
                t0 = time.perf_counter()
            except:
                pass
        stretch = chunck[inicio:final]
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
        inicio += 1
        final += 1
        count += 1


path = r"C:\Users\rossi\Desktop\y-cruncher v0.7.10.9513\ycds\0.txt"  # Nada encontrado
path = r"C:\Users\rossi\Desktop\y-cruncher v0.7.10.9513\ycds\1.txt"
palindromo = 21

print('Hello')

# thread = threading.Thread(target=worker, args=(path, palindromo))
# thread.append(thread)
# thread.start()

with open(path, 'r') as texto:
    t0 = time.perf_counter()
    count = 0
    ##############################################################
    # Extract a chunk of pi
    # 3,1415115187165161652116518165713515746157164117132157
    # Patch é um número.
    # Chunk é o trecho do texto.
    ##############################################################
    chunk = ''
    tail = ''
    patch = palindromo * 100000000  # Extrair um número (patch) grande e múltiplo do palíndromo
    try:
        while True:
            chunk += texto.read(patch) # Leitura de um pacote do texto (pi)
            # Verifica se eu consegui extrair o pacote de número e se ele não está muito pequeno #FIXME:
            if patch == 0:
                patch = palindromo
            elif patch < 10:
                patch = patch - 1
            elif len(chunk) < patch:
                patch = patch // 10

            chunk = tail + chunk
            palinpri(chunk)
            tail = chunk[0:-palindromo]
    except Exception as e:
        with open('error.txt') as error:
            error.write(e)

print(f'Os últimos números são {chunk}')
