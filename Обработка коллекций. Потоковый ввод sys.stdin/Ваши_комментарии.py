import sys
 
print(len(list(filter(lambda x: x.lstrip().startswith('#'), [text for text in sys.stdin]))))