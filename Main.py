
#Main.py

import random
import create

#======================================================================

def DeleteHandThreeCards(player_list,player_cards):
    '''
    手札の中から3枚組みのカードを探して、あれば1枚残す処理
    
    この関数内のコードはぐちゃぐちゃでわかりにくいので
    直したい！！！！
    
    '''
    for player_number in player_list:
        deleteThreeCard = []
        
        for i in player_cards[player_number]:
            card_number = 0
            for j in player_cards[player_number]:
                if i[2:4] == (j[2:4]):
                    
                    card_number += 1
                    
            if card_number == 3:
                deleteThreeCard.append(i)
        
        number_list = []
        for i in deleteThreeCard:
            delete_number = i[2:4]
    
            if (delete_number not in number_list):
                number_list.append(delete_number)
                
                three_card_counter = 0
                for j in deleteThreeCard:
                    if i[2:4] == (j[2:4]) and three_card_counter < 2:
                        player_cards[player_number].remove(j)
                        print('3枚あったので、player_%dさんの手札から%sを削除しました' % (player_number,j))
                        three_card_counter += 1
    
        CurrentHand(player_number)            
#======================================================


def DeleteHandTwoOrFourCards(player_number):
    '''
    #手札の中から2枚組みまたは4枚組みのカードを探して、あれば捨てる処理
    '''
    
    two_or_four_card = []
    
    print('player_%dさんは手札の中でペアがないか調べています・・・' % player_number)
    
    for i in player_cards[player_number]:
        card_number = 0
        for j in player_cards[player_number]:
            if i[2:4] == (j[2:4]):
                card_number += 1
     
        if card_number == 2 or card_number == 4:
            two_or_four_card.append(i)
    
    for i in two_or_four_card:
        print('player_%dさんの手札でペアができたので%sを削除しました' % (player_number,i))
        player_cards[player_number].remove(i)
    
    CurrentHand(player_number)
#======================================================

def DrowCard(player_number,opponent_player):
    '''
    隣のプレイヤーからカードをランダムに1枚引く処理
    '''
    
    drow_card = random.choice(player_cards[opponent_player])
    print('player_%dさんはplayer_%dさんから' % (player_number,opponent_player),drow_card, 'を引きました')
    player_cards[opponent_player].remove(drow_card)
    CurrentHand(opponent_player)
    player_cards[player_number].append(drow_card)
    CurrentHand(player_number)

#======================================================

def CurrentHand(player_number):
    '''
    プレイヤーの現在の手札を表示する関数
    '''
    print('player_%dさんの現在の手札は' % player_number,player_cards[player_number])
    
#======================================================

def DeletePlayer(player_number):
    '''
    手札が0枚になったプレイヤーを
    player_listから削除する処理
    '''
    
    if len(player_cards[player_number]) == 0:
        print('player_%sさんは上がりました！！！' % player_number)
        ranking.append(player_number)
        player_list.remove(player_number)
    else:
        print('player_%sさんの手札はあと%d枚です' % (player_number,len(player_cards[player_number])))
        
#======================================================

def GameStart(player_index):
    '''
    何度も実行する関数をまとめた関数
    
    引数player_indexを元にカードを引くプレイヤーと
    カードを引かれるプレイヤーを指定して、
    各関数にそのプレイヤー番号を渡す
    '''
    
    if player_index >= len(player_list):
        player_index = 0
    
    
    #turn_playerはカードを引く人
    #opponent_playerはカードを引かれる人
    
    turn_player = player_list[player_index]
    if player_index == len(player_list) - 1:
        opponent_player = player_list[0]
    else:
        opponent_player = player_list[player_index + 1]
    
    #カードを引く人と引かれる人が決まったら
    #下の各関数を実行する
    DrowCard(turn_player,opponent_player)
    DeletePlayer(opponent_player)
    DeleteHandTwoOrFourCards(turn_player)
    DeletePlayer(turn_player)
    
    player_index += 1
    
    return player_index
    
    
#======================================================
def InitGame():
    '''
    初期化関数
    '''
    print('Game Start!!!!!!!!!!!')
    create.CreateDeck(deck)
    create.CreateHand(deck,player_numbers,player_cards)
    DeleteHandThreeCards(player_list,player_cards)

    for i in range(player_numbers):
        DeleteHandTwoOrFourCards(i)
        DeletePlayer(i)
        CurrentHand(i)
#======================================================

def MainGame():
    
    game_flag = True #ゲームが進んでいる間はTrue、ゲームを終了させたいときはFalse
    turn_counter = 0 #ターン数を表示するための変数
    player_index = 0 #player_listを指定するインデックス : player_list[player_index]
    
    #メイン処理
    while game_flag:
        turn_counter += 1
        
        player_index = GameStart(player_index)
        
        print('現在参加中のプレイヤー',player_list)
        print('%dターン目が終了しました！' % turn_counter)
        
        if len(player_list) ==  1:
                game_flag = False

#======================================================

def EndGame():
                
    print('ゲーム終了です！！')
    for i in range(player_numbers - 1):
        print('%d位はplayer_%dさんです！' % (i + 1,ranking[i]))
    print('ビリはplayer_%dさんですd(￣ ￣)' % player_list[0])


#======================================================
#変数初期化
#======================================================

player_numbers = int(input())

if player_numbers > 52:
    print( '参加人数多すぎ！！o(｀ω´ )o' )
    exit()
    
deck = [] #53枚のカードを入れる配列(デッキ)
player_list = list(range(player_numbers)) #参加プレイヤーの番号を入れる配列 : [0,1,2,...]
player_cards = [[] for i in range(player_numbers)] #手札を入れる配列を参加人数分最初に空で作る : [[],[],[],...]

ranking = [] #上がった順にプレイヤー番号を入れて、最後に順位を表示させるための配列

#======================================================

#初期化
InitGame()

#メイン
MainGame()

#終了
EndGame()

