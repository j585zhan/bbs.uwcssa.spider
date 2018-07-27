import urllib2
 
request = urllib2.Request("http://bbs.uwcssa.com/forum.php?mod=forumdisplay&fid=54&filter=author&orderby=dateline")
response = urllib2.urlopen(request)
print response.read()
