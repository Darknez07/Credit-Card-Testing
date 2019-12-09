import re
def Distibute(k,new_card_num):
    evens = []
    odds = []
    if k == False:
        print("Not a correct card Number")
        exit(1)
    else:
        if len(new_card_num) % 2 == 0:
            for i in range(1, len(new_card_num) + 1):
                if i % 2 == 0:
                    evens.append(int(new_card_num[i - 1]))
                else:
                    odds.append(2 * int(new_card_num[i - 1]))
    return evens,odds
def CheckforTrailofsame():
    card_num=input("Enter the card Number: ")
    new_card_num = re.sub('[^0-9]', '', card_num)
    k = True
    prev = new_card_num[0]
    for i in new_card_num[1:]:
        if prev == i:
            k = False
            break
        else:
            k = True
        prev = i
    return Distibute(k,new_card_num)
def SumNumbers(evens,odds):
    numbers = []
    for j in odds:
        if j // 10 >= 1:
            numbers.append(j % 10 + j // 10)
        else:
            numbers.append(j)
    for j in evens:
        numbers.append(j)
    return sum(numbers)
my_tup=CheckforTrailofsame()
if SumNumbers(my_tup[0],my_tup[1])%10==0:
    print("Correct Credit Card")
else:
    print("Incorrect Credit Card")
