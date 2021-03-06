#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import sys
import stack

def reverse_string_with_stack(str1):
  ''' Uses a stack to reverse a string '''
  s = stack.Stack()
  revStr = ''
  for c in str1:
    s.push(c)
  while not s.isEmpty():
    revStr += s.pop()
  return revStr
  

def test_reverse_string_with_stack():
    str1 = 'Buffy is a Slayer!'
    assert(reverse_string_with_stack(str1) == '!reyalS a si yffuB')
    print('Tests passed!')


if __name__ == '__main__':
    test_reverse_string_with_stack()   




