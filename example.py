import dnsfinder
import sys

if dnsfinder.CheckSite(sys.argv[1])!=1:
    print 'This site is secured'
else:
    print 'This site is not secured'