from PIL import Image  
import numpy as np

input_image = "twitter.png"
output_file = "res.txt"
output_shape = (30, 30)
sorted_digits = [0, 8, 9, 6, 5, 1, 2, 4, 3, 7] # sorted from most to least dense

def image_to_digits(input_image, sorted_digits, new_size):
    image = Image.open(input_image)

    # preprocessing
    image = image.resize(new_size)
    image = image.convert('L') # Convert to grayscale
    image_array = np.array(image) / 255 # Convert to numpy array and normalize

    # Divide the intensity range into bins corresponding to each digit
    num_bins = len(sorted_digits)
    bins = np.linspace(0, 1, num_bins + 1)[1:-1]

    # Replace each pixel with the corresponding digit from the sorted_digits list
    digit_image = np.digitize(image_array, bins)
    digit_image = np.vectorize(lambda x: sorted_digits[x])(digit_image)

    print('ascii num:')
    print(digit_image)

    # flatten to number
    if digit_image[0][0] == 0:
        digit_image[0][0] = 1 # ensure that the leading digit is not 0

    return int("".join(map(str, digit_image.flatten())))

import random

def miller_rabin(n, k=5):
    # Small prime numbers check
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n < 2 or any(n % p == 0 for p in small_primes):
        return False

    # Find d and r such that n - 1 = 2^r * d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k rounds of Miller-Rabin tests
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def next_prime(n):
    if n % 2 == 0:
        n += 1
    while not miller_rabin(n):
        n += 2
    return n 

def construct_grid(n, shape):
    digits = [int(d) for d in str(n)]
    grid = np.array(digits).reshape(shape)
    return grid


number = image_to_digits(input_image, sorted_digits, output_shape)
prime = next_prime(number)

grid = construct_grid(prime, output_shape)
print('ascii prime:')
print(grid)
np.savetxt(output_file, grid, fmt="%d", delimiter="")
