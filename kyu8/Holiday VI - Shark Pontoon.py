def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    return "Alive!" if (pontoonDistance / youSpeed) < sharkDistance / (sharkSpeed - (sharkSpeed * 0.5 * dolphin)) else "Shark Bait!"
      
