#!/usr/bin/ruby
#Brian Franco

require 'cgi'
require 'stringio'
require 'mysql2'

$stdout.sync = true
$stderr.reopen $stdout
puts "content-type:text/html\r\n\r\n"
cgi= CGI.new ("html5")

db = Mysql2::Client.new(:host => '10.20.3.4',:username => 'dbms_bf',:password => 'bf_england',:database => 'dbms_bf_dbA')

puts "<!doctype html>"
puts "<html>"
puts "<head> <title> Delete From Table </title> </head>"
puts "<body>"

puts"<h1> Thank you for your response </h1>"
if (cgi['restriction'] == " ")
  puts "You must specify a condition to delete on"
end

if (cgi['fieldName'] == "Computer")
  queryString = "Delete From Computer WHERE Name = '" + cgi['restriction'] + "';"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the name." 
end 

if (cgi['fieldName'] == "AddingMachines")
  queryString = "Delete From AddingMachines WHERE Name = '" + cgi['restriction'] + "';"                                                  
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end

if (cgi['fieldName'] == "CPU")
  queryString = "Delete From CPU WHERE CPU = '" + cgi['restriction'] + "';"                                                          
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the CPU."
end

if (cgi['fieldName'] == "Manufacturer")
  queryString = "Delete From Manufacturer WHERE Manufacturer = '" + cgi['restriction'] + "';"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the Manufacturer."
end

if (cgi['fieldName'] == "Location")
  queryString = "Delete From Location WHERE LocationNumber = " + cgi['restriction'] + ";"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the Location Number."
end

if (cgi['fieldName'] == "ComputerHardware")
  queryString = "Delete From ComputerHardware WHERE Name = '" + cgi['restriction'] + "';"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end

if (cgi['fieldName'] == "Miscellaneous")
  queryString = "Delete From Miscellaneous WHERE Name = '" + cgi['restriction'] + "';"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end

if (cgi['fieldName'] == "Modem")
  queryString = "Delete From Modem WHERE Name = '" + cgi['restriction'] + "';"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end

if (cgi['fieldName'] == "Monitor")
  queryString = "Delete From Monitor WHERE Name = '" + cgi['restriction'] + "';"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end

if (cgi['fieldName'] == "Printer")
  queryString = "Delete From Printer WHERE Name = '" + cgi['restriction'] + "';"                                                                                                                                                 
  puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end

if (cgi['fieldName'] == "ProductionTimes")
  queryString = "Delete From ProductionTimes WHERE itemName = '" + cgi['restriction'] + "';"                                                                                                               
   puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end

if (cgi['fieldName'] == "Software")
  queryString = "Delete From Software WHERE Name = '" + cgi['restriction'] + "';"
  rows = db.query(queryString)
  puts "We have deleted all data with " + cgi['restriction']  + " as the name."
end





