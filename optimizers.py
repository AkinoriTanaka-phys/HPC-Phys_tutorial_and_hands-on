import numpy as np

class Optimizer():
    def __init__(self, Agt):
        self.Agt = Agt
    
    def update(self):
        """
        なんかいい感じの処理
        """
        pass
    
class SARSA_optimizer(Optimizer):
    def __init__(self, Agt, eta, gamma):
        self.Agent = Agt
        self.Q = Agt.Policy.Q
        self.eta = eta
        self.gamma = gamma

    def update(self, s, a, r_next, s_next):
        a_next = self.Agent.play() # 一回プレイさせてa_nextをサンプル
        TD_error = self.Q.get_values(s)[a] - (r_next + 
                                              self.gamma*self.Q.get_values(s_next)[a_next])
        self.Q.get_values(s)[a] -= self.eta*TD_error
        
        
    
class Qlearning_optimizer(Optimizer):
    def __init__(self, Agt, eta, gamma):
        self.Agent = Agt
        self.Q = Agt.Policy.Q
        self.eta = eta
        self.gamma = gamma

    def update(self, s, a, r_next, s_next):
        error = self.Q.get_values(s)[a] - (r_next + 
                                           self.gamma*np.max(self.Q.get_values(s_next)))
                                                       # ↑ ここが変わった
        self.Q.get_values(s)[a] -= self.eta*error
       
        
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
