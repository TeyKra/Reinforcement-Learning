# Lab3: Deep Q-Learning (DQN)

In this lab, the MountainCar-v0 environment is implemented using:

- **Replay Buffer**: To store and sample past experiences for training, improving learning stability.
- **Epsilon-Greedy Exploration**: To balance exploration and exploitation, with a decaying epsilon strategy.
- **Deep Q-Network**: A neural network with three fully connected layers (128 neurons each) to approximate Q-values.

## Objective

Train an agent to drive a car up a steep hill by building momentum. The DQN algorithm learns an optimal policy in continuous state spaces by minimizing Temporal Difference Loss.

---
### Next Steps
- Experiment with larger architectures or different epsilon decay rates.
- Try more advanced environments like Atari games or continuous control tasks.
- Explore DQN extensions such as Double DQN and Prioritized Experience Replay.
