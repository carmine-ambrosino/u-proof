# u-proof
![](./app/app/static/images/uproof.png)

u-proof is a tool that harnesses the power of machine learning and LLM to identify potential phishing websites.

## Preview
![](./app/app/static/images/preview.png)

## Requirements
- [Docker](https://www.docker.com/)
- [LM studio](https://lmstudio.ai/)
- Modern web browser

## Installation
``` bash
git clone https://github.com/carmine-ambrosino/u-proof.git
cd u-proof

docker compose up -d
```
## ⚠️ Note
- Make sure to set `API_LLM` and `MODELS` in `app/app/config.py` to properly configure the connection to [LM studio](https://lmstudio.ai/).

- Load first and enable JSON mode for LLM models in [LM studio](https://lmstudio.ai/).


## Used technologies
- **Flask:** Lightweight micro web framework written in Python.
- **LM Studio:** Tool to run local LLMs.
- **Docker:** Tool that is used to automate the deployment of applications in lightweight containers so that applications can work efficiently in different environments in isolation.
- **Docker Compose:** Tool for defining and running multi-container applications.

## Project structure
![](./app/app/static/images/ProjectStructure.gif)

# Model Configuration and Hyperparameter Optimization

In what follows we report the hyperparameter search space and the best configurations obtained via Grid Search for each model.

---

## Data Split and Cross-Validation

The dataset was divided into training and test sets using a hold-out strategy with an 80/20 split. To ensure reproducibility, a fixed random seed was adopted (`random_state = 42`).

Hyperparameter optimization was performed using K-Fold cross-validation on the training set, with shuffling enabled and the following configuration:
- number of folds: 2
- shuffle: enabled
- random seed: 42

## Dataset

The dataset contains $134\text{,}847$ phishing URLs and $99\text{,}722$ legitimate URLs, each described by $56$ categorical and numerical features.


## Logistic Regression

| Parameter | Grid Search Values | Best Value |
|---------|-------------------|-----------|
| tfidf__max_features | 1000, 2000 | 1000 |
| penalty | l1, l2 | l2 |
| class_weight | None, balanced | None |
| max_iter | 100 – 1100 (500 values) | — |

---

## Bernoulli Naive Bayes

| Parameter | Grid Search Values | Best Value |
|---------|-------------------|-----------|
| tfidf__max_features | 1000, 2000 | 2000 |
| alpha | 0.01, 0.001 | 0.01 |
| fit_prior | True, False | True |

---

## K-Nearest Neighbors (KNN)

| Parameter | Grid Search Values | Best Value |
|---------|-------------------|-----------|
| tfidf__max_features | 1000, 2000 | 1000 |
| n_neighbors | 1 – 100 (step 25) | 50 |
| leaf_size | 25, 50 | 25 |
| metric | euclidean, minkowski | euclidean |
| weights | uniform, distance | uniform |

---

## Support Vector Machine (SVM)

| Parameter | Grid Search Values | Best Value |
|---------|-------------------|-----------|
| tfidf__max_features | 1000, 2000 | 1000 |
| C | 1 – 13 (5 values) | 7 |
| probability | True, False | False |
| decision_function_shape | ovo, ovr | ovr |

---

## Decision Tree

| Parameter | Grid Search Values | Best Value |
|---------|-------------------|-----------|
| tfidf__max_features | 1000, 2000 | 1000 |
| max_depth | 1 – 50 (step 25) | 25 |
| criterion | gini, entropy | entropy |

---

## Random Forest

| Parameter | Grid Search Values | Best Value |
|---------|-------------------|-----------|
| n_estimators | 50, 100, 200 | 50 |
| max_depth | 2, 3, 10, 20, None | 10 |
| criterion | gini, entropy | gini |

---

## AdaBoost

| Parameter | Grid Search Values | Best Value |
|---------|-------------------|-----------|
| n_estimators | 50, 100, 200 | 50 |
| learning_rate | 0.01, 0.1, 1.0 | 0.1 |

---

## Stacking Classifier

The Stacking Classifier is a meta-model constructed by combining the previously optimized base classifiers.
Therefore, it does not define an independent hyperparameter search space; its behavior is entirely determined by the tuned base models.

## Experimental Result

### Machine Learning Models
| Model                     | Accuracy | Precision_0 | Recall_0 | F1-score_0 | Precision_1 | Recall_1 | F1-score_1 |
|---------------------------|---------:|------------:|---------:|-----------:|------------:|---------:|-----------:|
| **Logistic Regression**   |      92% |         90% |      92% |        91% |         94% |      93% |        93% |
| **KNN**                   |      98% |        100% |      97% |        98% |         97% |     100% |        98% |
| **Decision Tree**         |      95% |         91% |      97% |        94% |         98% |      93% |        95% |
| **Bernoulli Naive Bayes** |      88% |        100% |      72% |        84% |         83% |     100% |        91% |
| **SVM**                   |      95% |         93% |      96% |        94% |         97% |      94% |        96% |
| **Random Forest**         |      96% |         97% |      97% |        97% |         98% |      97% |        97% |
| **AdaBoost**              |      95% |         91% |      97% |        94% |         98% |      93% |        95% |
| **Stacking Classifier**   |      95% |         93% |      96% |        94% |         97% |      94% |        96% |

### Large Language Models
| Model               | Accuracy | Precision_0 | Recall_0 | F1-score_0 | Precision_1 | Recall_1 | F1-score_1 |
|---------------------|---------:|------------:|---------:|-----------:|------------:|---------:|-----------:|
| **GPT 4o**          |     100% |       100% |      100% |       100% |        100% |     100% |       100% |
| **GPT 4o mini**     |      95% |       100% |       90% |        90% |         95% |     100% |        97% |
| **Claude 3 Sonnet** |      85% |       100% |       70% |        82% |         85% |     100% |        92% |
| **Claude 3 Haiku**  |      95% |       100% |       90% |        90% |         95% |     100% |        97% |
| **Copilot**         |     100% |       100% |      100% |       100% |        100% |     100% |       100% |
| **Gemini**          |      80% |        80% |       80% |        80% |         80% |      80% |        80% |
| **Llama 3.1 8B**    |      90% |        90% |       90% |        90% |         90% |      90% |        90% |
| **Mistal 7B**       |      85% |       100% |       70% |        82% |         85% |     100% |        92% |
| **Llama 2 7B**      |      85% |        76% |       82% |        79% |         82% |      72% |        77% |
| **Llama 2 13B**     |      85% |        80% |       85% |        82% |         86% |      76% |        81% |

## Example Predictions: Legitimate vs Phishing

<p align="center">
  <img src="./app/app/static/images/PredizioneCorretta.png" width="470"/>
  <img src="./app/app/static/images/PredizionePhishing.png" width="534"/>
</p>

