#!/usr/bin/ruby

require 'cgi'
require 'stringio'

$stdout.sync = true
$stderr.reopen $stdout

print "Content-type: text/html\r\n\r\n"
cgi = CGI.new ("html5")

if cgi['WhatDo'] == 'SingleInsert'
  print "<HTML>\n"
  print "<HEAD>"
  print "<meta http-equiv='refresh' content='2; url=http://www.cs.transy.edu/ryan/DBProject/singleInsert.html'>"
  print "<TITLE> Redirecting </TITLE></HEAD>"
  print "<body>\n"
  print "<H1> REDIRECTING </H1>\n"
  print "</BODY>\n"
  print "</HTML>\n"
end
if cgi['WhatDo'] == 'MassInsert'
  print "<HTML>\n"
  print "<HEAD>"
  print "<meta http-equiv='refresh' content='2; url=http://www.cs.transy.edu/bfranco/DBProject/DBProject.html'>"
  print "<TITLE> Redirecting </TITLE></HEAD>"
  print "<body>\n"
  print "<H1> REDIRECTING </H1>\n"
  print "</BODY>\n"
  print "</HTML>\n"
end
if cgi['WhatDo'] == 'Delete'
  print "<HTML>\n"
  print "<HEAD>"
  print "<meta http-equiv='refresh' content='2; url=http://www.cs.transy.edu/bfranco/DBProject/delete.html'>"
  print "<TITLE> Redirecting </TITLE></HEAD>"

  print "<body>\n"
  print "<H1> REDIRECTING </H1>\n"
  print "</BODY>\n"
  print "</HTML>\n"

end
if cgi['WhatDo'] == 'MassInsert'
  print "<HTML>\n"
  print "<HEAD>"
  print "<meta http-equiv='refresh' content='2; url=http://www.cs.transy.edu/bfranco/DBProject/DBProject.html'>"
  print "<TITLE> Redirecting </TITLE></HEAD>"

  print "<body>\n"
  print "<H1> REDIRECTING </H1>\n"
  print "</BODY>\n"
  print "</HTML>\n"
end
if cgi['WhatDo'] == 'Retrieval'
  print "<HTML>\n"
  print "<HEAD>"
  print "<meta http-equiv='refresh' content='2; url=http://www.cs.transy.edu/bfranco/DBProject/retrieval.html'>"
  print "<TITLE> Redirecting </TITLE></HEAD>"

  print "<body>\n"
  print "<H1> REDIRECTING </H1>\n"
  print "</BODY>\n"
  print "</HTML>\n"
end
