import os
import sympy
import time
import threading
import concurrent.futures


def palinpri(chunck):
    global count, t0
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
    inicio = 0
    final = palindromo
    count += 1
    ##############################################################
    # Work with stretch
    ##############################################################
    while len(stretch) <= palindromo:
        stretch = chunck[inicio:final]
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
    # Extract a chunck of pi
    ##############################################################
    chunck = ''
    tail = ''
    patch = palindromo * 2100000000  # 2,1 bi
    while patch == 0:
        chunck += texto.read(patch)
        # Verifica se eu consegui extrair o pacote e se ele não está muito pequeno
        if len(chunck) < patch and len(chunck) / 10 > 10:
            patch = patch // 10
        # Extrair até o tamanho do chunck se tornar igual a 0
        elif len(chunck) > 0:
            patch = patch - 1
        # Se eu não consegui extrair nada do texto
        elif len(chunck) == 0:
            print('Todo arquivo foi lido')
            break
        chunck = tail + chunck
        palinpri(chunck)
        tail = chunck[0:-palindromo]
print(f'Os últimos números são {chunck}')
