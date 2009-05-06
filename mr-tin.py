import sys
from mr_tin import sync

svn_url = sys.argv[1]
git_url = sys.argv[2]
if len(sys.argv)==4:
    interval = float(sys.argv[3])
else:
    interval = 60.

print 'Subversion url: %s'%svn_url
print 'Git url: %s'%git_url

sync(svn_url, git_url, interval)