"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._config = [0]
        #pass
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._config = configuration[:]
        #print self._config
        #pass
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        lst = []
        counter = len(self._config)-1
        while counter >= 0 :
            lst.append(self._config[counter])
            counter = counter - 1
        #for index in lst :
        #    print index,
        #    print ", ",
        #print ""			
        print lst
        return ""
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._config[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for index in self._config[1:]:
            if index != 0:
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == 0:
            return False
        if self.get_num_seeds(house_num) == house_num:
            return True
        else :
            return False

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        index = 0
        if house_num != 0 :
            while index < house_num :
                self._config[index] = self._config[index] + 1
                index = index + 1
            self._config[house_num] = 0
        #pass

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        index = 1
        while index < len(self._config) :
            if self.is_legal_move(index) :
                return index
            else :
                index = index + 1
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        moves = []
        while not self.is_game_won() and self.choose_move() != 0 :
            index = self.choose_move()
            self.apply_move(index)
            moves.append(index)
            
        return moves
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
    my_game.set_board([0, 1, 2, 3, 4, 5, 6])
    # add more tests here
    
test_mancala()

import poc_mancala_gui
poc_mancala_gui.run_gui(SolitaireMancala())
# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
