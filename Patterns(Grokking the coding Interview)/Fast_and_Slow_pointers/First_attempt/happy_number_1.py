def find_happy_number(num):
    # TODO: Write your code here
    slow, fast = num, num
    while True:
        slow = find_squares(slow)
        fast = find_squares(find_squares(fast))
        if fast == slow:
            return slow == 1
    return False

def find_squares(num):
    _sum = 0
    while (num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
