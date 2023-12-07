from collections import defaultdict

with open('data.txt') as f:
    lines = f.read().splitlines()

card_values_p1 = {'2': 'A', '3': 'B', '4': 'C', '5': 'D', '6': 'E', '7': 'F', '8': 'G', '9': 'H', 'T': 'I', 'J': 'J', 'Q': 'K', 'K': 'L', 'A': 'M'}
card_values_p2 = {'J': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', 'T': 'J', 'Q': 'K', 'K': 'L', 'A': 'M'}
dict_hand = {'5 of a Kind': [], '4 of a Kind': [], 'Full House': [], '3 of a Kind': [], 'Two Pair': [], 'One Pair': [], 'High Card': []}
bids = []
hands_p1 = []
hands_p2 = []

def evaluate_hand(hand, counter, dict_hand):
    unique_cards = len(set(hand))
    if unique_cards == 1:
        dict_hand['5 of a Kind'].append(counter)
    elif unique_cards == 4:
        dict_hand['One Pair'].append(counter)
    elif unique_cards == 5:
        dict_hand['High Card'].append(counter)
    else:
        for i in hand:
            if unique_cards == 2 and hand.count(i) == 4:
                dict_hand['4 of a Kind'].append(counter)
                break
            if unique_cards == 2 and hand.count(i) == 3:
                dict_hand['Full House'].append(counter)
                break
            if unique_cards == 3 and hand.count(i) == 3:
                dict_hand['3 of a Kind'].append(counter)
                break
            if unique_cards == 3 and hand.count(i) == 2:
                dict_hand['Two Pair'].append(counter)
                break

for counter, line in enumerate(lines):
    hand, bid = line.split()
    bids.append(int(bid))
    hands_p1.append("".join(list(map(card_values_p1.get, hand))))
    hands_p2.append("".join(list(map(card_values_p2.get, hand))))
    evaluate_hand(hand, counter, dict_hand)

new_indizes = []
for key, values in dict_hand.items():
    hands_dict = defaultdict(str)
    for i in values:
        hands_dict[i] = hands_p1[i]
    hands_dict = dict(sorted(hands_dict.items(), key=lambda item: item[1])[::-1])
    new_indizes.extend(hands_dict.keys())

winnings = 0
for counter, i in enumerate(new_indizes):
    winnings += bids[i] * (len(new_indizes) - counter)

print(winnings)

# Second part logic
new_hands = []
for hand in hands_p2:
    if 'A' not in hand:
        new_hands.append(hand)
        continue

    if hand == 'AAAAA':
        new_hands.append('MMMMM')
        continue

    card_counts = {card: hand.count(card) for card in set(hand) if card != 'A'}
    if card_counts:  
        most_common_card = max(card_counts, key=card_counts.get)
        new_hand = hand.replace('A', most_common_card)
    else:  
        new_hand = 'MMMMM'  

    new_hands.append(new_hand)

dict_hand = {'5 of a Kind': [], '4 of a Kind': [], 'Full House': [], '3 of a Kind': [], 'Two Pair': [], 'One Pair': [], 'High Card': []}
for counter, hand in enumerate(new_hands):
    evaluate_hand(hand, counter, dict_hand)

new_winnings = 0
new_indizes = []
for key, values in dict_hand.items():
    hands_dict = defaultdict(str)
    for i in values:
        hands_dict[i] = hands_p2[i]
    hands_dict = dict(sorted(hands_dict.items(), key=lambda item: item[1])[::-1])
    new_indizes.extend(hands_dict.keys())

for counter, i in enumerate(new_indizes):
    new_winnings += bids[i] * (len(new_indizes) - counter)

print(new_winnings)
