import os
import random


def get_randomized_file_name(filename):
    """ Return a randomized file name for
    storage in our system.
    """
    num1 = str(random.randint(0, 1000000))
    num2 = str(random.randint(1001, 9000000))

    ext = os.path.splitext(filename)[1]
    return str(num1 + num2) + ext