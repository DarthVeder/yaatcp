#*_* coding: utf-8 *_*
"""
Usefull spherical geometry library. It contains the following functions:
convertDP2numeric(s_val) : convert " N34 22.992' " into a float numerical value
convertDPS2numeric(s_val) : convert " S 33° 35' 4.54" " into a float numerical value
distance(P1,P2) : distance between two points on the sphere given as Pi(lati,longi) 
"""

def convertDP2numeric(s_val):
    """ Converts a coordinate in the letteral format N34 22.992 (string)into
        a numeric one 34.3832. N,E,W,S must ALWAYS be at the beginning of the
        s_val string and degrees must be separated by a space from primes,
        but can be either lower or capital.

        Usage: val = convertCoord("N33 45.992").
        in: n33 44.55 OK
            N33 22.55 OK
            N 33 33.44 OK
            33 N 23.22 !! NO !!
    """
    s_val = s_val.strip()
    sign = {'N': 1.0, 'S': -1.0, 'E': 1.0, 'W': -1.0}
    # val[0] contains ALWAYS N, S, E or W. Lower or upper case are managed.
    letteral = s_val[0].upper()
    deg, prime = [ s_val[1:].split()[i] for i in range( len(s_val[1:].split()) )]
    val = float(deg) + float(prime[:-1])/60.0
    val = val * sign[letteral]

    return val


def convertDPS2numeric(s_val):
    """ Converts a coordinate in the letteral format N33° 35' 4.54" (string)into
        a numeric one 34.3832. N,E,W,S must ALWAYS be at the beginning of the
        s_val string and degrees must be separated by a space from primes,
        but can be either lower or capital.

        Usage: val (double) = convertCoord('''N33° 35' 4.54"''').
        in: n33 44.55' OK
            N33 22.55' OK
            N 33 33.44 OK
            33 N 23.22 !! NO !!
    """

    s_val = s_val.strip()
    sign = {'N': 1.0, 'S': -1.0, 'E': 1.0, 'W': -1.0}
    # val[0] contains ALWAYS N, S, E or W. Lower or upper case are managed.
    letteral = s_val[0].upper()
    deg , prime, second = [ float( s_val[1:].split()[i][:-1] ) for i in range( len(s_val[1:].split()) )]
    val = deg + prime/60.0 + second/3600.0
    val = val * sign[letteral]

    return val


if __name__ == '__main__':
    letter = ['N', 'S', 'E', 'W']
    s_val = '''33° 35' 4.54"'''.decode('utf-8')
    s_val2 = '''  33 35.54' '''
    for i in range(4):
        print(letter[i]+s_val)
        print( convertDPS2numeric(letter[i]+s_val) )

        
        print(letter[i]+s_val2)
        print( convertDP2numeric(letter[i]+s_val2) )
