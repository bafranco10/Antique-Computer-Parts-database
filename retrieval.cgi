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
puts "<head> <title> Antique Technology Information Display </title> </head>"
puts "<body>"

puts"<h1> Thank you for your response here is your information </h1>"

#These conditonals check what was selected from Drop Down. They then show the information accordingly

if (cgi['TableName'] == "AddingMachines")
  queryString = "Select * From AddingMachines;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td>Name</td> <td> Manufacturer </td> <td>Length</td> <td>Width</td> <td>Height</td> <td>Weight</td> <td>LocationNumber</td> </tr> " 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row['Length'].to_s + "</td>"
    puts "<td>" + row['Width'].to_s + "</td>"
    puts "<td>" + row['Height'].to_s + "</td>"
    puts "<td>" + row['Weight'].to_s + "</td>"
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['TableName'] == "CPU")
   queryString = "Select * From CPU;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td> CPU Name</td> <td> Speed </td></tr> "
  rows.each do |row|
    puts "<tr><td>" + row['CPU'] + "</td>"
    puts "<td>" + row['Speed'] + "</td></tr>"
    puts "</table>" 
  end
end
if (cgi['TableName'] == "Computer")
  queryString = "Select * From Computer;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td>Name</td> <td> Manufacturer </td> <td>Length</td> <td>Width</td> <td>Height</td> <td>Weight</td> <td> Price </td> <td>LocationNumber</td> </tr> " 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row['Length'].to_s + "</td>"
    puts "<td>" + row['Width'].to_s + "</td>"
    puts "<td>" + row['Height'].to_s + "</td>"
    puts "<td>" + row['Weight'].to_s + "</td>"
    puts "<td>" + row['Price'].to_s + "</td>" 
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['TableName'] == "ComputerHardware")
  queryString = "Select * From ComputerHardware;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td>Name</td> <td> CPU </td> <td>RAM</td> <td>Graphics</td> <td>Power Supply</td> <td>Sound</td> <td>Colors </td> <td> Keyboard</td> </tr> " 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row['CPU'] + "</td>"
    puts "<td>" + row['RAM'] + "</td>"
    puts "<td>" + row['Graphics'] + "</td>"
    puts "<td>" + row['PowerSupply'] + "</td>"
    puts "<td>" + row['Sound'] + "</td>"
    puts "<td>" + row['Colors'] + "</td>" 
    puts "<td>" + row['Keyboard'] + "</td>"
    puts "</tr>"
  end
  puts "</table>"
end

if (cgi['TableName'] == "Location")
  queryString = "Select * From Location;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td>Location Number</td><td> Location Name </td> <td> Is it on Display? </td> </tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "<td>" + row['LocationName'] + "</td>"
    puts "<td>" + row['DISPLAYCASE_YESORNO'] + "</td>"
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['TableName'] == "Manufacturer")
  queryString = "Select * From Manufacturer;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td>Manufacturer</td><td>Origin </td></tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row['Origin'] + "</td>"
    puts "</tr>"
  end
  puts "</table>"
end

if (cgi['TableName'] == "Miscellaneous")
  queryString = "Select * From Miscellaneous;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td>Type</td> <td>Manufacturer</td><td>LocationNumber </td></tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row['Type'] + "</td>" 
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>"
end

if (cgi['TableName'] == "Modem")
  queryString = "Select * From Modem;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td>Manufacturer</td><td>Location Number </td></tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"  
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>"
end

if (cgi['TableName'] == "Monitor")
  queryString = "Select * From Monitor;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td>Manufacturer</td><td>Location Number </td></tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"  
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>"
end

if (cgi['TableName'] == "Printer")
  queryString = "Select * From Printer;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td>Manufacturer</td><td>Origin </td> <td> Speed </td> <td> Graphics </td> <td> LocationNumber </td></tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"  
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row['Origin'] + "</td>"
    puts "<td>" + row['Speed'] + "</td>"
    puts "<td>" + row['Graphics'] + "</td>"
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>"
end

if (cgi['TableName'] == "ProductionTimes")
  queryString = "Select * From ProductionTimes;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td>Start Production</td><td>Stop Production </td></tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Itemname'] + "</td>"  
    puts "<td>" + row['StartProduction'].to_s + "</td>"
    puts "<td>" + row['StopProduction'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>"
  
end

if (cgi['TableName'] == "Software")
  queryString = "Select * From Software;"
  rows =  db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td>Operating System</td><td>Built in Language </td></tr> "
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"  
    puts "<td>" + row['OperatingSystem'] + "</td>"
    puts "<td>" + row['BuiltInLanguage'].to_s + "</td>"
    puts "</tr>"
  end
  puts "</table>"
end

#These conditonals are all to see which table to call and what attributes the user wants

if (cgi['fieldName'] == "Computer")
  queryString = "Select Name, " + cgi['restriction'] + " From Computer;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
    puts "</table>"
  end
end

if (cgi['fieldName'] == "AddingMachines")
  queryString = "Select Name, " + cgi['restriction'] + " From AddingMachines;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>"
end 

if (cgi['fieldName'] == "CPU")
  queryString = "Select CPU, " + cgi['restriction'] + " From CPU;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['CPU'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>"
end

#Does not display properly 
if (cgi['fieldName'] == "Manufacturer")
  queryString = "Select Manufacturer, " + cgi['restriction'] + " From Manufacturer;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Manufacturer'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>"
end 

if (cgi['fieldName'] == "Location")
  queryString = "Select LocationNumber, " + cgi['restriction'] + " From Location;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Location Number </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['LocationNumber'].to_s + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['fieldName'] == "ComputerHardware")
  queryString = "Select Name, " + cgi['restriction'] + " From ComputerHardware;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['fieldName'] == "Miscellaneous")
  queryString = "Select Name, " + cgi['restriction'] + " From Miscellaneous;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['fieldName'] == "Modem")
  queryString = "Select Name, " + cgi['restriction'] + " From Modem;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['fieldName'] == "Monitor")
  queryString = "Select Name, " + cgi['restriction'] + " From Monitor;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['fieldName'] == "Printer")
  queryString = "Select Name, " + cgi['restriction'] + " From Printer;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['fieldName'] == "ProductionTimes")
  queryString = "Select Itemname, " + cgi['restriction'] + " From ProductionTimes;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Itemname'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end

if (cgi['fieldName'] == "Software")
  queryString = "Select Name, " + cgi['restriction'] + " From Software;"
  rows = db.query(queryString)
  puts "<table>"
  puts "<tr> <td> Name </td> <td> " + cgi['restriction'] + "</td></tr>" 
  rows.each do |row|
    puts "<tr>"
    puts "<td>" + row['Name'] + "</td>"
    puts "<td>" + row[cgi['restriction']].to_s + "</td>" 
    puts "</tr>"
  end
  puts "</table>" 
end
