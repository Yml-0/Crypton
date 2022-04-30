import os
import sys
import base64
import perem
import defs
defs.name()
print('What do you want to do?')
print('1 Encrypt')
print('2 Decrypt')
print('')
what_do = int(input())
if what_do == 1:
    defs.encrypt()
if what_do == 2:
    defs.decrypt()