from func_ex_01 import med_aluno

def test_ex03():
    print('media')
    assert med_aluno("marcos", {"vini": [8, 8], "oseas": [9, 8], "marcos":[10, 9]}) == 9.5
    assert med_aluno("augusto", {"vinireis": [2, 5], "augusto": [5, 7], "cesar": [0 , 1]}) == 6
    assert med_aluno("oseas", {"cesar": [3, 5], "marcos": [5, 5], "oseas": [6, 7], "augusto": [10, 9]})