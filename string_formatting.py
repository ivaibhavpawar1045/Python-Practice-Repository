

"""
Problem:  You need to print each number from 1 to n in decimal, octal, hexadecimal (uppercase), and binary, 
          all aligned to the width of the binary representation of n.

Sample Input : 2

Platform: HackerRank

Difficulty: hard 

"""

def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(decimal, octal, hexa, binary)
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)