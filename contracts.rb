#!/usr/bin/ruby

choice = 'y'
cable1 = 0
cable = 0
daysInMonth = 0
dayOfMonth = 0
package = 0
mega = 49.99
megax = 69.99
megag = 89.99
contract = 0
con0 = 400
con1 = 300
con2 = 200
con3 = 100
router = 0
router1 = 100
tax = 0
total = 0
rate = 0
time = Time.new
year = time.year

while choice == 'y' do
	
  month = time.month 

  if month == 2 && (year%4==0 && year%100!=0 || year%400==0) 
     daysInMonth = 29
  elsif month == 2 && year%4!=0
     daysInMonth = 28
  elsif month == 4 || month == 6  || month == 9 || month == 11
     daysInMonth = 30
  elsif month == 1 || month == 3 || month == 5 || month ==7 || month == 8 || month == 10 || month == 12
     daysInMonth = 31
  end

  dayOfMonth = time.day
  daysLeftInMonth = daysInMonth - dayOfMonth 
 
  puts ""
  puts "It is the #{dayOfMonth} There are #{daysLeftInMonth} days out of #{daysInMonth} days left in the month"
  puts ""

  puts "Are you charging for cable?(1 or 2)" 
  puts "1)Yes"
  puts "2)No"
  cable1 = gets.chomp

  if cable1.to_i == 1
    puts "How many feet of cable?"
    cable = gets.chomp
  else
  end

  puts "Is the customer getting a router?"
  puts "1) Yes"
  puts "2) No"
  router = gets.chomp

  if router.to_i == 1
    router1 = 100
  else router.to_i == 2
    router1 = 0
  end

  puts "What package are you going to use?(1,2 or 3)"
  puts "1)Coolnet Mega"
  puts "2)Coolnet Mega Extreme"
  puts "3)Coolnet Mega Gamer"
  package = gets.chomp

  if package.to_i == 1
    packagerate = mega
  elsif package.to_i == 2
    packagerate = megax
  else package.to_i == 3
    packagerate = megag
  end

  puts "What length of contract? (0-3)"
  conlength = gets.chomp
    
  if conlength.to_i == 0
    concost = con0
  elsif conlength.to_i == 1
    concost = con1
  elsif conlength.to_i == 2
    concost = con2
  else conlength.to_i == 3
    concost = con3
  end

  puts ""
  puts ""
  puts "PackageRate: #{packagerate}"
  puts "PackageRateType: #{packagerate.class}"
  puts "DayOfMonth: #{dayOfMonth}"
  puts "DayOfMonthType: #{dayOfMonth.class}"
  puts "DaysInMonth: #{daysInMonth}"
  puts "DaysInMOnthType: #{daysInMonth.class}"
  puts ""
  puts ""
  
  prorate = packagerate*(daysLeftInMonth.to_f/daysInMonth.to_f) 

  puts "PRORRRRAAATTTEEE #{prorate}"

  subtotal = prorate.to_f + router1.to_f + concost.to_f + cable.to_f
  
  tax = subtotal.to_f * 0.05

  total = subtotal.to_f + tax.to_f
   
  puts ""
  puts "router1 = #{router1}"
  puts "packagerate = #{packagerate}"
  puts "cable = #{cable}"
  puts "days left: #{daysLeftInMonth}"
  puts "Contract cost = #{concost}"
  puts ""
  
  print "prorate = "
  puts sprintf( "$%.02f" , prorate)
  print "Subtotal = " 
  puts sprintf( "$%.02f" , subtotal )
  print "Tax = "
  puts sprintf( "$%.02f" , tax)
  print "Total = "
  puts sprintf( "$%.02f" , total)

  puts "Do you want to continue Using this program?(y/n)"
  choice = gets.chomp

end
