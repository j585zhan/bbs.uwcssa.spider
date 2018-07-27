import urllib2
import sys
 
pages=5
sys.stderr.write("\r[%s%s]" % ('#' * 0, '.' * (pages - 0)))
sys.stderr.flush()
for i in range(1, pages+1):
    request = urllib2.Request("http://bbs.uwcssa.com/forum.php?mod=forumdisplay&fid=60&filter=author&orderby=dateline&page=" + str(i))
    response = urllib2.urlopen(request)
    print response.read()
    sys.stderr.write("\r[%s%s]" % ('#' * i, '.' * (pages - i)))
    sys.stderr.flush()

sys.stderr.write("\n")
