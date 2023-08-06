#include <pybind11/eigen.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "cones.h"
#include "deriv.h"
#include "linop.h"
#include "lsqr.h"

namespace py = pybind11;

PYBIND11_MODULE(_diffcp, m) {
  m.doc() = "Testing github actions.";

  m.def("say_hello_cones", &say_hello_cones);
  m.def("say_hello_linop", &say_hello_linop);
}
