#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


def find_subst_in_str(str1, set1):
    sub_str1 = ''
    found = False
    
    while set1:
        for c in str1:
            if c in set1:
                set1.remove(c)
                found = True
            if found == True:
                sub_str1 += c
            if len(set1) == 0: found = False
    return sub_str1

	

def test_find_subst_in_str(module_name='this module'):
    str1 = 'ydxahbcscdk'
    
    set1 = {'a','b','c','d'}
    result = 'dxahbc'
    
    assert( find_subst_in_str(str1, set1)==result)
    
    set2 = {'a','b','c'}
    result2 = 'ahbc'
    assert( find_subst_in_str(str1, set2)==result2)

        
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_find_subst_in_str()

