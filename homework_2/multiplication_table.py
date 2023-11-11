import random


def create_multiplication_table(num: int) -> list[str]:
    out = [f'{i} * {num} = {i * num}' for i in range(1, num + 1)]
    return out


if __name__ == '__main__':
    n = random.randint(2, 50)
    print(n)
    print(*create_multiplication_table(n), sep='\n')
