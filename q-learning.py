import numpy as np

class SimpleApplication:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.goal_state = (4, 4)
        self.agent_state = (0, 0)

    def is_terminal(self, state):
        return state == self.goal_state

    def take_action(self, action):
        next_state = self.agent_state
        # up
        if action == 0 and self.agent_state[0] > 0:  
            next_state = (self.agent_state[0] - 1, self.agent_state[1])
        # down
        elif action == 1 and self.agent_state[0] < self.grid_size - 1:  
            next_state = (self.agent_state[0] + 1, self.agent_state[1])
        # left
        elif action == 2 and self.agent_state[1] > 0:  
            next_state = (self.agent_state[0], self.agent_state[1] - 1)
        # right    
        elif action == 3 and self.agent_state[1] < self.grid_size - 1:  
            next_state = (self.agent_state[0], self.agent_state[1] + 1)
        
        # update agent state if valid move
        if next_state != self.agent_state:
            self.agent_state = next_state
        
        # calculate reward
        # reward = -1 if next_state != self.goal_state else 100  # -1 for each step, 100 for reaching the goal
        if next_state == self.goal_state:
            reward = 100 
        else:
            distance = np.sqrt((self.goal_state[0] - next_state[0]) ** 2 + (self.goal_state[1] - next_state[1]) ** 2)
            reward = -10 * distance

        return reward, next_state

    def initial_state(self):
        return self.agent_state

class AutoBlackTest:
    def __init__(self, num_actions, num_states):
        self.num_actions = num_actions
        self.num_states = num_states
        # initialize Q-table with zeros
        self.Q = np.zeros((num_states[0], num_states[1], num_actions))  
        self.learning_rate = 0.1
        self.discount_factor = 0.9
        self.exploration_rate = 0.5

    def choose_action(self, state):
        if np.random.rand() < self.exploration_rate:
            return np.random.randint(self.num_actions)
        else:
            return np.argmax(self.Q[state[0], state[1]])  # best action

    def update_q_table(self, state, action, reward, next_state):
        if not (0 <= next_state[0] < self.num_states[0] and 0 <= next_state[1] < self.num_states[1]):
            return
        best_next_action = np.argmax(self.Q[next_state[0], next_state[1]])
        td_target = reward + self.discount_factor * self.Q[next_state[0], next_state[1], best_next_action]
        td_error = td_target - self.Q[state[0], state[1], action]
        self.Q[state[0], state[1], action] += self.learning_rate * td_error

# initialize environment and agent
grid_size = 5  
application = SimpleApplication(grid_size)
auto_test = AutoBlackTest(num_actions=4, num_states=(grid_size, grid_size))

# train the agent using Q-learning
for episode in range(5000):
    state = application.initial_state()
    while not application.is_terminal(state):
        action = auto_test.choose_action(state)
        reward, next_state = application.take_action(action)
        auto_test.update_q_table(state, action, reward, next_state)
        state = next_state

# test the agent
def test_application():
    application.agent_state = (0, 0)
    state = application.initial_state()
    steps = 0
    while not application.is_terminal(state):
        action = auto_test.choose_action(state)
        reward, next_state = application.take_action(action)
        state = next_state
        steps += 1
        act = ''
        if action == 0:
            act = 'UP   '
        elif action == 1:
            act = 'DOWN '
        elif action == 2:
            act = 'LEFT '
        elif action == 3:
            act = 'RIGHT'
        print("Step:", steps, "Action:", act, "Next state:", state)
    print("Goal reached in", steps, "steps.")

test_application()

