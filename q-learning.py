import numpy as np
import random
from random import uniform, randint  # Required import

# Global variables
q_table = None
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration probability

def print_table():
    """Displays the Q-table in a readable format (2 decimal places)."""
    for row in q_table:
        print(["{:.2f}".format(x) for x in row])

def init(n_state: int, n_action: int):
    """
    Initializes the Q-table with random values between -1 and 1.
    
    @param n_state: Total number of possible states.
    @param n_action: Number of possible actions.
    """
    global q_table
    q_table = np.array([[uniform(-1, 1) for _ in range(n_action)] for _ in range(n_state)])
    print("Q-table initialized:")
    print_table()  # Displaying as requested

def learn(old_state: int, action: int, reward: float, new_state: int):
    """
    Updates the Q-table using the Q-learning rule.
    
    @param old_state: Previous state.
    @param action: Executed action.
    @param reward: Immediate reward.
    @param new_state: New state after the action.
    """
    global q_table
    max_future_q = max(q_table[new_state])  # max Q(s', a')
    target = (1 - gamma) * reward + gamma * max_future_q
    q_table[old_state, action] = (1 - alpha) * q_table[old_state, action] + alpha * target

    print(f"Q-table updated after action {action} in state {old_state}:")
    print_table()

def argmax(lst):
    """Returns the index of the highest value in a list."""
    return lst.index(max(lst))

def take_decision(state: int) -> int:
    """
    Selects an action using the epsilon-greedy strategy.
    
    @param state: Current state.
    @return: The index of the chosen action.
    """
    global q_table
    if random.uniform(0, 1) < epsilon:
        action = randint(0, q_table.shape[1] - 1)  # Exploration: random action
        print("Exploration!")
    else:
        action = argmax(q_table[state].tolist())  # Exploitation: best action
    return action
