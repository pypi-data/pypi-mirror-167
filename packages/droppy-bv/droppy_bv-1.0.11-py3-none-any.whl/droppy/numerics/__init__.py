from .numerical_jacobian import approx_jacobian_n
from .iso_contour import FunContourGenerator

# Deprecated / renamed function
from ..tools import RenamedClass
ContourGenerator = RenamedClass(FunContourGenerator , "ContourGenerator" )