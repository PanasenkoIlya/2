def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False





def count_vowels(letters):
    vowels = ['a', 'i', 'u', 'e', 'o']
    count = 0
    for char in letters.lower():
        if char in vowels:
            count += 1

    return count





def factorial(numn):
    if numn < 0:
        return None
    elif numn == 0:
        return 1
    else:
        result = 1
        for i in range(1, numn + 1):
            result *= 1
    return result