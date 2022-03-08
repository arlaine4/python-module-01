import sys
from copy import deepcopy


def check_sub_list_floats(input_vec):
    """
    Check list of lists of floats
    """
    for elem in input_vec:
        if type(elem) is list and len(elem) == 1 and\
                type(elem[0]) is float:
            continue
        else:
            sys.exit(f'Invalid value in vector : {input_vec}')
    return True


def init_vec(input_vec):
    # Init block for int size as input
    if type(input_vec) is int and input_vec > 0:
        return [[float(f)] for f in list(range(0, input_vec))], (1, input_vec)
    elif type(input_vec) is int and input_vec <= 0:
        sys.exit('Invalid integer for vector creation')
    # Init block for list of floats as input
    elif type(input_vec) is float:
        sys.exit('Float type not valid for vector creation')
    elif type(input_vec) is list and len(input_vec) > 0 and\
            list not in [type(f) for f in input_vec]:
        cpy_input = [float(f) for f in input_vec if type(f) is float]
        if len(cpy_input) == len(input_vec):
            return cpy_input, (1, len(input_vec))
        else:
            sys.exit(f'Invalid value in vector : {input_vec}')
    # Init block for a list of lists of floats as input
    elif type(input_vec) is list and len(input_vec) > 0 and \
            check_sub_list_floats(input_vec):
        return input_vec, (len(input_vec), 1)
    # Init block for range as input
    elif type(input_vec) is tuple and type(input_vec[0]) is int and \
            type(input_vec[1]) is int and 0 <= input_vec[0] < input_vec[1] - 1:
        return [[float(f)] for f in list(range(input_vec[0], input_vec[1] + 1))],\
               (input_vec[1], 1)
    elif type(input_vec) is tuple and (0 <= input_vec[1] < input_vec[0] - 1 or
                                       input_vec[0] == input_vec[1]):
        if input_vec[0] == input_vec[1]:
            return None, None
        else:
            sys.exit('Invalid vector')
    else:
        sys.exit(f'Invalid vector : {input_vec}')


class Vector:
    def __init__(self, input_vec):
        self.values, self.shape = init_vec(input_vec)

    def T(self):
        """
        Transpose method, changes row vector to column vector and vice versa
        """
        tmp_vec = deepcopy(self.values)
        tmp_shape = deepcopy(self.shape)
        if self.shape[0] == 1:
            self.values = [[f] for f in tmp_vec]
            self.shape = (tmp_shape[1], 1)
        else:
            self.values = [float(f[0]) for f in tmp_vec]
            self.shape = (1, tmp_shape[0])

    def add_vec_to_vec(self, other):
        """
        Handles vectors addition, both must be of the same exact dimensions
        """
        new_vec = deepcopy(self.values)
        for i in range(len(new_vec)):
            if type(self.values[0]) is not list:
                new_vec[i] += other[i]
            else:
                new_vec[i][0] += other[i][0]
        return new_vec

    def sub_vec_to_vec(self, other):
        """
        Handles vector subtraction, both must be of the same exact dimensions
        """
        new_vec = deepcopy(self.values)
        for i in range(len(new_vec)):
            if type(self.values[0]) is not list:
                new_vec[i] -= other[i]
            else:
                new_vec[i][0] -= other[i][0]
        return new_vec

    def mul_scalar_to_vec(self, scalar):
        """
        Handles vector multiplication by a scalar
        """
        new_vec = []
        for i in range(len(self.values)):
            if type(self.values[0]) is not list:
                new_vec.append(self.values[i] * scalar)
            else:
                new_vec.append([self.values[i][0] * scalar])
        return new_vec

    def div_scalar_to_vec(self, scalar):
        """
        Handles vector division by a scalar
        """
        new_vec = []
        if scalar == 0:
            sys.exit("Invalid division by 0.")
        for i in range(len(self.values)):
            if type(self.values[0]) is not list:
                new_vec.append(self.values[i] / scalar)
            else:
                new_vec.append([self.values[i][0] / scalar])
        return new_vec

    def dot_product(self, other):
        """
        Handles Vector dot product
        """
        res = 0
        if not (self.shape == other.shape and isinstance(self.values[0], type(other.values[0]))):
            sys.exit(f'Invalid dot product, dimensions does not match between vectors')
        if len(self.values) == 1 or len(other.values) == 1:
            sys.exit(f'Invalid operation between {self.values} and {other.values}')
        for i in range(len(self.values)):
            if type(self.values[0]) is not list:
                res += self.values[i] * other.values[i]
            else:
                res += self.values[i][0] * other.values[i][0]
        return res

    def verif_shape(self, other):
        if self.shape == other.shape or (self.shape[0] == other.shape[1] and self.shape[1] == other.shape[0]):
            return True
        return False

    def __add__(self, other):
        try:
            if self.verif_shape(other) and isinstance(self.values[0], type(other.values[0])):
                return Vector(self.add_vec_to_vec(other.values))
            else:
                print('Both vectors must have the same dimensions to perform addition.')
        except AttributeError:
            print("Can't add scalar to Vector")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        try:
            if self.verif_shape(other) and isinstance(self.values[0], type(other.values[0])):
                return Vector(self.sub_vec_to_vec(other.values))
            else:
                print('Both vectors must have the same dimensions to perform subtraction.')
        except AttributeError:
            print("Can't subtract scalar to Vector")

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vector(self.mul_scalar_to_vec(other))
        elif type(other) is Vector:
            return self.dot_product(other)
        else:
            print(f'Can only multiply a vector by a scalar, invalid value {other}')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        print(self, other)
        if type(other) in [int, float]:
            return Vector(self.div_scalar_to_vec(other))
        else:
            print(f'Can only divide a vector by a scalar, invalid value {other}')

    def __rtruediv__(self, other):
        if self.shape[0] != 1:
            print(f'Invalid division')
        else:
            return self.__truediv__(other)

    def __str__(self):
        return f'Vector({self.values})'

    def __repr__(self):
        return f'shape : {self.shape}\nvalues : {self.values}'
