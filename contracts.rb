#!/usr/bin/ruby

choice = 'y'
cable1 = 0
cable = 0
month1 = 0
month2 = 0
package = 0
mega = 49.99
megax = 59.99
megag = 79.99
contract = 0
con0 = 450
con1 = 350
con2 = 250
con3 = 150
router = 0
router1 = 100
tax = 0
total = 0
rate = 0
time = Time.new
year = time.year

while choice == 'y' do
	
  month0 = time.month

  if month0 == 2 && (year%4==0 && year%100!=0 || year%400==0) 
     month1 = 29
  elsif month0 == 2 && year%4!=0
     month1 = 28
  elsif month0 == 4 || month0 == 6  || month0 == 9 || month0 == 11
     month1 == 30
  else
     month1 == 31
  end

  month2 = time.day

  month3 = month1 - month2.to_i
 
  puts ""
  puts "It is the #{month2} There are #{month3} days out of #{month1} days left in the month"
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

  prorate = (packagerate/month1)*month3.to_f

  subtotal = prorate + router1 + concost + cable.to_i
  
  tax = subtotal * 0.05

  total = subtotal + tax
   
  puts ""
  print "prorate = "
  puts sprintf( "$%.02f" , prorate)
  puts "router1 = #{router1}"
  puts "packagerate = #{packagerate}"
  puts "cable = #{cable}"
  puts "days left: #{month3}"
  puts "Contract cost = #{concost}"
  puts ""
  print "Subtotal = " 
  puts sprintf( "$%.02f" , subtotal )
  print "Tax = "
  puts sprintf( "$%.02f" , tax)
  print "Total = "
  puts sprintf( "$%.02f" , total)

  puts "Do you want to continue Using this program?(y/n)"
  choice = gets.chomp

end
