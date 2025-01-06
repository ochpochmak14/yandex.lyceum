word = input()
dct = dict()
dct['a'] = ".-"
dct['b'] = '-...'
dct['c'] = '-.-.'
dct['d'] = '-..'
dct['e'] = '.'
dct['f'] = '..-.'
dct['g'] = '--.'
dct['h'] = '....'
dct['i'] = '..'
dct['j'] = '.---'
dct['k'] = '-.-'
dct['l'] = '.-..'
dct['m'] = '--'
dct['n'] = '-.'
dct['o'] = '---'
dct['p'] = '.--.'
dct['q'] = '--.-'
dct['r'] = '.-.'
dct['s'] = '...'
dct['t'] = '-'
dct['u'] = '..-'
dct['v'] = '...-'
dct['w'] = '.--'
dct['x'] = '-..-'
dct['y'] = '-.--'
dct['z'] = '--..'
word = [x.lower() for x in word.split()]
for char in word:
    ans = ""
    for i in char:
        ans += dct[i] + ' '
    ans = ans.strip()
    print(ans)