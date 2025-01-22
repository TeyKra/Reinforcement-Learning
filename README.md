# Reinforcement-Learning

This repository contains four branches, each dedicated to a specific reinforcement learning lab.

## Branches and Labs

1. **Reinforcement-Learning - TP1:**
    - This project explores value iteration and policy iteration algorithms in a maze environment modeled as an MDP. The goal is to optimize policies by maximizing expected rewards, with a comparative analysis of computational efficiency. Visualizations illustrate convergence rates and performance.

2. **Reinforcement-Learning - TP2: OpenAI Gym Labs:**
    - **Lab 1: MountainCar-v0 with Function Approximation**
        - This project implements the MountainCar-v0 environment using:
            - Function approximation to represent the Q-function in continuous state spaces.
            - Epsilon-greedy exploration to balance exploration and exploitation during training.
        - **Objective**: Train an agent to drive a car up a steep hill by approximating the Q-values and improving its policy iteratively.

    - **Lab 2: FrozenLake with Q-Learning**
        - This project implements the FrozenLake environment using:
            - The Q-learning algorithm to learn an optimal policy for navigating the grid.
            - Epsilon-greedy exploration to explore the state-action space effectively.
        - **Objective**: Train an agent to navigate a grid world, avoid falling into holes, and reach the goal. The agent iteratively updates the Q-values to converge towards an optimal policy.

3. **Reinforcement-Learning - TP3: Deep Q-Network (DQN) Implementation**
    - This project focuses on implementing the Deep Q-Network (DQN) algorithm in the MountainCar-v0 environment. Unlike table-based RL approaches, DQN uses a neural network to approximate the Q-function in continuous state spaces.
    - **Objective**: Train an agent to overcome the steep hill by leveraging deep reinforcement learning techniques. The agent learns to optimize its policy through iterative improvements in Q-value approximations.

4. **Reinforcement-Learning - TP4: Actor-Critic with Softmax Policy - Pendulum Swing-Up**
    - This project develops an Actor-Critic (AC) agent to solve a continuing task in the Pendulum environment using:
        - A softmax-based policy representation for discrete action spaces, parameterized to optimize the agent's decision-making process.
        - The average reward framework to enable long-term learning in continuing tasks.
        - Differential temporal difference (TD) error to update the critic and estimate the value function accurately.
        - Gradient-based updates to improve the actor by approximating and sampling the gradient of the objective.
    - **Objective**: Train an agent to learn an optimal policy for swinging up and balancing the pendulum using Actor-Critic reinforcement learning techniques. The agent iteratively improves its performance through policy and value updates.