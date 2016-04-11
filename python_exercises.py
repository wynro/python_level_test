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

def invertir(map):
    return_map = {}
    for k, v in map.iteritems():
        try:
            if return_map.has_key(v):
                # Concatenate
                return_map[v] += [k]
            else:
                # New
                return_map[v] = [k]
        except TypeError:
            # Conversion fail, ignore it silently
            1+1
        except:
            print "Unexpected error: ", sys.exc_info()[0]
            raise
    return return_map

def no_unico(list):
    already_found = []
    not_unique = []
    for i in list:
        if i not in already_found:
            already_found += [i]
        else:
            if i not in not_unique:
                not_unique += [i]
    return iter(not_unique)

class Cancion:
    lines = []

    def __init__(self, lines):
        self.lines = lines

    def play(self):
        for i in self.lines:
            print i
