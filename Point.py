import math


class Point:
    nb = 0

    def _init_(self, abs, ord):
        self.__abs = abs
        self.__ord = ord
        Point.nb += 1

    @property
    def getabs(self):
        return self.__abs

    def setabs(self, value):
        self.__abs = value

    @property
    def getord(self):
        return self.__ord

    def _str_(self):
        return f'({str(self._abs)},{str(self._ord)})'

    def _eq_(self, other):
        if self._abs == other.abs and self.ord == other._ord:
            return True
        else:
            return False


    def calculer_distance(self, p):
        return math.sqrt(math.pow(self._abs - p.abs, 2) + math.pow(self.ord - p._ord, 2))

    def calculer_milieu(self, p):
        xM = (self._abs + p._abs) / 2
        yM = (self._ord + p._ord) / 2
        return Point(xM, yM)


class TroisPoints:
    def _init_(self, point1, point2, point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    @property
    def getpoint1(self):
        return self.__point1

    def setpoint1(self, value):
        self.__point1 = value

    @property
    def getpoint2(self):
        return self.__point2

    def setpoint2(self, value):
        self.__point2 = value

    @property
    def getpoint3(self):
        return self.__point3

    def setpoint3(self, value):
        self.__point3 = value

    def sont_alignes(self):
        dist1 = self._point1.calculer_distance(self._point2)
        dist2 = self._point1.calculer_distance(self._point3)
        dist3 = self._point2.calculer_distance(self._point3)

        if dist1 == dist2 + dist3 or dist2 == dist1 + dist3 or dist3 == dist1 + dist2:
            return True
        else:
            return False

    def est_isocele(self):
        dist1 = self._point1.calculer_distance(self._point2)
        dist2 = self._point1.calculer_distance(self._point3)
        dist3 = self._point2.calculer_distance(self._point3)

        if dist1 == dist2 or dist1 == dist3 or dist2 == dist3:
            return True
        else:
            return False

    @staticmethod
    def calculer_distance_statique(p1, p2):
        return Point.calculer_distance(p1, p2)

    @staticmethod
    def calculer_milieu_statique(p1, p2):
        return Point.calculer_milieu(p1, p2)