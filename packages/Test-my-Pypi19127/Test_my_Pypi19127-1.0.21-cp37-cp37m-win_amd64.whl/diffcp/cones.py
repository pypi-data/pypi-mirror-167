import numpy as np
import scipy.sparse as sparse
import _diffcp
from distutils.version import StrictVersion
import scs

def say_hello_from_cones_python():
    _diffcp.say_hello_cones()