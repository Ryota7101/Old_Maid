
#create.py

import random

def CreateDeck(deck):
    '''
    53枚のトランプのまとまり(デッキ)を作る処理
    '''
    card_mark = ['S','H','C','D']
    for i in card_mark:
        for j in range(1,14):
            deck.append(i + '-' + str(j))
    deck.append('J-0')
    
    random.shuffle(deck)
    
    
def CreateHand(deck,player_numbers,player_cards):
    '''
    デッキから参加人数分の手札を作る処理
    '''
    player_number = 0
    for i in deck:
        player_cards[player_number].append(i)
        player_number += 1
        if (player_number >= player_numbers):
            player_number = 0
            
    
    print(player_cards[0])
    print(player_cards[1])
    print(player_cards[2])