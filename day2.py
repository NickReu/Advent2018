data = open("input2").read().split()

def star1(data):
    twos = 0
    threes = 0
    for ID in data:
        seen = {}
        for letter in ID:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
        if 2 in seen.values():
            twos += 1
        if 3 in seen.values():
            threes += 1
    return twos * threes

def check(word1, word2):
    assert len(word1) == len(word2)
    score = 0
    pos = None
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            score += 1
            if score > 1:
                return False
            else:
                pos = i
    if score == 1:
        return pos

def star2(data):
    best_score = 0
    for ID1 in data:
        for ID2 in data:
            diff = check(ID1, ID2)
            if diff:
                return(ID1[:diff] + ID1[diff + 1:])

print(star2(data))
