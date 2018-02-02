i = 0
print "You have %s coins" % i
while True:
    coin = raw_input("Do you want another? ")
    if coin == "yes":
        i += 1
    print "You have %s coins." % i
    if coin == "no":
        print "Bye"
        break
