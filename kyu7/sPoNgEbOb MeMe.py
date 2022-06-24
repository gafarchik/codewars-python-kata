def sponge_meme( s ):
    return ''.join([c.upper() if i % 2 == 0
                    else c.lower()
                    for i,c in enumerate(s)])
