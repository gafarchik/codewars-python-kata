def get_count(sentence):
    return len(list(filter(lambda x: x if x in ['a', 'e', 'i', 'o', 'u'] else '', sentence)))
