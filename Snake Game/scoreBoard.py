import turtle
from food import Food
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Food):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0,260)
        self.hideturtle()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()