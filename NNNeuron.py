# Tin Jukić, Seminar 2
# Artificial Neural Network Neuron

class NNNeuron:
    """
    Neuron of the Artificial Neural Network.\n
    Author: Tin Jukić
    """

    def __init__(self, num_of_weights: int):
        """
        Constructor for creating a neuron of the ANN.
        :param num_of_weights: number of weights that the neuron has
        """
        self._num_of_weights: int = num_of_weights
        self._weights: [] = []
