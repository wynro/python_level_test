import sys

def bien_formada(s, depth=0):
    try:
        # A little dirty, but meh
        try:
            first = s[0]
            last = s[1:]
        except IndexError:
            first = ''
            last = ''
        # Generalize to {}?
        if first == '(':
            return bien_formada(last, depth+1)
        elif first == ')':
            return bien_formada(last, depth-1)
        elif first.isdigit():
            if depth != int(first):
                return False
            return bien_formada(last, depth)
        elif last == '' and depth == 0:
            return True
        else:
            return False
    except:
        print "Error: ", sys.exc_info()[0]
