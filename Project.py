import random
 
#Bag with 10 marbles
bag = ['White','White','White','White','White','White','Black','Black','Black','Black',]

#Starting amount of money
start_amt = 1000

#Current amount
amt = start_amt

#Result of last round
result = 0

#Number of rounds
rounds = int(input("Enter Number Of Rounds: "))

#last marble
marble = 'none'

#Welcome user to game
print(f'You start the game with {start_amt} gold pieces')

#Draw marble
random.shuffle(bag)
marble = random.choice(bag)

#Loop drawing marbles
for draw in range(1,rounds+1):
    bet = int(input(f'Current Amount: {amt} Last draw:{marble} \nRound {draw} :- How much do you want to bet?: '))

# win or loss
if marble == 'White':
    result = bet*2
else:
    result = bet-bet
#calc win or loss/ result and new amount/purse
amt+=result

#lose game if lose half of money
if amt < 0.5 * start_amt:
    print(f'Game over! You lost too much gold!!!')
    

#print results
print(f'Amount: {amt}, last result: ({marble}): {result}')
print('')

# print final results
print('starting/ ending amount: ', start_amt, '/',amt)
print('gain/loss: ', ((amt-start_amt)/start_amt *100),'%')
