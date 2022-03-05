class TennisBase():
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1Points = 0
        self.p2Points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1Score()
        else:
            self.p2Score()

    def p1Score(self):
        self.p1Points +=1


    def p2Score(self):
        self.p2Points +=1

    def isDeuce(self):
        return self.p1Points==self.p2Points

    def deuceScore(self, points):
        return {
                0 : "Love-All",
                1 : "Fifteen-All",
                2 : "Thirty-All",
            }.get(points, "Deuce")

    def isWinOrAdvantage(self):
        return self.p1Points>=4 or self.p2Points>=4

    def winOrAdvantageScore(self, p1Points, p2Points):
        minusResult = p1Points - p2Points

        if (minusResult==1):
          return "Advantage " + self.player1Name
        elif (minusResult ==-1):
            return "Advantage " + self.player2Name
        elif (minusResult>=2):
            return  "Win for " + self.player1Name
        else:
            return "Win for " + self.player2Name

    def commonScore(self, p1Points, p2Points):
        pointNames = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty",
        }

        p1PointName = pointNames[p1Points]
        p2PointName = pointNames[p2Points]

        return f'{p1PointName}-{p2PointName}'
