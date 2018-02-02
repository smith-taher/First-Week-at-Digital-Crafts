Bill = float(raw_input('Total bill amount? '))
Service = raw_input('Level of service? ')

if Service == 'good':
    Tip = .2 * Bill
    print 'Tip amount: $%.2f' % Tip
if Service == 'fair':
    Tip = .15 * Bill
    print 'Tip amount: $%.2f' % Tip
if Service == 'bad':
    Tip = .10 * Bill
    print 'Tip amount: $%.2f' % Tip

Total = Bill + Tip
print 'Total amount: $%.2f' % Total

#I love the brevity of your code, It's very readable. 