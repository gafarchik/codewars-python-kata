def turn(current, target):
    sides = ['N',"E","S","W"]
    side = ""
    cur = sides.index(current)
    tar = sides.index(target)
    if cur == 3 and tar == 0:
        side = 'right'
    elif cur == 0 and tar == 3:
        side = 'left'
    elif cur > tar:
        side = "left"
    elif cur < tar:
        side = "right"
    return side
