def nth_fib_bf(number):
    if number == 2:
        return 1
    elif number == 1:
        return 0
    else:
        return nth_fib_bf(number-1) + nth_fib_bf(number-2)
    
def memo_sol(number, hash={}):
    if number in hash:
        return hash[number]
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        hash[number] = memo_sol(number-1, hash) + memo_sol(number-2, hash)
        return hash[number]

def bottom_up(number):
    last_two_fibs = [0, 1]

    if number == 1:
        return 0
    if number == 2:
        return 1

    for i in range(number-2):
        first_fib, second_fib = last_two_fibs
        next_fib = first_fib + second_fib
        last_two_fibs[0] = second_fib
        last_two_fibs[1] = next_fib

    return last_two_fibs[1]


print(bottom_up(100))
print(nth_fib_bf(100))