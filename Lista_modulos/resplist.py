def first_last6(nums):
    if not 6 in nums:
        return False
    else:
        if nums[0] == 6 or nums[-1] == 6:
            return True
        else:
            return False

def same_first_last(nums):
  if nums != [] and nums[0] == nums[-1]:
    retorno = True
  else:
    retorno = False
  return retorno

def common_end(a, b):
  if a[0] == b[0] or a[-1] == b[-1]:
    retorno = True
  else:
    retorno = False
  return retorno

def maior_ponta(nums):
  c=1
  if nums[0] >= nums[-1]:
    pos1 = nums[0]
    del nums[:]
    while c <=3:
      nums.append(pos1)
      c=c+1
    return nums
  elif nums[0] < nums[-1]:
    pos1 = nums[-1]
    del nums[:]
    while c <=3:
      nums.append(pos1)
      c=c+1
    return nums

def sum2(nums):
  if len(nums) >=2 :
    result = nums[0] + nums[1]
    del nums[:]
    nums=result
    return nums
  elif len(nums) == 1 :
    return nums[0]
  elif len(nums) == 0 :
    return 0

def middle_way(a, b):
  pos1=a[1]
  pos2=b[1]
  del a[:]
  a.append(pos1)
  a.append(pos2)
  return a

def date_fashion(eu, par):
  if eu <=2 or par <=2:
    result= 0
    return result
  elif eu >= 8 or par >= 8:
    result = 2
    return result
  elif eu < 8 or par <8:
    result = 1
    return result

def squirrel_play(temp, is_summer):
    if temp >= 60 and temp <=90 and not is_summer:
        return True
    else:
        if temp >= 60 and temp <=100 and is_summer:
            return True
        else:
            return False

def pego_correndo(speed, is_birthday):
  if is_birthday :
    speed-=5
  if speed <= 60:
    return 0
  elif speed >=61 and speed <=80:
    return 1
  elif speed >= 81:
    return 2

def alarm_clock(day, vacation):
  if not vacation:
    if day == 6 or day == 0:
      return '10:00'
    else:
      return '7:00'
  else:
    if day == 6 or day == 0:
      return 'off'
    else:
      return '10:00'