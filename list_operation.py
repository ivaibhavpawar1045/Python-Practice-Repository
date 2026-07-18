"""
Problem: Consider a list (list = []). You can perform the following commands:
           insert i e: Insert integer  at position .
          print: Print the list.
          remove e: Delete the first occurrence of integer .
          append e: Insert integer  at the end of the list.
          sort: Sort the list.
          pop: Pop the last element from the list.
          reverse: Reverse the list.

Sample Input : 12
               insert 0 5
               insert 1 10
               insert 0 6
               print
               remove 6
               append 9
               append 1
               sort
               print
               pop
               reverse
               print      

Platform: HackerRank
Difficulty: Medium
"""

if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        parts  = input().split()
        cmd = parts[0]

        if cmd == 'insert':
            i = int(parts[1])
            e = int(parts[2])
            lst.insert(i,e)

        elif cmd == 'print':
            print(lst)

        elif cmd == 'remove':
            e = int(parts[1])
            lst.remove(e)

        elif cmd == 'append':
            e = int(parts[1])
            lst.append(e)

        elif cmd == 'sort':
            lst.sort()

        elif cmd == 'pop':
            lst.pop()

        elif cmd == 'reverse':
            lst.reverse()