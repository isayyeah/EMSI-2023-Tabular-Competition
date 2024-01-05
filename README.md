# Overview

## Welcome to the EMSI 2023 Tabular Competition!

Your goal in this competition is to leverage binary classification techniques to predict a patient's smoking status based on various health indicators. Enjoy the challenge and have fun!

## Evaluation

Submissions will be assessed based on the area under the Receiver Operating Characteristic (ROC) curve, measuring the relationship between predicted probabilities and observed targets.

## Submission File

Submit a file with predictions for the target variable 'smoking' for each id in the test set. The file should follow this format:

```csv
id,smoking
159256,0.5
159257,0.5
159258,0.5
...
```

## Timeline

- **Start Date:** November 22, 2023
- **Entry Deadline:** Same as the Final Submission Deadline
- **Team Merger Deadline:** Same as the Final Submission Deadline
- **Final Submission Deadline:** January 3, 2024

## Prizes

1. **1st Place:** 3 bonus points on the Final Exam + 2 bonus points (in this competition) for the entire class of the winning team.
2. **2nd Place:** 2 bonus points on the Final Exam
3. **3rd Place:** 1 bonus point on the Final Exam

**Please note:**
- Places cannot be shared.
- In case of tied rankings, priority goes to the smallest team. If still tied, a draw will determine the bonus recipient.

## About the Tabular Playground Series

The Tabular Playground Series aims to offer the Kaggle community lightweight challenges for learning and honing skills in machine learning and data science. Each competition typically lasts a few weeks, providing an opportunity for quick iteration on models, feature engineering, visualizations, and more.

## Synthetically-Generated Datasets

Playground competitions utilize synthetic data, striking a balance between real-world data with named features and the need to keep test labels private. This approach allows for more interesting datasets while addressing challenges associated with synthetic data generation. Your feedback on the datasets is encouraged to aid continuous improvement.
