#! /usr/bin/python3

PASSWORDS = {'email' : 'efbuyegfKWFGEY',
             'facebook' : 'bfahbshfbskefb',
             'github' : 'abfhbfkubcak'}

import sys, pyperclip

if len(sys.argv)<2:
    print('Usage: ./password.py [account] - copy account password')
    sys.exit()

account_name = sys.argv[1]


if account_name in PASSWORDS:
    pyperclip.copy(PASSWORDS[account_name])
    print('Password Copied')

else:
    print('No account named' + str(account_name) + 'exists!')
