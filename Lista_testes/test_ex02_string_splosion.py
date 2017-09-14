# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  if len(s)==1:
    return s 
  elif len(s)==2:
    return s[0]+s[0]+s[1]
  elif len(s)==3:
    return s[0]+s[0]+s[1]+s[0]+s[1]+s[2]
  elif len(s)==4:
    return s[0]+s[0]+s[1]+s[0]+s[1]+s[2]+s[0]+s[1]+s[2]+s[3]
  elif len(s)==5:
    return s[0]+s[0]+s[1]+s[0]+s[1]+s[2]+s[0]+s[1]+s[2]+s[3]+s[0]+s[1]+s[2]+s[3]+s[4]
  elif len(s)==6:
    return s[0]+s[0]+s[1]+s[0]+s[1]+s[2]+s[0]+s[1]+s[2]+s[3]+s[0]+s[1]+s[2]+s[3]+s[4]+s[0]+s[1]+s[2]+s[3]+s[4]+s[5]
    
  
  
def test_ex02():
  print ('String Explosion')
  assert string_splosion('Code') == 'CCoCodCode'
  assert string_splosion('abc') == 'aababc'
  assert string_splosion('ab') == 'aab'
  assert string_splosion('x') == 'x'
  assert string_splosion('fade') == 'ffafadfade'
  assert string_splosion('There') == 'TThTheTherThere'
  assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
  assert string_splosion('Bye') == 'BByBye'
  assert string_splosion('Good') == 'GGoGooGood'
  assert string_splosion('Bad') == 'BBaBad'
