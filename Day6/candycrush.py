'''initialization
while condition
upd
  #stmts
   '''
#break statements are like terminating the loop
'''
i=20
while i<31: 
    if i == 25:
        pass
    print(i)
    i+=1'''
#shooting bullets
'''
bullets = 10
while bullets > 0:
    print(f'{bullets} are left shoot ')
    bullets -= 1
else:
    print('game over')
    '''
#candy crush
moves = 30
winning_point = 9
while moves > 0:
    if moves == winning_point:
        print('you won the game')
        break
    print(f'{moves} moves left')
    moves -= 1
else:
    print('game over')