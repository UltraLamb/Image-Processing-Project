# Dataset Information

No downloaded dataset is used in this project.

The driving tracks and observations are generated at runtime by the Gymnasium
`CarRacing-v3` environment.

- Environment: `CarRacing-v3`
- Raw observation: 96 x 96 x 3 RGB frame
- Action space: continuous steering, gas, and brake
- Project representation: image-processing-derived road-geometry features
- Base feature vector: 16D
- Policy input: four-frame temporal stack, producing a 64D input vector

The demo videos, logs, tables, and notebook outputs in this repository are saved
project artifacts. They are evidence for the submitted package, not a separate
downloaded dataset.
