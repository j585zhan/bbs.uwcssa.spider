import urllib2
import sys
 
pages=5
sys.stderr.write("\r[%s%s]" % ('#' * 0, '.' * (pages - 0)))
sys.stderr.flush()

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

for i in range(1, pages+1):
    request = urllib2.Request("http://bbs.uwcssa.com/forum.php?mod=forumdisplay&fid=60&filter=author&orderby=dateline&page=" + str(i), headers=hdr)
    response = urllib2.urlopen(request)
    print response.read()
    sys.stderr.write("\r[%s%s]" % ('#' * i, '.' * (pages - i)))
    sys.stderr.flush()

sys.stderr.write("\n")
