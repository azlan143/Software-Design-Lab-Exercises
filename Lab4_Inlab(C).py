#Python recursive func that takes a char string s
#and output its reverse

def reverse(s):
    if s != '':
        reverse(s[1:])
        print(s[0], end = '')

reverse('pots&pans')

