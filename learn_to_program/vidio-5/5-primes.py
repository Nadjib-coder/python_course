def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


print(is_prime(6))


def get_primes(max_number):
    prime_list = []
    for num1 in range(2, max_number):
        if is_prime(num1):
            prime_list.append(num1)
    return prime_list


max_num = int(input("Search for primes up to :"))

list_of_primes = get_primes(max_num)

for prime in list_of_primes:
    print(prime)
