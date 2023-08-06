import _diffcp
import cvxpy as cp
import numpy as np
import pytest
from scipy import sparse

import diffcp.cone_program as cone_prog
import diffcp.cones as cone_lib
import diffcp.utils as utils




def test_psd_dim():
    n = 1
    assert 1 == n


