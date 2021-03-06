#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def find_long_con_inc(seq):
    ''' find the longest continuous increasing subsequence'''
    one_seq = []
    result = []
    
    for i in range(0, len(seq)-1):
        pivot = seq[i]      
        if pivot <= seq[i+1]:
            one_seq.append(pivot)
        else:
            one_seq.append(pivot)
            if len(one_seq) > len(result):
                result = one_seq
            one_seq = []
    return result


def test_find_long_con_inc(module_name='this module'):
    seq = [1, -2, 3, 5, 1, -1, 4, -1, 6]
    long_con_inc = [-2,3,5]

    assert(find_long_con_inc(seq) == long_con_inc )

if __name__ == '__main__':
    test_find_long_con_inc()

