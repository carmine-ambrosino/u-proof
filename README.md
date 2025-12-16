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

# Dataset

The **PhiUSIIL Phishing URL (Website)** dataset provides critical insights into distinguishing phishing URLs from legitimate ones through a comprehensive set of features, including URL length and domain characteristics.

The dataset contains **134,847 phishing URLs** and **99,722 legitimate URLs**, each described by **56 categorical and numerical features**.

If you use this dataset, please cite:

    Prasad, A., & Chandra, S. (2024). *PhiUSIIL Phishing URL (Website)* [Dataset].  
    UCI Machine Learning Repository.  
    https://doi.org/10.1016/j.cose.2023.103545


# Machine Learning Models

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

# Large Language Model

## oVERVIEW OF llm 
### GPT
**GPT** is a large language model (LLM) developed by OpenAI[^1]. It is characterized by strong natural language understanding and generation capabilities, positioning it as a state-of-the-art LLM. GPT demonstrates a broad vocabulary and deep contextual understanding, enabling it to produce human-like text across a wide range of topics. Its versatility is reflected in its ability to engage in dynamic dialogues, respond to complex queries, and support diverse language-based applications. The OpenAI GPT family includes GPT-2, GPT-3.5, GPT-4, and GPT-4 Mini.

### Claude
**Claude 3 Sonnet** and **Claude 3 Haiku** are LLMs developed by Anthropic[^2] and belong to the Claude 3 model family. These models offer enhanced capabilities in analysis and forecasting, advanced content generation, and code synthesis. Each variant provides a different trade-off between performance, speed, and cost, allowing users to select the most suitable model for their specific application.

### Copilot
**Copilot**, developed by Microsoft, is an LLM designed to assist users across a broad spectrum of tasks, ranging from answering factual queries to generating creative content. Its primary strength lies in producing contextually relevant outputs while augmenting responses with web-based information retrieval, thereby improving completeness and accuracy.

### LLaMa
**LLaMA** (Large Language Model Meta AI) represents a family of advanced LLMs developed by Meta. This family includes models such as LLaMA 2 8B, LLaMA 2 70B, LLaMA 3 8B, and LLaMA 3.1 8B, all trained on large-scale datasets to excel at understanding and generating natural language. Notably, the latest models, LLaMA 3 8B and LLaMA 3.1 8B, reflect the next generation of Meta’s open-source technologies. These models are designed for both versatility and efficiency, performing well in tasks that require logical reasoning and code generation, and are therefore widely adopted by developers and researchers.

### Mistral
**Mistral** models, developed by Mistral AI, establish a new benchmark in state-of-the-art AI capabilities. This family targets complex and multilingual reasoning tasks, including text comprehension and code generation. It includes Mistral Large, Medium, Next, Small, Mistral 7B, Mixtral 8x7B, and Mixtral 8x22B. Mistral Large is distinguished by its strong language understanding and generation capabilities, while Mistral Medium provides a lightweight yet highly competitive alternative, outperforming GPT-3.5 on several benchmarks. Mistral Next, a research prototype, achieves performance comparable to GPT-4. Mistral Small emphasizes efficiency and cost-effectiveness, making it suitable for low-latency applications. Finally, Mixtral is an innovative open-source mixture-of-experts model designed primarily for research use.

### Gemini
**Gemini**, one of the most recent models released by Google AI[^3], is a multimodal LLM optimized for reasoning across multiple input modalities, including text, images, video, audio, and code. Gemini has undergone extensive safety evaluations and is among the most rigorously tested Google AI models, particularly with respect to bias and toxicity mitigation. In this work, we evaluate these LLMs by equipping the proposed tool with GPT-4o, GPT-4o Mini, Claude 3.5 Sonnet, Claude 3 Haiku, LLaMA 3.1 8B, Mixtral 8x7B, Copilot, and Google Gemini.

---

[^1]: [https://chat.openai.com/](https://chat.openai.com/)

[^2]: [https://www.anthropic.com/news/claude-3-family](https://www.anthropic.com/news/claude-3-family)

[^3]: [https://bard.google.com/](https://bard.google.com/)

## LLMs via LMStudio

This tool interacts with LLMs locally through **LMStudio**. The following **GGUF** models have been used for the experiments (inference-only; no training or fine-tuning is performed within this project).

### Mistral 7B Instruct v0.2 (GGUF)

* **Repository:** `TheBloke/Mistral-7B-Instruct-v0.2-GGUF`
* **Model file:** `mistral-7b-instruct-v0.2.Q8_0.gguf`
* **Original model:** *Mistral 7B Instruct v0.2* (Mistral AI)
* **Notes:** GGUF quantized model files provided in the referenced repository.
* **Model card:** [https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF)

### Meta-Llama 3.1 8B Instruct (GGUF)

* **Repository:** `lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF`
* **Model file:** `Meta-Llama-3.1-8B-Instruct-Q8_0.gguf`
* **Original model:** *Meta-Llama-3.1-8B-Instruct* (meta-llama)
* **Notes:** Community-provided GGUF quantization (bartowski), based on a llama.cpp release.
* **Model card:** [https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF](https://huggingface.co/lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF)

---

### Meta-LLaMA 2 7B (Chat/Instruct)

* **Original model (Meta):** LLaMA 2 7B Chat
* **Official model card:**
  [https://huggingface.co/meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf)
* **GGUF repository (LMStudio-compatible):**
  `TheBloke/Llama-2-7B-Chat-GGUF`
* **Notes:** GGUF quantized version of the official chat/instruct model, suitable for local inference via LMStudio.

---

### Meta-LLaMA 2 13B (Chat/Instruct)

* **Original model (Meta):** LLaMA 2 13B Chat
* **Official model card:**
  [https://huggingface.co/meta-llama/Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf)
* **GGUF repository (LMStudio-compatible):**
  `TheBloke/Llama-2-13B-Chat-GGUF`
* **Notes:** GGUF quantized version derived from the official Meta release and used in inference-only mode.

---

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

