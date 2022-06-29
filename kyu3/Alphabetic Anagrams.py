from collections import Counter
def listPosition(word):
    word_len, d, l = len(word), 1, 1
    count = Counter()
    for i in range(word_len):
        wrd = word[(word_len - 1) - i]
        count[wrd] += 1
        for s in count:
            if (s < wrd):
                d += l * count[s] // count[wrd]
        l = l * (i + 1) // count[wrd]
    return d
