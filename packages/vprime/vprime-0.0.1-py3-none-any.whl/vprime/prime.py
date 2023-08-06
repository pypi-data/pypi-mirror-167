class Prime:
    def find_prime(num):
        if num > 1:
            condition = False
            for i in range(2,num):
                if num%i == 0:
                    return True
            if condition:
                return "Not prime"
            else:
                return "Prime"