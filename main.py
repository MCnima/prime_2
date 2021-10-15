import sys


def main():
    number = int(sys.argv[1])
    try_until = int((number//2) + 1)
    for Try_number in range(2, try_until + 1):
        if number % Try_number == 0:
            print('number is NOT prime by factor of %d' % Try_number)
            break
        else:
            if Try_number == try_until:
                print('%d is prime!!!!' % number)
            else:
                pass


if __name__ == '__main__':
    main()
