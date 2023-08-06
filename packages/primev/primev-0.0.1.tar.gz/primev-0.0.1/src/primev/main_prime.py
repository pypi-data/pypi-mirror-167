class Prime:
    def find_prime(self,num):
        if num > 1:
            condition = False
            for i in range(2,num):
                if num % i == 0:
                    condition = True
            if condition:
                return "Not Prime"
            else:
                return "Prime"