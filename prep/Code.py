from typing import List

def special_pairs(n: int) -> [[int]]:
    res = []
    def is_prime(a , b): 
        if a <= 0 and b <= 0:
            return False
        for x,y in zip(range(2, int(a**0.5)+1), range(2, int(b**0.5)+1)):
            if a % x == 0 and b % y == 0:
                return False
            return True
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            if (i + j) == n and is_prime(i , j):
                res.append([i,j])
    return res

# R E A D M E
# DO NOT CHANGE the code below, we use it to grade your submission. If changed your submission will be failed automatically.
if __name__ == '__main__':
    n = int(input())
    output = special_pairs(n)
    if output == []:
        print('[]')
    else:
        output_str_list = ['[%s]' % ','.join(map(str, combination)) for combination in output]
        output_str = '[%s]' % ','.join(output_str_list)
        print(output_str)