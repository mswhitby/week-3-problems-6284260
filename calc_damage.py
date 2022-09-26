def user_input():
  input(
    """
    1.input damage value
    2.damage cannot be negative
    3.damage must be a number
    
    """
    
    "Please input damage: " 
    
  )
  
  return 
  

def user_inpt():
  input(
    """
    1.input speed value
    2.speed cannot be negative
    3.speed must be a number
    
    """
    
    "Please input speed: " 
    
  )
  
  return 
  
def user_ipt():
  input(
    """
    1.input time value
    2.time cannot be negative
    3.time must be a number
    
    """
    
    "Please input time: " 
    
  )
  
  return 
  
def damage_total():
  DPS=damage*speed*time
  for character in DPS:
   if DPS < 0:
    print("invalid")
    break

  return
  print(str(DPS))
  
  
  
  
damage = user_input()
time =  user_ipt()
speed = user_inpt()
