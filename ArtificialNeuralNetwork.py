# Tin Jukić, Seminar 2
# Artificial Neural Network

class ArtificialNeuralNetwork:
    """
    Artificial Neural Network for solving Vehicle Routing Problem (VRP).\n
    Author: Tin Jukić
    """

    def __init__(self, num_of_weights: int, num_of_layers: int = 1):
        """
        Constructor for creating an ANN.
        :param num_of_weights: number of weights which the ANN has
        :param num_of_layers: number of hidden layers which the ANN has
        """
        self._num_of_weights: int = num_of_weights + 1  # +w0!
        self._num_of_layers: int = num_of_layers + 1  # +last layer!
        self._layers: [] = []  # ovdje trebam spremiti sve slojeve neuronske mreze
