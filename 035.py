import resources.pef as pef
import time
"""
https://projecteuler.net/problem=35
6.02173376083374
"""


def rotate(num, amount):
    lnum = [int(j) for j in str(num)]

    for i in range(amount):
        lnum.append(lnum.pop(0))

    num = int(''.join(map(str,lnum)))
    return num


def main():

    primes = pef.prime_sieve(1000000)

    count = 4
    for i in primes:
        primecount = 1
        for j in range(1, len(str(i))):

            num = rotate(i, j)

            if pef.is_prime(num):
                primecount += 1
                if primecount == len(str(i)):
                    count += 1

    return count


if __name__ == "__main__":
    start_time = time.time()
    answer = main()
    end_time = time.time()
    pef.answer(answer, end_time - start_time)
