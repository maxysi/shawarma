fall = 'осінь'
leto = 'літо'

asking = input('укажіть пору року? ') # - осінь
print('яка пора року?\n')
if asking == leto:
    print('надворі жара, іди купайся')
elif asking == fall:
    print('надворі холодно, вдягай шапку')
else:
    print('ми хз що вам вдягати') 