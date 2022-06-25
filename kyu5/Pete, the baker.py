def cakes(recipe, available):
    count = 0
    in_recp = list(recipe)
    in_avelb = list(available)
    in_recp_val = list(recipe.values())
    in_avelb_val = list(available.values())
    can_bake = []
    if len(available)>=len(recipe):
        for x in range(0,len(recipe)):
            try:
                ind = in_avelb.index(in_recp[x])
            except:
                return False
            if in_recp_val[x] <= in_avelb_val[ind]:
                can_bake.append(in_avelb_val[ind]//in_recp_val[x])
            else:
                return False
        return min(can_bake)
    else:
        return False
