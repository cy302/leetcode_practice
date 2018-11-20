def card_game(n):
    cards = list(range(1, n+1))
    out_cards = []
    count = 1

    while len(cards) != 0:
        if count%2 == 1:
            a = cards[0]
            out_cards.append(a)
            cards.pop(0)
        else:
            a = copy.copy(cards[0])
            cards.pop(0)
            cards.append(a)
        count += 1

    out_cards = np.array(out_cards)
    order = [np.where(out_cards == i)[0][0]+1 for i in list(range(1, n+1))]
    return order


card_game(5)
