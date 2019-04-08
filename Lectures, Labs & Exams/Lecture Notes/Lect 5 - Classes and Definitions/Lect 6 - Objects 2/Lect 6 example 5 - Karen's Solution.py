class BasketBallPlayer:
    __playerName = ""
    __playerNumber = 0
    __playerFouls = 0
    __playerPoints = 0
    __playerOnCourt = False


    def __init__(self, name=None, number=None):
        if name is not None:
            self.__playerName = name
        if number is not None:
            self.__playerNumber = number
            self.__fouls = 0
            self.__playerOnCourt = False
            self.__playerPoints = 0

    def print_stats(self):
        print("Player Name :", self.__playerName)
        print("Player Number :", self.__playerNumber)
        print("Player Fouls :", self.__playerFouls)
        print("Player Points :", self.__playerPoints)
        print("Player on Court :", self.__playerOnCourt)


    def add_score(self, score_in):
        if score_in >=1 and score_in <= 4:
            self.__playerPoints += score_in


    def add_personal_foul(self):
        if self.__playerFouls < 5:
            self.__playerFouls += 1
        if self.__playerFouls >= 5:
            self.__playerOnCourt = False
            print("Player fouled out")


    def player_substitution(self):
        if self.__playerOnCourt is True:
            self.__playerOnCourt = False
            print("Player now off the court")
        elif self.__playerOnCourt is False and self.__playerFouls < 5:
            self.__playerOnCourt = True
            print("Player now on court")
        else:
            print("Player is fouled out and can not join the game")

stephCurry = BasketBallPlayer("Stephen Curry", 30)
score = int(input("Score:"))
stephCurry.add_score(score)
stephCurry.print_stats()


stephCurry.player_substitution()
stephCurry.print_stats()


stephCurry.add_personal_foul()
stephCurry.add_personal_foul()
stephCurry.add_personal_foul()
stephCurry.add_personal_foul()
stephCurry.add_personal_foul()


stephCurry.print_stats()
stephCurry.player_substitution()
