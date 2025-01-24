def number_in_english(number: int) -> str:
    n = number
    l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
          'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', '']
    l2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
          'eighty', 'ninety']
     
    if not n:
        return 'zero'
    if n // 100 and n % 100:
        result = '{} hundred and '.format(l1[n // 100 - 1])
    elif n // 100:
        result = '{} hundred'.format(l1[n // 100 - 1])
    else:
        result = ''
    if n % 100 <= 19:
        result += l1[n % 100 - 1]
    else:
        result = result + l2[n % 100 // 10 - 2] + ' ' + l1[n % 10 - 1]
    return result
 