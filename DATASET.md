# Dataset Information

No downloaded dataset is used.

The environment generates tracks and observations at runtime:

- Environment: `CarRacing-v3`
- Observation: 96 x 96 x 3 RGB image
- Action: continuous steering, gas, brake
- Project observation wrapper: 14D ray-feature vector
- PPO input: four stacked observations = 56D
