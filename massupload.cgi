#!/usr/bin/ruby

require 'cgi'
require 'stringio'
require 'mysql2'

$stdout.sync = true
$stderr.reopen $stdout

# function takes in the lines from the CSV file and is only called if the user selects to add into this table
# function will exit with a success message if it is successful
#iterate thru lines and add lines to table

  def AddingMachines(str,size, db)
    sentinelValue = 0
    counter = 1
    while  sentinelValue < size do
      newData = str[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end

      sentinelValue = sentinelValue + 1 
    
    queryString = "INSERT INTO AddingMachines (Name,Manufacturer,Length,Width,Height,LocationNumber) VALUES('" + seps[0] + "','" + seps[1] + "','" + seps[2] + "','" + seps[3] + "','" + seps[4]+ "'," + seps[5] + ");"
    #puts queryString + "<br>"
    db.query(queryString)
    puts " Got through line " + counter.to_s + "<br>"
    counter = counter + 1
    end
     puts "Your file has been successfully uploaded to AddingMachines"
  end

  # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def CPU (str, size, db)
    sentinelValue = 0
    counter = 1
    while  sentinelValue < size do
      newData = str[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO CPU (CPU,Speed) VALUES('" + seps[0] + "','" + seps[1] + "');"
      #puts queryString + "<br>"
      db.query(queryString)
      puts " Got through line " + counter.to_s + "<br>"
      counter = counter + 1
    end
    puts "Your file has been successfully uploaded to CPU"
  end

  # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def Computers (str, size, db)
    sentinelValue = 0
    counter = 1
    while  sentinelValue < size do
      newData = str[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Computer (Name,Manufacturer,Length,Width,Height,Weight,Price,LocationNumber) VALUES('" + seps[0] + "','" + seps[1] + "'," + seps[2] + "," + seps[3] + "," + seps[4] + "," + seps[5] + "," + seps[6] + "," + seps[7] + ");"
      puts " Got through line " + counter.to_s + "<br>"
      #puts queryString + "<br>"
      db.query(queryString)
      counter = counter + 1
    end
    puts "Your file has been successfully uploaded to Computer" 
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def ComputerHardware (allTheLines, size, db)
    sentinelValue = 0
    counter = 1
    while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      seps.each_with_index do |sep,index|
        seps[index] = seps[index].strip
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO ComputerHardware (Name,CPU,RAM,Graphics,PowerSupply,Sound,Colors,Keyboard) VALUES('" + seps[0] + "','" + seps[1] + "','" + seps[2] + "','" + seps[3] + "','" + seps[4] + "','" + seps[5] + "','" + seps[6] + "','" + seps[7] + "');"
      #puts queryString + "<br>"
      db.query(queryString)
      puts "Got through line" + counter.to_s + "<br>"
      counter = counter + 1
    end
    puts "Your file has been successfully uploaded to Computer Hardware"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def Location(allTheLines, size, db) 
     sentinelValue = 0
    while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Location(LocationNumber,LocationName,DISPLAYCASE_YESORNO,AmountOwned) VALUES(" + seps[0] + "," + seps[1] + "','" + seps[2] + "'," + seps[3] + ");"
      #puts queryString + "<br>"
      db.query(queryString)
      puts " Got through line " + counter.to_s + "<br>"
      counter = counter + 1
    end
    puts "Your File has been successfully uploaded to Location"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  #Have issues with this one
  
  def Manufacturer(allTheLines, size, db)
    sentinelValue = 0
    counter = 1
    while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Manufacturer(Manufacturer,Origin) VALUES('" + seps[0] + "','" + seps[1] +  "');"
      #puts queryString + "<br>"
      db.query(queryString)
      puts " Got through line " + counter.to_s + "<br>"
      counter = counter + 1
    end
    puts "Your file has been successfully uploaded to Manufacturer"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def Miscellaneous(allTheLines, size, db)
    sentinelValue = 0
    counter = 1
    while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Miscellaneous(Name,Type,Manufacturer,LocationNumber) VALUES('" + seps[0] + "','" + seps[1] +  "','" + seps[2] + "'," + seps[3] + ");"
      puts queryString + "<br>"
      #db.query(queryString)
      puts " Got through line " + counter.to_s + "<br>"
      counter = counter + 1
    end
    puts "Your File was successfully uploaded to Miscellaneous"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def Modem(allTheLines, size, db)
    sentinelValue = 0
    counter = 1
      while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Modem(Name,Manufacturer,LocationNumber) VALUES('" + seps[0] + "','" + seps[1] + "'," + seps[2] + ");"
      #puts queryString + "<br>"
      db.query(queryString)
      puts " Got through line " + counter.to_s + "<br>"
      counter = counter + 1
      end
      puts " You have successfully uploaded to Modem"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def Monitor(allTheLines, size, db)
      sentinelValue = 0
      while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Monitor(Name,Manufacturer,LocationNumber) VALUES('" + seps[0] + "','" + seps[1] + "'," + seps[2] + ");"
      #puts queryString + "<br>"
      db.query(queryString)
      end
      puts " You have successfully uploaded to Monitor"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def Printer (allTheLines, size, db)
    sentinelValue = 0
      while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Printer(Name,Manufacturer,Origin,Speed,Graphics,LocationNumber) VALUES('" + seps[0] + "','" + seps[1] + "','" + seps[2] + "','" + seps[3] + "','" + seps[4] + "'," + seps[5] +");"
      #puts queryString + "<br>"
      db.query(queryString)
      end
      puts " You have successfully uploaded to Printer"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def ProductionTimes(allTheLines,size,db)
    sentinelValue = 0
    counter = 1
      while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO ProductionTimes(Itemname,StartProduction, StopProduction) VALUES('" + seps[0] + 
"','" + seps[1] + "','" + seps[2] + "');" 
      #puts queryString + "<br>"
      db.query(queryString)
      puts " Got through line " + counter.to_s + "<br>"
      counter = counter + 1
      end
      puts " You have successfully uploaded to Production Times"
  end

   # function takes in the lines from the CSV file and is only called if the user selects to add into this table
  # function will exit with a success message if it is successful and insert items into database
  
  def Software(allTheLines,size,db)
    sentinelValue = 0
    counter = 1
      while  sentinelValue < size do
      newData = allTheLines[sentinelValue]
      seps = newData.tr("\n", "").split(",", -1)
      (0..seps.length-1).each do |checkNullness|
        if seps[checkNullness] == " "
          seps[checkNullness] = "NULL"
        end
      end
      sentinelValue = sentinelValue + 1
      queryString = "INSERT INTO Software(Name,OperatingSystem,BuiltInLanguage) VALUES('" + seps[0] +
"','" + seps[1] + "','" + seps[2] + "');"
     # puts queryString + "<br>"
      db.query(queryString)
      puts " Got through line " + counter.to_s + "<br>"
      counter = counter + 1
      end
      puts " You have successfully uploaded to Software"
  end
    
db = Mysql2::Client.new(:host => '10.20.3.4',:username => 'dbms_bf',:password => 'bf_england',:database => 'dbms_bf_dbA')

print "Content-type: text/html\r\n\r\n"

uploadLocation = "/NFSHome/bfranco/public_html/UploadLocation/"
cgi = CGI.new("html5")

fromfile = cgi.params['fileName'].first
originalName = cgi.params['fileName'].first.instance_variable_get("@original_filename")

tofile = uploadLocation + originalName

File.open(tofile.untaint, 'w') { |file| file << fromfile.read}
counter = 0
sentinelValue = 0

allTheLines = IO.readlines(tofile)
lineSize = allTheLines.size
print "<HTML>\n"
print "<HEAD>"
print "<TITLE> Upload Done</TITLE></HEAD>"

print "<body>\n"

#conditonals that check which table to insert data into based on user selection

  if (cgi['TableName'] == "AddingMachines")
    AddingMachines(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "CPU")
    CPU(allTheLines,lineSize,db)
  end
  if (cgi['TableName'] == "Computer")
     Computers(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "ComputerHardware")
    ComputerHardware(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "Location")
    Location(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "Manufacturer")
     Manufacturer(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "Miscellaneous")
     Miscellaneous(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "Modem")
     Modem(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "Monitor")
     Monitor(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "Printer")
     Printer(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "ProductionTimes")
     ProductionTimes(allTheLines,lineSize,db)
  end
  
  if (cgi['TableName'] == "Software")
     Software(allTheLines,lineSize,db)
  end
  
#displays success message
print "<H1> Mass insert completed. </H1>\n"
print "Uploaded " + originalName  
print "</BODY>\n"
print "</HTML>\n"
