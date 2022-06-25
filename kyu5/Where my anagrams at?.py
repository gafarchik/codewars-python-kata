def anagrams(word, words):
    wrd = sorted(word) 
    ans = []
    for x in range(0,len(words)):
        if sorted(words[x]) == wrd:
            ans.append(words[x])
    return ans
