
"""
Problem:  Use split and join function and seperate the words by '-'

Sample Input : this is a string  

Platform: Hacker Rank

Difficulty: Easy 

"""

def split_and_join(line):
    word = line.split("-")
    return "-".join(word)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)