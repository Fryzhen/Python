

def main():
    print(po2_v2(9))
    print(po2_v2(3))
    print(po2_v2(4))
    print(po2_v2(-1))
    print(po2_v2(5))


def po2_v1(number):
    i = 0
    while 2**i <= number:
        if 2**i == number:
            return True
        else:
            i += 1
    return False


def po2_v2(number):
    while number > 1:
        number /= 2
    return True if number == 1 else False



if __name__ == "__main__":
    main()