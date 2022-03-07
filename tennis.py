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
        if (self.isDeuce()):
            return self.deuceScore(self.p1Points)
        elif (self.isWinOrAdvantage()):
            return self.winOrAdvantageScore(self.p1Points, self.p2Points)
        else:
            return self.commonScore(self.p1Points, self.p2Points)

class TennisGame3(TennisBase):

    def score(self):
        if (self.isDeuce()):
            return self.deuceScore(self.p1Points)
        elif (self.isWinOrAdvantage()):
            return self.winOrAdvantageScore(self.p1Points, self.p2Points)
        else:
            return self.commonScore(self.p1Points, self.p2Points)
