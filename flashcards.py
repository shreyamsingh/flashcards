from random import randint
def question(test):
   r = randint(0, len(test)-1)
   print test[r]
   new = []
   for i in range(len(test)):
      if i != r:
         new.append(test[i])
   
   ans = raw_input().split(';')
   if ans == new:
      print "correct!"
      return 1
   else:
      print "wrong", test
      return 0

questions = [['conor', 'conari', 'conatus sum', 'to try'],
['moror', 'morari', 'moratus sum', 'to delay, remain, stay'],
['vereor', 'vereri', 'veritus sum', 'to be afraid, fear'],
['collabor', 'collabi', 'collapsus sum', 'to collapse'],
['consequor', 'consequi', 'consecutus sum', 'to catch up to, overtake'],
['loquor', 'loqui', 'locutus sum', 'to speak, talk'],
['proficiscor', 'proficisci', 'profectus sum', 'to set out, leave'],
['sequor', 'sequi', 'secutus sum', 'to follow'],
['egredior', 'egredi', 'egressus sum', 'to go out, leave'],
['ingredior', 'ingredi', 'ingressus sum', 'to go in, enter'],
['regredior', 'regredi', 'regressus sum', 'to go back, return'],
['experior', 'experiri', 'expertus sum', 'to test, try']]

correct = 0
for i in range(12):
   correct += question(questions[randint(0, 11)])
print float(correct)/12.0
