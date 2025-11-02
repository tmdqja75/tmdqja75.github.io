---
layout: post
title: Systematic Prompt Engineering with DSPy
image:
  path: https://miro.medium.com/v2/resize:fit:2000/1*5bWUR3N5ki5mE5D6aGZLQA.png
description: >
  Systematic prompt management using metrics
categories: llm
sitemap:
  changefreq: weekly
comments: true
---

* this list will be replaced by the table of contents
{:toc}

As the use of large language models (LLMs) has rapidly expanded, the way we design and manage prompts has become increasingly crucial to model performance, stability, and maintainability—far more than simply considering "what prompt to input." In this context, **DSPy (Declarative Self-improving Python)** is gaining attention as it proposes a new paradigm for prompt engineering. In this article, we will summarize the necessity and motivation behind DSPy in the realm of prompt engineering.

## Issues with Traditional Prompt Engineering

Many individuals frequently modify prompts while using ChatGPT and seek out various prompt engineering techniques. While manual prompt engineering may not be a significant issue for personal tasks, the scenario changes when developing real services leveraging LLMs. Let’s examine the limitations of traditional prompt engineering when applied to actual services.

### 1. Lack of Stability / Reproducibility

Even the same prompt can yield different results depending on the execution time, context, model type, and settings. Minor variations in vocabulary or changes in sentence order can lead to significantly different outputs. This variability makes it challenging to expect predictable and stable behavior from the system.

### 2. Labor-Intensive Process / High Costs of Iterative Tuning

Significant time is often spent searching for effective prompts, relying heavily on trial-and-error approaches and human intuition. This is particularly pronounced for complex tasks, where modifying or tuning prompts may be necessary each time the model changes or the requirements shift slightly.

### 3. Challenges with Scalability and Maintenance

When utilizing multiple models or having various use cases, managing prompts for each case becomes essential, leading to much manual work in version control, testing, and optimization. Therefore, the existing prompt engineering processes struggle to adapt to changes in the environment (e.g., the release of new LLMs).

### 4. Limited Optimization

Optimization is often attempted solely through selecting a few examples or instructions manually. The manner in which examples are chosen, how instructions are phrased, and the structure within the prompt significantly affect the quality of the model's output, yet human experimentation with all combinations is limited.

## DSPy’s Proposed Directions for Prompt Engineering

To address the aforementioned shortcomings in prompt engineering, DSPy presents a fresh approach that leverages programming and code-based methodologies, moving away from reliance on manual processes.

## Components of DSPy

Though the DSPy API offers various components, let’s focus on the three most important ones. We will use a task that classifies emotions from sentences as an example to explain each component.

### LM

LM serves as the fundamental engine that calls the actual language model (LLM) within DSPy. It supports multiple providers (OpenAI, Anthropic, ollama local models, etc.) and primarily offers caching functionality, allowing for reuse of identical calls (prompts).

```python
import dspy
lm = dspy.LM('openai/gpt-4o-mini', temperature=0.0, max_tokens=256)

dspy.configure(lm=lm)
```

### Signature

According to [DSPy’s official documentation](https://dspy.ai/learn/programming/signatures/):

> Signatures allow you to tell the LM **what** it needs to do, rather than specify **how** we should ask the LM to do it.

Instead of specifying how to request the LLM, Signatures let you instruct the LLM on **what** it is required to perform. 

Signatures do not constitute the prompt itself; rather, they serve as a format that DSPy adheres to when configuring LLM calls (prompt generation, few-shot examples, etc.). This means you declare what is needed (input → output) without writing the query directly to the LLM.

In traditional prompt engineering, you would structure the prompt as follows for input into the LLM:

```python
"""
You are a classifier that determines whether a sentence is positive or negative.
Look at the sentence below and determine what emotion it conveys:

user_input: {user_input}

response:
"""
```

Utilizing DSPy’s Signature allows for clearer delineation of inputs and outputs, as shown below:

```python
from typing import Literal

class Emotion(dspy.Signature):
    """Classify emotion."""

    sentence: str = dspy.InputField()
    sentiment: Literal['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'] = dspy.OutputField()
```

By specifying output types and options within the Signature, the output scope of the LLM can be constrained, thereby reducing incorrect label predictions.

### Modules

Modules are components within DSPy that define how inputs are processed and called to the LLM in the output format defined by the Signature, presented in Python class format. They determine "which prompting style, reasoning approach, code execution, tools, etc., will be applied." DSPy provides a variety of Modules, including the following examples:

- Predict: The most basic form, simply providing input to the LLM and receiving the output prediction.
- ChainOfThought: The LLM articulates its internal reasoning process step-by-step and then outputs a final label.
- ProgramOfThought: The LLM generates code, which is then executed to determine the label (e.g., creating emotional analysis code → executing → obtaining results).
- ReAct: Combining reasoning with tool usage to derive outcomes.

Modules can be utilized as follows:

```python
classify = dspy.Predict(Emotion)
result = classify(sentence="I’m so happy to see you!")

result.sentiment
>>>'joy'
```

```python
classify_cot = dspy.ChainOfThought(Emotion)
result2 = classify_cot(sentence="I’m so happy to see you!")
result.sentiment
>>>'joy'
```

### Optimizers

Optimizers are classes of algorithms that automatically enhance the DSPy program (module + signature settings, etc.) by adjusting prompts (or LM weights) to maximize a given metric (e.g., accuracy, F1 score).

To use an Optimizer, the following components are needed:

- Preparation of a dataset suitable for the task's purpose (either generated by the LLM or created manually).

```python
examples = [
  {
    "sentence": "I'm happy",
    "sentiment": "joy"
  },
  {
    "sentence": "I'm sad",
    "sentiment": "sadness"
  },
  {
    "sentence": "I'm scared!",
    "sentiment": "fear"
  },
  ...
]

dspy_data = list()

for example in examples:
    dspy_data.append(dspy.Example(**example).with_inputs('sentence'))
```

- Setting evaluation metrics to compare prompt performance (e.g., F1, accuracy, precision, etc.)

```python
def accuracy(example, prediction, trace=None) -> bool:
    return example.label == prediction.label
```

- A module that includes the prompt (refer to the Module section).
- Selecting the desired Optimizer and proceeding with prompt optimization (you can find the available optimizers [here](https://dspy.ai/learn/optimization/optimizers/#what-dspy-optimizers-are-currently-available)).

```python
tp = dspy.MIPROv2(metric=validate_category, auto="light")
optimzed_classify = tp.compile(
  classify,
  trainset=dspy_data,
  max_labeled_demos=0,
  max_bootstrapped_demos=0
)
```

By following these process steps, the prompts will be automatically optimized in a way that improves the evaluation metrics with each optimization iteration.

## Conclusion

Prompt engineering has emerged as a critical challenge, extending beyond a simple technical technique to reliably implementing LLMs in real services. Within this trend, DSPy offers a new paradigm centered on code-based, automatic optimization, moving past manual prompt design.

As more models and agent applications emerge, the significance of a programming-based approach to prompts and systematic optimization will only increase. The code-based prompt engineering method provided by DSPy enables developers to create a more predictable, scalable, and maintainable process for prompt engineering.