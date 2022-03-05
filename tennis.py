# -*- coding: utf-8 -*-

from tennisBase import TennisBase


class TennisGame1(TennisBase):

    def score(self):
        if (self.isDeuce()):
            return self.deuceScore(self.p1Points)
        elif (self.isWinOrAdvantage()):
            return self.winOrAdvantageScore(self.p1Points, self.p2Points)
        else:
            return self.commonScore(self.p1Points, self.p2Points)

class TennisGame2(TennisBase):

    def score(self):
        result = ""
        if (self.isDeuce()):
            return self.deuceScore(self.p1Points)

        P1res = ""
        P2res = ""
        if (self.p1Points > 0 and self.p2Points==0):
            if (self.p1Points==1):
                P1res = "Fifteen"
            if (self.p1Points==2):
                P1res = "Thirty"
            if (self.p1Points==3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2Points > 0 and self.p1Points==0):
            if (self.p2Points==1):
                P2res = "Fifteen"
            if (self.p2Points==2):
                P2res = "Thirty"
            if (self.p2Points==3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res


        if (self.p1Points>self.p2Points and self.p1Points < 4):
            if (self.p1Points==2):
                P1res="Thirty"
            if (self.p1Points==3):
                P1res="Forty"
            if (self.p2Points==1):
                P2res="Fifteen"
            if (self.p2Points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2Points>self.p1Points and self.p2Points < 4):
            if (self.p2Points==2):
                P2res="Thirty"
            if (self.p2Points==3):
                P2res="Forty"
            if (self.p1Points==1):
                P1res="Fifteen"
            if (self.p1Points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res

        if (self.p1Points > self.p2Points and self.p2Points >= 3):
            result = "Advantage " + self.player1Name

        if (self.p2Points > self.p1Points and self.p1Points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1Points>=4 and self.p2Points>=0 and (self.p1Points-self.p2Points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2Points>=4 and self.p1Points>=0 and (self.p2Points-self.p1Points)>=2):
            result = "Win for " + self.player2Name
        return result

class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s
