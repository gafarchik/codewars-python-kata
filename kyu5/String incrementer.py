def increment_string(strng):
    alpha = strng.rstrip('0123456789')
    nums = strng[len(alpha):]
    if nums == "": 
        return strng+"1"
    else:
        return alpha + str(int(nums) + 1).zfill(len(nums))
