import numpy as np

import matplotlib.pyplot as plt
import matplotlib.collections as mc
import copy

action2vect = {0: np.array([0, -1]),
               1: np.array([0, +1]),
               2: np.array([-1, 0]),
               3: np.array([+1, 0])
               }

a2m = {0:'up', 1:'down', 2:'left', 3:'right'}

def random_initialize(Maze):
    floor_labels = np.arange(len(Maze.floors))
    start_floor_label = np.random.choice(floor_labels)
    goal_floor_label = np.random.choice(floor_labels)
    Maze.set_start(Maze.floors[start_floor_label].tolist())
    Maze.set_goal(Maze.floors[goal_floor_label].tolist())
    return Maze
        
class MazeEnv():
    def __init__(self, lx, ly, threshold=0.9, figsize=5):
        self.lx = lx
        self.ly = ly
        self.create_maze_by_normal_distribution(threshold=threshold)
        self = random_initialize(self)
        
        self.action_space = [0,1,2,3]
        self.status = 'Initialized'
        self.figsize = figsize
        
    def reset(self, coordinate=[None, None]):
        """
        put the state at the start.
        """
        if coordinate[0]!=None:
            self.state = np.array(coordinate)
        else:
            self.state = np.array(self.start)
        self.status = 'Reset'
        self.t = 0
        return self.get_state()
        
    def is_solved(self):
        """
        if the state is at the goal, returns True.
        """
        return self.goal==self.state.tolist()
    
    def get_reward(self):
        return self.is_solved()*1
    
    def get_state(self):
        """
        returns (x, y) coordinate of the state
        """
        return copy.deepcopy(self.state)#, copy.deepcopy(self.state[1])
    
    def take_action(self, action):
        add_vector_np = action2vect[action]
        if (self.state+add_vector_np).tolist() in self.floors.tolist():
            self.state = self.state+add_vector_np
            self.status = 'Moved'
        else:
            self.status = 'Move failed'
            
    def step0(self, state, action):
        add_vector_np = action2vect[action]
        if (state+add_vector_np).tolist() in self.floors.tolist():
            next_state = state+add_vector_np
            self.status = 'Moved'
        else:
            next_state = state
            self.status = 'Move failed'
        self.t += 1
        return next_state
    
    def step1(self, state, action, state_p):
        if state_p.tolist()==self.goal:
            reward = 1
        elif False:
            reward = 0.1
        else:
            reward = 0
        return reward
    
    def step(self, action):
        state = self.get_state()
        next_state = self.step0(state, action)
        reward = self.step1(state, action, next_state)
        # self.state update
        self.state = next_state
        return self.get_state(), reward, self.is_solved(), {}
    
    def step_(self, action):
        self.take_action(action)
        reward = self.get_reward()
        ob = self.get_state()
        episode_over = self.is_solved()
        return ob, reward, episode_over, {}
        
    def create_maze_by_normal_distribution(self, threshold):
        """
        creating a random maze.
        Higher threshold creates easier maze.
        around threshold=1 is recomended.
        """
        x = np.random.randn(self.lx*self.ly).reshape(self.lx, self.ly)
        y = (x < threshold)*(x > -threshold)
        self.tile = y
        self.load_tile()
        
    def load_tile(self):
        self.floors = np.array(list(np.where(self.tile==True))).T # (#white tiles, 2), 2 means (x,y) coordinate
        self.holes = np.array(list(np.where(self.tile==True))).T # (#black tiles, 2)

    def flip(self, coordinate=[None, None]):
        self.tile[coordinate[0], coordinate[1]] = not self.tile[coordinate[0], coordinate[1]]
        self.load_tile()
        
    def render(self, fig=None, ax=None, lines=None, values_table=None):
        canvas = False
        if ax!=None:
            pass
            canvas = True
            ax.clear()
        else:
            fig = plt.figure(figsize=(self.figsize, self.figsize))
            ax = fig.add_subplot(111)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
        ####
        if values_table is not None:
            lx, ly, _ = values_table.shape
            vmaxs = np.max(values_table, axis=2).reshape(lx, ly, 1)
            vt = np.transpose(values_table*self.tile.reshape(lx, ly, 1)/vmaxs, (1,0,2))
            width = 0.5
            X, Y= np.meshgrid(np.arange(0, lx, 1), np.arange(0, ly, 1))
            #values = X**2
            #print(X.shape)
            ones = .5*np.ones(lx*ly).reshape(lx, ly)
            zeros= np.zeros(lx*ly).reshape(lx, ly)
            # up
            ax.quiver(X, Y, zeros, ones, vt[:,:,0], alpha=0.8, 
                      cmap='Reds', scale_units='xy', scale=1)
            # down
            ax.quiver(X, Y, zeros, -ones, vt[:,:,1], alpha=0.8, 
                      cmap='Reds', scale_units='xy', scale=1)
            # left
            ax.quiver(X, Y, -ones, zeros, vt[:,:,2], alpha=0.8, 
                      cmap='Reds', scale_units='xy', scale=1)
            # right
            ax.quiver(X, Y, ones, zeros, vt[:,:,3], alpha=0.8, 
                      cmap='Reds', scale_units='xy', scale=1)
            #plt.colorbar(vt)
        ####
        
        ax.imshow(self.tile.T, interpolation="none", cmap='gray')
        try:
            ax.scatter(self.start[0], self.start[1], marker='x', s=100, color='blue',
                       alpha=0.8, label='start')
        except AttributeError:
            pass
        try:
            ax.scatter(self.goal[0], self.goal[1], marker='d', s=100, color='red',
                       alpha=0.8, label='goal')
        except AttributeError:
            pass
        try:
            ax.scatter(self.state[0], self.state[1], marker='o', s=100, color='black',
                       alpha=0.8, label='agent')
        except AttributeError:
            pass
        if lines is not None:
            lc = mc.LineCollection(lines, linewidths=2, color='black', alpha=0.5)
            ax.add_collection(lc)
        else:
            pass
            
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
                  scatterpoints=1)
        if canvas:
            #pass
            fig.canvas.draw()
        else:
            plt.show()
        
    def set_start(self, coordinate=[None, None]):
        if coordinate in self.floors.tolist():
            self.start = coordinate
        else:
            print('Set the start on a white tile.')
            
    def set_goal(self, coordinate=[None, None]):
        if coordinate in self.floors.tolist():
            self.goal = coordinate
        else:
            print('Set the goal on a white tile.')
                      
    def play(self, Agent, show=True):
        lines = []
        while not self.is_solved():
            state0 = self.get_state()
            action = Agent.play()
            self.step(action)
            state1 = self.get_state()
            lines.append([state0, state1])
            if show:
                self.render(lines=lines)
                
    def play_interactive(self, Agent):
        fig = plt.figure(figsize=(8, 5))
        ax = fig.add_subplot(111)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        self.render(fig=fig, ax=ax)
        lines = []
        while not self.is_solved():
            state0 = self.get_state()
            action = Agent.play()
            self.step(action)
            state1 = self.get_state()
            lines.append([state0, state1])
            self.render(fig=fig, ax=ax, lines=lines)
            #fig.canvas.draw()
        self.render(fig=fig, ax=ax, lines=lines)
        plt.show()
        print("solved!")

