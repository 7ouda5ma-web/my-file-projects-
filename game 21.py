import time
import random


def show_title():
    print("starting game .......")
    time.sleep(3)
    print("\033[H\033[J", end="")
    print('''
   ╔══════════════════════════════╗
   ║        ♠ BLACKJACK ♠        ║
   ╠══════════════════════════════╣
   ║      A♠        K♣           ║
   ║                              ║
   ║        ASKTY KIST           ║
   ║                              ║
   ║      Q♦        J♥           ║
   ╚══════════════════════════════╝
    ''')


def create_cards():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    player_cards = [
        random.choice(cards),
        random.choice(cards)
    ]

    dealer_cards = [
        random.choice(cards),
        random.choice(cards)
    ]

    return cards, player_cards, dealer_cards


def player_turn(cards, player_cards, dealer_cards):
    game_over = False

    while not game_over:
        player_score = sum(player_cards)

        print(f"\nyour cards are: {player_cards}")
        print(f"current score is: {player_score}")
        print(f"computer's first card is: [{dealer_cards[0]}, ?]")

        if player_score == 21:
            print("Congratulations, you reached 21!")
            break

        elif player_score > 21:
            print("Unfortunately, you exceeded 21.")
            break

        choice = input("Get another card? (y/n): ").lower()

        if choice == "y":
            player_cards.append(random.choice(cards))
        else:
            game_over = True

    return player_cards


def dealer_turn(cards, dealer_cards):
    print(
        f"\ncomputer's cards: {dealer_cards}, "
        f"current score is: {sum(dealer_cards)}"
    )

    while sum(dealer_cards) < 17:
        time.sleep(1)

        new_card = random.choice(cards)
        dealer_cards.append(new_card)

        print(
            f"dealer pulled a card: {new_card}, "
            f"current score is: {sum(dealer_cards)}"
        )

    return dealer_cards


def show_result(player_cards, dealer_cards):
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)

    print("\n--- FINAL RESULT ---")
    print(f"your total: {player_score}")
    print(f"dealer total: {dealer_score}")

    if player_score > 21:
        print("You went over 21. Computer won 🎇")

    elif dealer_score > 21:
        print("Computer went over 21. You won 🎇")

    elif player_score > dealer_score:
        print("Congratulations, you won!")

    elif dealer_score > player_score:
        print("Computer won!")

    else:
        print("Draw 😊")


def play_blackjack():
    show_title()

    cards, player_cards, dealer_cards = create_cards()

    player_cards = player_turn(
        cards,
        player_cards,
        dealer_cards
    )

    if sum(player_cards) <= 21:
        dealer_cards = dealer_turn(
            cards,
            dealer_cards
        )

    show_result(
        player_cards,
        dealer_cards
    )


def main():
    game = input('''
choose a game to start.....
1-froggy
2-twenty one
3-snake
-----------
''')

    if game.lower() == "twenty one":
        play_blackjack()

main()