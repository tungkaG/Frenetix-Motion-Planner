class CartesianSample:
    def __init__(self):
        self.x = []
        self.y = []
        self.theta = []
        self.v = []            
        self.acceleration = []
        self.a = []
        self.kappa = []
        self.kappa_dot = []   

class CurvilinearSample:
    def __init__(self):
        self.s = []
        self.s_dot = []
        self.s_ddot = []
        self.d = []              
        self.d_dot = []
        self.d_ddot = []
        
class TrajectoryBoard:
    def __init__(self):
        self.valid = True
        self.cartesian = CartesianSample()
        self.curvilinear = CurvilinearSample()
        self.cost = []
        self.feasible = []
        self._coll_detected = None