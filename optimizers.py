import numpy as np

class Optimizer():
    def __init__(self):
        pass
    
class Qlearning_optimizer(Optimizer):
    def __init__(self, Agt, lr, gamma):
        self.Q = Agt.Policy.Q
        self.lr = lr
        self.gamma = gamma
        
    def update(self, state0, action, reward, state1):
        _s, a, r, s = state0, action, reward, state1
        deltaQ = r + self.gamma*np.max(self.Q.get_values(s)) - self.Q.get_values(_s)[a]   
        self.Q.get_values(_s)[a] += self.lr*deltaQ
        
class SARSA_optimizer(Optimizer):
    def __init__(self, Agt, lr, gamma):
        self.Agent = Agt
        self.Q = Agt.Policy.Q
        self.lr = lr
        self.gamma = gamma

    def update(self, state0, action0, reward, state1):
        action1 = self.Agent.play()
        _s,a,r,s,a_ = state0, action0, reward, state1, action1
        TD_error = r + self.gamma*self.Q.get_values(s)[a_] - self.Q.get_values(_s)[a]
        self.Q.get_values(_s)[a] += self.lr*TD_error
        
class REINFORCE_optimizer(Optimizer):
    def __init__(self, Agt, lr):
        self.Policy = Agt.Policy
        self.Q = Agt.Policy.Q
        self.lr = lr
        
    def update_single(self, state, action, orbit=[None]):
        g2 = 0
        for a in range(4):
            if a==action:
                g1 = orbit.count([state, a])*(1-self.Policy.get_prob(state)[action])
            else:
                g2+= orbit.count([state, a])
        g2*=-self.Policy.get_prob(state)[action]
        
        T = len(orbit)
        self.Q.get_values(state)[action] += (g1+g2)*self.lr/T
            
    def update(self, orbit=[None]):
        for x in range(self.Policy.Env.lx):
            for y in range(self.Policy.Env.lx):
                for action in range(4):
                    self.update_single((x, y), action, orbit)
                    
###### not yet
class ActorCritic_optimizer(Optimizer):
    def __init__(self, Actor, Critic, lrA, lrC, gamma):
        self.f = Actor.f
        self.V = Critic.V
        self.gamma = gamma
        self.lrA = lrA
        self.lrC = lrC
        
    def return_TD_error(self, x, y, xp, yp, reward):
        return reward + self.gamma*self.V[xp,yp] - self.V[x,y]
        
    def update_Critic(self, x, y, xp, yp, reward, action_label):  
        self.V[x,y] += self.lrC*self.return_TD_error(x, y, xp, yp, reward)
            
    def update_Actor(self, x, y, xp, yp, reward, action_label):
        self.f[x, y, action_label] += self.lrA*self.return_TD_error(x, y, xp, yp, reward)
