# 함수로 묶은 버전
import random

def dicegame():
    # Variable
    Player_life = 3
    Stage_num = 10
    Stage = 1

    # Method
    print('='*20,'GAME START!!','='*20,'\n\n')
    while Stage <= Stage_num and Player_life > 0:
        print(f'{"-"*20}Now STAGE is : {Stage}!{"-"*20}')
        print('Manager will decide the result Even(0) or Odd(1).')
        Manager_result = random.randrange(0,2)
        input('Player will roll the dice! : (PRESS ENTER)\n')
        Player_result = random.randrange(1,7)
        print(f'Player got {Player_result}!')
        Player_result = 0 if Player_result % 2 == 0 else 1
        print('\n\nNow show the result!')
        print(f'Player Result is {"Even" if Player_result == 0 else "Odd"}')
        print(f'Manager Result is {"Even" if Manager_result == 0 else "Odd"}\n')
        print(f'This time player and Manager choose {"SAME" if Player_result == Manager_result else "DIFFERENT"}!\n')
        Player_life = (Player_life - 0) if Player_result == Manager_result else (Player_life - 1)
        print(f'Stage {Stage} is over. \nPlayer Life is now {Player_life}!\n')
        Stage += 1

    print('Player WIN!!!') if Player_life > 0 else print('Player LOSE!!')
    print('='*20,'GAME OVER!!','='*20)


dicegame()