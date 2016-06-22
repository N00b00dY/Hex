from tkinter import *

"""
Hex Game
"""


class HexGui:
    """
    HexGui: ...
    """

    def _init__(self, m, n, game):
        canvas_width = 800
        canvas_height = 800
        python_green = "#476042"

        self.master =Tk()
        self.w = Canvas(master, width=canvas_width, height=canvas_height)
        self.w.pack()
        pass

    def receive_move(self, move):
        pass

    def set_first(self):
        pass


class HexBoard:
    """
    HexBoard: ...
    """

    def __init__(self, m, n):
        self.nodes = [[Node(i, j) for j in range(m)] for i in range(n)]
        self.__initialize_nodes(m, n)

    """
    Geht teilgraphen durch und checkt:
    Existiert ein roter teilgraph mit mindestens einem knoten aus
    {(0,0), ... , (n,0)} und {(0,m), ..., (n,m)} ?
    Existiert ein blauer teilgraph mit mindestens einem knoten aus
    {(0,0), ... , (0,m)} und {(n,0), ..., (n,m)} ?
    """
    def finished(self):
        pass

    def winner(self):
        pass

    def receive_move(self, move):
        move = (3, 4)


    def get_last_move(self):
        pass

    # String representation to test logic without GUI
    def __str__(self):
        colours = [[node.string_rep for node in row] for row in self.nodes]
        output = ""
        for i, row in enumerate(colours):
            output += i * "   " + "   ".join(row) + "\n"
        return output

    def __initialize_nodes(self, m, n):
        for i, row in enumerate(self.nodes):
            for j, node in enumerate(row):
                if i > 0:
                    node.neighbours.append(self.nodes[i - 1][j])
                if j > 0:
                    node.neighbours.append(self.nodes[i][j - 1])
                if i < n - 1:
                    node.neighbours.append(self.nodes[i + 1][j])
                if j < m - 1:
                    node.neighbours.append(self.nodes[i][j + 1])
                if i > 0 and j > 0:
                    node.neighbours.append(self.nodes[i - 1][j - 1])
                if i < n - 1 and j < m - 1:
                    node.neighbours.append(self.nodes[i + 1][j + 1])


class Game:
    """
    Game: ...
    """

    def __init__(self, m, n, mode):
        pass

    def choose_first(self):
        pass

    def current_player(self):
        pass

    def make_move(self, move):
        pass


class Node:
    """
    Might want to refractor later and create helper class file
    """

    def __init__(self, i, j):
        self.colour = None
        self.string_rep = "[ ]"  # string_rep for testing without GUI
        self.neighbours = []
        self.i = i
        self.j = j

    def __str__(self):
        return self.colour
