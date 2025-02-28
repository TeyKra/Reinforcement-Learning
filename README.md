# Reinforcement-Learning

This repository contains 7 branches, each dedicated to a specific reinforcement learning lab.

## Branches and Labs

1. **Reinforcement-Learning - Lab1:**
    - This lab explores value iteration and policy iteration algorithms in a maze environment modeled as an MDP. The goal is to optimize policies by maximizing expected rewards, with a comparative analysis of computational efficiency. Visualizations illustrate convergence rates and performance.

2. **Reinforcement-Learning - Lab2: OpenAI Gym Labs:**
    - **1: MountainCar-v0 with Function Approximation**
        - This lab implements the MountainCar-v0 environment using:
            - Function approximation to represent the Q-function in continuous state spaces.
            - Epsilon-greedy exploration to balance exploration and exploitation during training.
        - **Objective**: Train an agent to drive a car up a steep hill by approximating the Q-values and improving its policy iteratively.

    - **2: FrozenLake with Q-Learning**
        - This lab implements the FrozenLake environment using:
            - The Q-learning algorithm to learn an optimal policy for navigating the grid.
            - Epsilon-greedy exploration to explore the state-action space effectively.
        - **Objective**: Train an agent to navigate a grid world, avoid falling into holes, and reach the goal. The agent iteratively updates the Q-values to converge towards an optimal policy.

3. **Reinforcement-Learning - Lab3: Deep Q-Network (DQN) Implementation**
    - This lab focuses on implementing the Deep Q-Network (DQN) algorithm in the MountainCar-v0 environment. Unlike table-based RL approaches, DQN uses a neural network to approximate the Q-function in continuous state spaces.
    - **Objective**: Train an agent to overcome the steep hill by leveraging deep reinforcement learning techniques. The agent learns to optimize its policy through iterative improvements in Q-value approximations.

4. **Reinforcement-Learning - Lab4: Actor-Critic with Softmax Policy - Pendulum Swing-Up**
    - This lab develops an Actor-Critic (AC) agent to solve a continuing task in the Pendulum environment using:
        - A softmax-based policy representation for discrete action spaces, parameterized to optimize the agent's decision-making process.
        - The average reward framework to enable long-term learning in continuing tasks.
        - Differential temporal difference (TD) error to update the critic and estimate the value function accurately.
        - Gradient-based updates to improve the actor by approximating and sampling the gradient of the objective.
    - **Objective**: Train an agent to learn an optimal policy for swinging up and balancing the pendulum using Actor-Critic reinforcement learning techniques. The agent iteratively improves its performance through policy and value updates.

5. **Reinforcement-Learning - Lab5: Robot-AlphAI Q-Learning**
    - This lab focuses on implementing the **Q-learning** algorithm, a fundamental reinforcement learning technique, to train an AI-controlled robot using the **AlphAI** platform.
    - Unlike deep learning-based approaches, Q-learning uses a **Q-table** to estimate the expected rewards of different actions in a given state, allowing the agent to improve its decision-making iteratively.
        - Implementation of **Q-learning** in Python to enable the robot to learn through trial and error.
        - Configuration of the AlphAI simulation environment and initialization of the **Q-table**.
        - Development of **decision-making functions** based on Q-values.
        - Introduction of **exploration mechanisms** to balance exploration vs. exploitation.
        - Optimization of **learning parameters** (learning rate, discount factor) for improved performance.

    - **Objective**: Train a robot to navigate an environment while avoiding obstacles through reinforcement learning. The robot will learn optimal movement strategies by exploring various actions and updating its policy based on received rewards.
    - **Demonstration**:
        - Watch the robot in action using the trained **Q-learning** algorithm.  

6. **Reinforcement-Learning - Lab6: Swinging Up the Pendulum Using DDPG**  
    - This lab focuses on implementing the **Deep Deterministic Policy Gradient (DDPG)** algorithm to train an agent in the **Pendulum** environment. DDPG is an actor-critic reinforcement learning method designed for continuous action spaces.  
        - Utilizing the **average reward framework** for learning in continuing tasks.  
        - Representing the **policy as a neural network (NN)** to handle continuous action spaces efficiently.  
        - Approximating and **sampling the gradient of the objective** to update the actor network.  
        - Updating the critic using **differential temporal difference (TD) error** to estimate the value function accurately.  
    - **Objective**: Train an agent to learn an optimal **swing-up and balancing strategy** for the pendulum using **DDPG reinforcement learning techniques**. The agent iteratively improves its policy through gradient-based updates of the actor and critic networks.  

7. **Reinforcement-Learning - Lab7: Introduction to Stable Baselines - PPO**
    - This lab leverages the RL Baselines3 Zoo framework, which utilizes the Stable Baselines3 library to provide a unified interface for reinforcement learning.
    - **Key Features:**
        - **Training Scripts:** Utilize pre-built scripts for training agents.
        - **Evaluation:** Assess agent performance using standardized evaluation methods.
        - **Hyperparameter Tuning:** Easily adjust and optimize hyperparameters.
        - **Visualization:** Plot results and record training videos for comprehensive analysis.
    - **Objective:** Learn the fundamentals of using the Stable Baselines3 library by creating, training, and evaluating a PPO model. This lab demonstrates how simple it is to switch between different RL algorithms thanks to the consistent interface provided by the framework.
