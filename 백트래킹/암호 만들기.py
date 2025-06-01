gather = ['a','e','i','o','u']
L, C = map(int,input().split())
letters = input().split()
letters.sort()
s = []
visited = [False] * C
def backtracking(start):
    if len(s) == L:
        gather_count = 0
        for g in gather:
            if g in s:
                gather_count += 1
        vowel_count = L - gather_count
        if gather_count >= 1 and vowel_count >= 2:
            print(''.join(s))
        return
    for i in range(start, C):
        if visited[i]:
            continue
        visited[i] = True
        
        s.append(letters[i])
        backtracking(i)
        s.pop()
        visited[i] = False
backtracking(0)
