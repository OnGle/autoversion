#!/usr/bin/python
"""Map git commits to auto-versions and vice versa

Options:
  -r --reverse		map version to git commit

"""
import sys
import help
import getopt

from autoversion import *

@help.usage(__doc__)
def usage():
    print >> sys.stderr, "Syntax: %s <commit> [ ... ]" % sys.argv[0]
    print >> sys.stderr, "Syntax: %s -r <version> [ ... ]" % sys.argv[0]

def fatal(s):
    print >> sys.stderr, "error: " + str(s)
    sys.exit(1)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'rh', ['reverse'])
    except getopt.GetoptError, e:
        usage(e)

    opt_reverse = False
    for opt, val in opts:
        if opt == '-h':
            usage()
            
        if opt in ('-r', '--reverse'):
            opt_reverse = True

    if not args:
        usage()

    for arg in args:
        if opt_reverse:
            print version2commit(arg)
        else:
            print commit2version(arg)

if __name__=="__main__":
    main()
