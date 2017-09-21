from func_ex_01 import contagemvogal

def test_ex02():
  print ('contagemvogal')
  assert contagemvogal('aeiou') == 5
  assert contagemvogal('banana') == 3
  assert contagemvogal('impacta') == 3
  assert contagemvogal('o cesar é o cara') == 6
