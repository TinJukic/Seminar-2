# Tin Jukić, Seminar 2
# Artificial Neural Network Layer

class NNLayer:
    """
    Layer of the Artificial Neural Network\n
    Can be hidden or final layer\n
    Author: Tin Jukić
    """

    def __init__(self, num_of_weights: int, number_of_neurons: int, hidden=True):
        """
        Constructor for creating a layer of the ANN.
        :param num_of_weights: number of weights in each neuron
        :param number_of_neurons: number of neurons in the layer
        :param hidden: specifies whether the layer is hidden or not
        """
        self._num_of_weights: int = num_of_weights
        self._num_of_neurons: int = number_of_neurons
        self._hidden: bool = hidden
