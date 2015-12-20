__author__ = 'Faiku Fitim, Janusz Gradonski'

from raum.Gestirn import *
from raum.Light import *


class Fixstern(Gestirn):
    def __init__(self, position, rotSpeed, textur, planeten, anim, licht, radius, divisions):
        """
        kosnturktor um einen fixstern anzulegen
        :param position: posiition
        :param rotSpeed: rotationsgeschw
        :param textur: textur des fixsterns
        :param planeten: planeten die um ihn rotieren - koennen spaeter acuh hinuzgefuegt werden
        :param anim: animation
        :param licht: belichtung
        :param radius: radisu
        :param divisions: unterteilungen
        :return:
        """
        self.position = position  # Position im XYZ-Raum
        self.anim = anim  # Animationen an/aus
        self.textur = textur  # Textur
        self.divisions = divisions  # Unterteilungen. Mehr = feinere, schoenere Kugel
        self.licht = licht
        self.radius = radius
        self.rotation = [0, 90, 0]
        self.rotSpeed = rotSpeed
        self.inialSpeeds = [rotSpeed]

        if isinstance(planeten, list):
            self.planeten = planeten
        else:
            self.planeten = []

    def addPlanet(self, planet):
        """
        planeten hinzufuegen
        :param planet: planet der zum fixstern hinzugefuegt wird
        :return:
        """
        self.planeten.append(planet)

    def getPlanetAt(self, index):
        """
        gibt einen planeten an einem index zurueck
        :param index: index des planeten
        :return: planet
        """
        return self.planeten[index]

    def getPlaneten(self):
        """
        gitb alle planeten zurueck
        :return: alle planeten
        """
        return self.planeten

    def setAnimation(self, anim):
        """
        setzt die animation
        :param anim: animationswert
        :return:
        """
        self.anim = anim

        for x in range(0, len(self.planeten)):
            self.planeten[x].setAnimation(anim)

    def draw(self, top, zoom):
        """
        zeichnet den fixstern
        :param top:
        :param zoom:
        :return:
        """
        Gestirn.draw(self, top, zoom)

        if isinstance(self.licht, Light):
            self.licht.draw()

        for x in range(0, len(self.planeten)):
            if isinstance(self.planeten[x], Gestirn):
                self.planeten[x].draw(top, zoom)

    def update(self):
        """
        aktualisiert die bewegugn des fixsterns
        :return:
        """
        if self.anim:
            Gestirn.update(self)

        for x in range(0, len(self.planeten)):
            self.planeten[x].update()

    def animateAllChildrenFaster(self, factor, factorMov):
        """
        animiert alle kindplaneten schneller
        :param factor: geschwindigkeitsfaktor
        :param factorMov: bewegungsgeschwindigkeitfaktor
        :return:
        """
        self.rotSpeed += factor

        for i in range(0, len(self.planeten)):
            self.planeten[i].animateAllChildrenFaster(factor, factorMov)

    def animateAllChildrenSlower(self, factor, factorMov):
        """
        Alle Planeten in der Galaxie werden Langsamer
        :param factor: geschwindigkeitsfaktor
        :param factorMov: bewegungsgeschwindigkeitfaktor
        :return:
        """
        if self.rotSpeed - factor > self.inialSpeeds[0]:
            self.rotSpeed -= factor
        else:
            self.rotSpeed = self.inialSpeeds[0]

        for i in range(0, len(self.planeten)):
            self.planeten[i].animateAllChildrenSlower(factor, factorMov)

    def disableLight(self):
        """
        deaktiviert das licht
        :return:
        """
        self.licht.disable()

    def enableLight(self):
        """
        aktiviert das licht
        :return:
        """
        self.licht.enable()