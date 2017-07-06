txt = raw_input(' Enter any string: ')
l = len(txt)
for i in range( 0,l/2 ):
    if txt[i] == txt[l-i-1]:
        print 'Given string a palindrome '
    else:
        print'not a pallindrome'

                

