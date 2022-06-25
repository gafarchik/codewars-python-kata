def duplicate_count(text):
    return len([letter for letter in set(text.lower()) if text.lower().count(letter) > 1])
     
