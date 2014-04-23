#!/usr/bin/python
import sys
import getopt
def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\0" not in s, "Input string cannot contain null character ('\\0')"
    s += "\0"  # Add end of file marker
    table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string

def ibwt(r):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith(" ")][0]  # Find the correct row (ending in "\0")
    return s.rstrip(" ")  # Get rid of trailing null character

def main(argv):
    # parse command line options
    try:
        opts, args = getopt.getopt(argv, "hed", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
	if o in ("-d", "--decode"):
	    string = raw_input()
	    print(ibwt(string))
	    sys.exit(0)
	elif o in ("-e", "--encode"):
	    string = raw_input()
	    print(bwt(string))
	    sys.exit(0)
    print 'Decodifica Codifica utilitzant l\'algoritme Burrows-Wheeler'
    print 'test.py -d --decode decodifica '
    print 'test.py -e --encode codific codifica'
    # process arguments
    sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
