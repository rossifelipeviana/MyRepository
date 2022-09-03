################################################################
# 1 - Recursion to iterate.
# 2 - In if structure ever use "else" to return something, its help other to fix some bug.
################################################################
def testar_divisao(value: int, list: list) -> (float):
    "Take a value and test your division by a value in list."

    if isinstance(list[0], (float, int)) and list[0] > 0:
        print(value / list[0])
    elif isinstance(list[0], str):
        print(f'"{list[0]}" é uma string e não pode ser um denominador.')
    elif callable(list[0]):
        print(f"Até uma função tu tá passando, meu brother???")
    elif list[0] == 0:
        print("Não dá para dividir por 0, amigo...")
    else:
        try:
            value / list[0]
        except Exception as e:
            print(e)

    if len(list) == 1:
        return

    return testar_divisao(value, list[1:])


if __name__ == "__main__":
    print("\n")
    a = 10
    b = [1, 2]
    c = "a"
    d = lambda x: x * 2
    e = 0

    list = (a, b, c, d, e)

    testar_divisao(100, list)
    print("\n")
