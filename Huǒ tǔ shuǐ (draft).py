from random import randint
from threading import Timer
import sys

list_choice = ["earth", "water", "fire"]

print("Welcome to Hu Tao Shi")
print("You have 3 lives")
print("Note: Fire beats Water, Water beats Fire, Earth beats Water")
print("Choose between fire, earth and water")


class player:
    def __init__(self, name="player", life=3):
        self.name = name
        self.life = life


class game:
    def __init__(self):
        self.choice = 'None'
        self.score = 0

    def get_input(self, choice, run):
        n = 0
        for x in range(3):
            if choice == list_choice[x]:
                n = 1
        if n == 0:
            print('Wrong input pls try again')
            run = False
            return run
        if n == 1:
            self.choice = choice
            return run

    def return_choice(self):
        return self.choice

    def check(self, comp_choice):
        if self.choice != "None":
            if self.choice == "earth" and comp_choice == "water":
                self.score = self.score + 1
                print("You win")
            elif self.choice == "earth" and comp_choice == "fire":
                self.score = self.score
                player.life = player.life - 1
                print('You lose')
            if self.choice == "water" and comp_choice == "fire":
                self.score = self.score + 1
                print("You win")
            elif self.choice == "water" and comp_choice == "earth":
                self.score = self.score
                player.life = player.life - 1
                print('You lose')
            if self.choice == "fire" and comp_choice == "earth":
                self.score = self.score + 1
                print("You win")
            elif self.choice == "fire" and comp_choice == "water":
                self.score = self.score
                player.life = player.life - 1
                print('You lose')
            if self.choice == comp_choice:
                print("It's a draw")

    def return_score(self):
        return self.score


player = player()
game = game()


def main():
    def time():
        print("Time's up, You lose")
        player.life -= 1
        print("Your score is:", game.return_score())
        print(f'{player.name} life {player.life}')
        main()

    t = Timer(3, time)
    run = True
    t.start()

    while run:
        if player.life == 0:
            print("game over")
            print(f"final score: {game.score}")
            t.cancel()
            sys.exit()

        else:
            run = game.get_input(input("Enter your pick:"), run)
            t.join()

            if run == True:
                comp_choice = list_choice[randint(0, 2)]
                print(f"The Computer chose: {comp_choice}")
                game.check(comp_choice)
                print("Your score is:", game.return_score())
                print(f'{player.name} life {player.life}')
                main()

            else:
                run = True


if __name__ == "__main__":
    main()
