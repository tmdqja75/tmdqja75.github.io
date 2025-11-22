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

As the adoption of Large Language Models (LLMs) has rapidly expanded in recent times, the focus has shifted from simply "what instructions (prompts) to input" to "how to design and manage prompts systematically." This shift has profound implications for model performance, stability, and maintainability. In this context, **DSPy (Declarative Self-improving Python)** is gaining attention by presenting a new paradigm for prompt engineering. In this article, I'll explore why DSPy is essential in the prompt engineering landscape and examine its underlying motivations.

## Problems with Traditional Prompt Engineering

Many people frequently modify prompts while using ChatGPT and often research prompt engineering techniques. While manual prompt engineering for personal tasks isn't particularly problematic, the story becomes quite different when developing actual services that leverage LLMs. Let's first examine the limitations of traditional prompt engineering when applied to real-world services.

### 1. Instability / Lack of Reproducibility

Even with identical prompts, results can vary depending on execution time, context, model type, configurations, and other factors. Minor vocabulary changes or alterations in sentence order can often lead to dramatically different outputs. This makes it challenging to expect predictable and stable behavior from the system.

### 2. Manual-Centric / High Repetitive Tuning Costs

Finding good prompts requires significant time investment. There's extensive trial-and-error involved, with heavy reliance on human intuition and instinct. Particularly for complex tasks, whenever models change or requirements shift subtly, prompts may need to be rewritten or re-tuned from scratch.

### 3. Scalability and Maintenance Challenges

When using multiple models or handling various use cases, each scenario requires individual prompt management, with version control, testing, and optimization being largely manual processes. Consequently, traditional prompt engineering processes struggle to adapt to environmental changes (such as new LLM releases).

### 4. Limited Optimization

Optimization attempts often rely solely on manually selecting a few examples (few-shot) or instructions. While the choice of examples, expression methods for instructions, and structural elements within prompts significantly impact model output quality, there are inherent limitations to humans experimenting with all possible combinations.

## DSPy's Approach to Prompt Engineering

To address the shortcomings of prompt engineering listed above, DSPy presents a fresh approach to prompt engineering based on code and programming, rather than relying on traditional manual processes.

## Components of DSPy

While DSPy API offers various components, let's explore the three most crucial ones. To explain each component, I'll use a sentiment classification task as an example.

### LM

This is the fundamental engine where DSPy programs actually call language models (LLMs). It supports multiple providers (OpenAI, Anthropic, ollama local models, etc.) and provides built-in caching functionality, enabling reuse for identical calls (prompts).

```python

import dspy
lm = dspy.LM('openai/gpt-4o-mini', temperature=0.0, max_tokens=256)

dspy.configure(lm=lm)

```

### Signature

[DSPy's official documentation](https://dspy.ai/learn/programming/signatures/) describes Signatures as follows:

> Signatures allow you to tell the LM **what** it needs to do, rather than specify **how** we should ask the LM to do it.
> {:.lead}

Signatures aren't the prompts themselves, but rather specify the format that DSPy should follow when internally constructing LM calls (prompt generation, few-shot examples, etc.). Instead of directly writing how to query the LM, you simply declare "what is needed" (input → output).

In traditional prompt engineering, you would structure prompts like this as input for the LLM:

```python
"""
You are a classifier that determines whether a sentence is positive or negative.
Look at the sentence below and determine what emotion the sentence conveys.

user_input: {user_input}

response:
"""
```

Using DSPy's Signature, you can be more explicit about input and output purposes:

```python
from typing import Literal

class Emotion(dspy.Signature):
    """Classify emotion."""

    sentence: str = dspy.InputField()
    sentiment: Literal['sadness', 'joy', 'love', 'anger', 'fear', 'surprise'] = dspy.OutputField()

```

As shown in the example above, by specifying output types or output options in the Signature, you can constrain the LM's output range and reduce incorrect label predictions.

### Modules

A Module is a component that defines, in Python class format, the method/strategy for actually receiving input and calling the LM according to the output format defined by the Signature. In other words, it determines "what prompting style, reasoning method, code execution, tools, etc., to use." DSPy provides various Modules, including the following examples:

- Predict: The most basic form, simply giving input to the LM and directly predicting output
- ChainOfThought: LM writes out its internal thought process (step-by-step) before reasoning and then outputs the final label
- ProgramOfThought: LM generates code, and the label is determined by executing that code. Example: generate sentiment analysis code → execute → obtain results
- ReAct: reasoning + tool usage to derive results

Modules can be used as shown in the code below:

```python
classify = dspy.Predict(Emotion)
result = classify(sentence="I'm so happy to see you!")

result.sentiment
>>>'joy'
```

```python
classify_cot = dspy.ChainOfThought(Emotion)
result2 = classify_cot(sentence="I'm so happy to see you!")
result.sentiment
>>>'joy'
```

### Optimizers

An Optimizer is an optimization algorithm class that automatically improves DSPy programs (module + signature configurations, etc.) by adjusting prompts (or LM weights) to maximize given metrics (e.g., accuracy, F1, etc.).

Using an Optimizer requires the following components:

- Dataset preparation suitable for the task objective (generated by LLM or created manually)

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
  },...
]

dspy_data = list()

for example in examples:
    dspy_data.append(dspy.Example(**example).with_inputs('sentence'))
```

- Setting evaluation metrics to compare prompt performance (ex: F1, Accuracy, precision, etc)

```python
def accuracy(example, prediction, trace=None) -> bool:
    return example.label == prediction.label
```

- Module containing prompts (refer to the Module section above)
- Select desired Optimizer and proceed with prompt optimization (available optimizers can be found [here](https://dspy.ai/learn/optimization/optimizers/#what-dspy-optimizers-are-currently-available))

```python
tp = dspy.MIPROv2(metric=validate_category, auto="light")
optimzed_classify = tp.compile(
  classify,
  trainset=dspy_data,
  max_labeled_demos=0,
  max_bootstrapped_demos=0
)
```

Following this step-by-step process, prompts are automatically optimized in the direction of improving evaluation metrics at each optimization step.

## Conclusion

Prompt engineering has evolved beyond simple technical techniques to become a core challenge for stably deploying LLMs in actual services. DSPy presents a new paradigm within this trend, moving beyond manual-centric prompt design toward code-based, automatic optimization-focused approaches.

As more models and Agent applications emerge in the future, the importance of programmatic approaches to prompts and systematic optimization will only grow. The code-based prompt engineering methodology provided by DSPy can help developers make prompt engineering more predictable, scalable, and maintainable.