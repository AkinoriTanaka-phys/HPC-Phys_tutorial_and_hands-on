import numpy as np

def get_indices(x_np, value, is_equal=True):
    """
    > x_np = np.array([10, 10, 100, 1000])
    > get_indices(x_np, 10, is_equal=True)
    >>> [0,1]
    > get_indices(x_np, 10, is_equal=False)
    >>> [2,3]
    """
    r = np.arange(len(x_np))
    ell = r[x_np==value].tolist()
    n_ell = r[x_np!=value].tolist()
    #print(equal_labels_list)
    if is_equal:
        return r[x_np==value].tolist()
    elif (not is_equal) and n_ell!=[]:
        return r[x_np!=value].tolist()
    else:
        return r.tolist()

def softmax(xs):
    num = np.exp(xs)
    den = np.sum(num)
    return num/den

class Table():
    """
    Training parameter class
    """
    def __init__(self, Env, init=0):
        self.values_table = init*np.ones(Env.lx*Env.ly*4).reshape(Env.lx, Env.ly, 4)
        
    def get_values(self, state):
        x, y = state
        return self.values_table[x, y, :]


class Policy():
    def __init__(self):
        pass
    
    def sample(self):
        action = None
        return action
    
class Random(Policy):
    def __init__(self, Env):
        self.A = Env.action_space # 迷路だと[0, 1, 2, 3]
        
    def sample(self):
        return np.random.choice(self.A)
    
class Greedy(Policy):
    def __init__(self, Env, Q=None):
        if Q is None:
            self.Q = Table(Env)
        else:
            self.Q = Q
        self.Env = Env
        
    def sample(self):
        Qvalues = self.Q.get_values(self.Env.state)
        maxQ = np.max(Qvalues)
        possible_actions = get_indices(Qvalues, maxQ, is_equal=True)
        action = np.random.choice(possible_actions)
        return action

class EpsilonGreedy(Policy):
    def __init__(self, Env, epsilon=0.1, Q=None):
        if Q is None:
            self.Q = Table(Env)
        else:
            self.Q = Q
        self.Env = Env
        self.epsilon = epsilon
        
    def sample(self):
        Qvalues = self.Q.get_values(self.Env.state)
        maxQ = np.max(Qvalues)
        r = np.random.rand()
        if r < 1- self.epsilon:
            possible_actions = get_indices(Qvalues, maxQ, is_equal=True)
        else:
            possible_actions = get_indices(Qvalues, maxQ, is_equal=False)
        
        try:## for early stage of learning
            action = np.random.choice(possible_actions)
        except ValueError:
            action = np.random.choice(np.arange(len(Qvalues))) 
            
        return action

       
class Softmax(Policy):
    def __init__(self, Env, temperature=1, Q=None):
        if Q is None:
            self.Q = Table(Env)
        else:
            self.Q = Q
        self.Env = Env
        self.temperature = temperature
        
    def get_prob(self, state):
        Qvalues = self.Q.get_values(state)
        prob = softmax(Qvalues/self.temperature)
        return prob
        
    def sample(self):
        prob = self.get_prob(self.Env.state)
        action = np.random.choice(np.arange(4), p=prob)
        return action