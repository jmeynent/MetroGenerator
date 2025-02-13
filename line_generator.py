import tkinter as tk
import random as rd
import numpy as np


class station:
    def __init__(self, lines: list, coor: tuple, name: str):
        self.x = coor[0]
        self.y = coor[1]
        self.corespondance = lines
        self.name = name

    def add_correspondance(self, line):
        self.corespondance.append(line)

    def __repr__(self):
        return self.name + f": {self.corespondance} at x = {self.x}, y = {self.y}"

    def rename(self, new_name):
        self.name = new_name


class lines:
    def __init__(
        self,
        number: int,
        stations: list,
        ltype: str,
        offset=(rd.normalvariate(0, 1), rd.normalvariate(0, 1)),
        angle=(rd.random * 2 * np.pi),
        radius=10,
        color=tuple(rd.randint(10, 255) for _ in range(3)),
    ):
        self.name = str(number)
        self.stations = stations
        self.type = ltype
        self.offset = offset
        self.angle = angle
        self.radius = radius
        self.color = color

    def add_station(self, station: station, index: int = -1):
        if index >= 0:
            self.stations.insert(index, station)
        else:
            self.stations.append(station)
