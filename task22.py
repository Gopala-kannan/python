prime = int(input("Enter a Number : "))

if prime > 1:
    for i in range(2, prime):
            if (prime % i) == 0:
                print(prime, "It Not Prime")
                break
            else:
                print(prime, "Prime")
                break
    else:
        (prime, "its Not Prime")