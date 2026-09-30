"""
Problem:  You need to capitalize the first letter of each word in a string, but only if that first character is a letter. 

Platform : HackerRank

Difficulty: Mid

"""

def solve(s: str) -> str:
    words = s.split(' ')
    capitalized = []
    for w in words:
        if w and w[0].isalpha():
            w = w[0].upper() + w[1:]
        capitalized.append(w)
    return ' '.join(capitalized)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
