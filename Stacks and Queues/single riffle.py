def check_single_riffle(shuffled_deck, deck1, deck2):
    deck1_index = 0
    deck2_index = 0
    deck1_max = len(deck1) - 1
    deck2_max = len(deck2) - 1

    for card in shuffled_deck:

        if deck1_index <= deck1_max and card == deck1[deck1_index]:
            deck1_index += 1

        elif deck2_index <= deck2_max and card == deck2[deck2_index]:
            deck2_index += 1

        else:
            return False

    return True



deck = [10,20,30,40]
deck1 = [10,30,40]
deck2 = [20]
print(check_single_riffle(deck,deck1,deck2))