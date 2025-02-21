import random

choice_hand = {0: "グー", 1: "チョキ", 2: "パー"}
choice_num = tuple(choice_hand.keys())
computer_hand = random.choice(choice_num)


my_hand = 99

print("*" * 30 + f"\n 選択肢 : {choice_hand} \n" + "*" * 30)

while my_hand not in choice_num:
    my_hand = input("自分が出す手を入力してください(整数 : 0, 1, 2) > ")
    try:
        my_hand = int(my_hand)
    except ValueError:
        print("整数の0, 1, 2を入力してください")


print(f"コンピュータの出した手 : {choice_hand[computer_hand]}")
print(f"自分の出した手 : {choice_hand[my_hand]}")

result = False
if computer_hand == my_hand:
    result = "あいこ"
else:
    if computer_hand == 0 and my_hand == 2:
        result = True
    elif computer_hand == 1 and my_hand == 0:
        result = True
    elif computer_hand == 2 and my_hand == 1:
        result = True
if isinstance(result, bool):
    result = "勝ち" if result else "負け"

print(f"結果 : {result}")
