# Lab6 : Swinging Up the Pendulum Using DDPG

## Overview

This lab focuses on implementing the **Deep Deterministic Policy Gradient (DDPG)** algorithm, a reinforcement learning technique designed for continuous action spaces. The objective is to train an agent to swing up and balance an **inverted pendulum** by leveraging an **actor-critic framework**.

### Key Concepts:
- **Deep Deterministic Policy Gradient (DDPG)**: A model-free, off-policy reinforcement learning algorithm that extends Deterministic Policy Gradient (DPG) with deep learning techniques.
- **Actor-Critic Architecture**: The agent consists of an **actor**, which selects actions based on the current state, and a **critic**, which evaluates the quality of these actions.
- **Continuous Action Space**: Unlike discrete action environments, the agent must learn to apply precise forces within a continuous range (`-2` to `+2`).
- **Experience Replay & Target Networks**: These enhancements improve training stability by storing past experiences for learning and preventing abrupt policy updates.
