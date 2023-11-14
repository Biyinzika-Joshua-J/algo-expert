def nth_fib_bf(number):
    if number == 2:
        return 1
    elif number == 1:
        return 0
    else:
        return nth_fib_bf(number-1) + nth_fib_bf(number-2)
    
def memo_sol(number, hash={1:0, 2:1}):
    if number in hash:
        return hash[number]
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





def bottom_up_revised(n):
    last_fibs = [0, 1]
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(n-2):
        first, second = last_fibs
        next = first + second
        last_fibs[0] = last_fibs[1]
        last_fibs[1] = next
    return last_fibs[1]