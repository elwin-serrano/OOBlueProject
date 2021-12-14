from random import randint
from pytimedinput import timedInput

list_choice = ["earth", "water", "fire"]
# header
print("☆:::::::::::::::::::::::::::  Welcome to Hu Tao Shi  ::::::::::::::::::::::::::::::::::☆")
print("\n☆:::::::::::::::::::::::::::  Rules  ::::::::::::::::::::::::::::::::::☆")
print("You have 3 lives")
print("Pls. choose between fire, earth and water")
print("Note: Fire beats Water, Water beats Fire, Earth beats Water")
print("☆::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::☆\n")


# players life
class player:
    def __init__(self, name="player", life=3):
        self.name = name
        self.life = life


# main code
class game:
    def __init__(self):
        self.choice = 'None'
        self.score = 0

    # getting the input
    def get_input(self, choice, run):
        n = 0
        for x in range(3):
            if choice == list_choice[x]:
                n = 1
        if n == 0:
            print('No/Wrong input')
            run = False
            return run
        if n == 1:
            self.choice = choice
            return run

    def return_choice(self):
        return self.choice

    # checking the winner
    def check(self, comp_choice):
        if self.choice != "None":
            if self.choice == "earth" and comp_choice == "water":
                self.score = self.score + 1
                print("You win\n")
            elif self.choice == "earth" and comp_choice == "fire":
                self.score = self.score
                player.life = player.life - 1
                print('You lose\n')
            if self.choice == "water" and comp_choice == "fire":
                self.score = self.score + 1
                print("You win\n")
            elif self.choice == "water" and comp_choice == "earth":
                self.score = self.score
                player.life = player.life - 1
                print('You lose\n')
            if self.choice == "fire" and comp_choice == "earth":
                self.score = self.score + 1
                print("You win\n")
            elif self.choice == "fire" and comp_choice == "water":
                self.score = self.score
                player.life = player.life - 1
                print('You lose\n')
            if self.choice == comp_choice:
                print("It's a draw\n")

    # saving the score
    def return_score(self):
        return self.score


player = player()
game = game()
run = True


def main():
    while True:
        # to close if player loses all 3 life
        if player.life == 0:
            print("game over")
            print(f"final score: {game.score}")
            quit()

        else:
            # for the input timer
            run, timedOut = timedInput("Enter your pick: ", timeout=30)
            game.get_input(run, run)
            # if time runs out
            if (timedOut):
                print("Time's up, You lose")
                player.life -= 1
                print("Your score is:", game.return_score())
                print(f'{player.name} life: {player.life}\n')
                print("☆::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::☆\n")
                main()
            # if player enters his/her choice
            else:
                comp_choice = list_choice[randint(0, 2)]
                print(f"The Computer chose: {comp_choice}")
                game.check(comp_choice)
                print("Your score is:", game.return_score())
                print(f'{player.name} life: {player.life}\n')
                print("☆::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::☆\n")
                main()


# run the script
if __name__ == "__main__":
    x = str(input("press enter to continue: "))
    print("☆::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::☆\n")
    main()
