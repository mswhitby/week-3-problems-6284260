def user_inpu():
  damage=input(
    """
    1.input damage value
    2.damage cannot be negative
    3.damage must be a number
    4.damage cannot be in word form
    
    """
    
    "Please input damage: " 
  )
  
  return damage
  int(damage)
  
def user_inpt():
  speed=input(
    """
    1.input speed value
    2.speed cannot be negative
    3.speed must be a number
    4.speed cannot be in word form
    
    """
    
    "Please input speed: " 
  )
  
  return speed
  int(speed)
  
def user_ipt():
  time=input(
    """
    1.input time value
    2.time cannot be negative
    3.time must be a number
    4.time interval is in seconds
    
    """
    
    "Please input time: " 
  )
  
  return time
  int(time)
  
def damage_total(damage,speed,time):
  damage, speed, time = int(damage), int(speed), int(time)
  # print(damage, type(damage))
  # print(speed, type(speed))
  # print(time, type(time))
  dps = damage * speed * time
  dps=str(dps)
  # print(dps, type(dps))
  if  "-" in dps:
    print("invalid")
  print(dps)
  
  return dps
  
  
  
  
damage = user_inpu()
speed = user_inpt()
time =  user_ipt()
rule_1 = damage_total(damage,speed,time)
