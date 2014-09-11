import logging
l = logging.getLogger("claripy.backends.backend_vsa")

from .backend import Backend, BackendError

class BackendVSA(Backend):
    def __init__(self):
        Backend.__init__(self)
        self._make_raw_ops(set(backend_operations), op_module=bv)
        self._make_raw_ops(set(backend_vsa_creation_operations), op_module=BackendVSA)

    def StridedInterval(self, name, size):
        pass

    def convert(self, a, result=None):
        if type(a) in { int, long, float, bool, str, BVV }:
            return a

        import ipdb; ipdb.set_trace()

from ..bv import BVV
from ..operations import backend_operations, backend_vsa_creation_operations
from .. import bv