


def get_average_prime_numbers():
    prime_numbers = []
    prime_to = int(input("Enter a number to print prime numbers upto: "))
    
    for i in range(2, prime_to +1):
        if i % 2 == 0:
            if i == 2:
                prime_numbers.append(i)
        elif i % 3 == 0:
            if i == 3:
                prime_numbers.append(i)
        elif i== 5:
            prime_numbers.append(i)
        elif i % 5 != 0:
            prime_numbers.append(i)
    print(prime_numbers)

    number = 0
    for i in prime_numbers:
       number += i
    averager_of_prime_number = number/ len(prime_numbers) 
    print(averager_of_prime_number)

get_average_prime_numbers()