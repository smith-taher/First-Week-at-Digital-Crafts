Bill = float(raw_input('Total bill amount? '))
Service = raw_input('Level of service? ')
People = int(raw_input('Split how many ways? '))

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

Amount_Person = Total / People

print 'Amount per person: $%.2f' % Amount_Person