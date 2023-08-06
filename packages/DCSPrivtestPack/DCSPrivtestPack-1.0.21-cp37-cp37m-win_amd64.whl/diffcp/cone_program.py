import multiprocessing as mp
import warnings
from multiprocessing.pool import ThreadPool

import ecos
import numpy as np
import scipy.sparse as sparse
import scs
from distutils.version import StrictVersion

import _diffcp
import diffcp.cones as cone_lib


def say_hello_from_python_cones():
    _diffcp.say_hello_cones()


