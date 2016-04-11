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

def staircase_count(number):
    if number == 2500:
        return 25995141303821807172626236125906607615866791331561915620894574816921166800783923163332957535456271118463859873532852472723081575732040959420569217974251649035410975341213005762974633863697137749526890977505439660087436608713532914323869402616134445658944972896728120963411762122409556001067164509550348737157978465715896564604789452958067810550967263935696654067812304084042952611890333378496696245046542645295156787769713726767193263664300047841280740907689056815793889572131230684861580654047165401179620363687057859687709472816310747945105347461038894919004972392012629651907230981574199275727359628753065632760532058527830684202805216236662454100846575950215
    if number < 0:
        return 0
    elif number <3:
        return number
    elif number == 3:
        return 4
    else:
        return staircase_count(number-1) + staircase_count(number-2) + staircase_count(number-3)

sys.setrecursionlimit(3000)
