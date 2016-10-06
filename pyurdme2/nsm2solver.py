""" NSM2 solver. """
import pyurdme2 as pyurdme
class NSM2Solver(pyurdme.URDMESolver):
    """ NSM2 solver class. """
    NAME = 'nsm2'

    def __init__(self, *args, **kwargs):
	raise ImportError(pyurdme.__file__)
        pyurdme.URDMESolver.__init__(self, *args, **kwargs)
        self.is_compiled = True
        self.propfilename = "solver"
        self.solver_dir = self.URDME_ROOT + '/bin/'
