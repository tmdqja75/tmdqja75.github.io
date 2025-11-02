---
layout: post
title: MLOps 💙 Kubernetes
image: 
  path: /assets/post_banner/mlops-k8s.png
description: >
  Exploring the powerful synergy between MLOps and Kubernetes.
categories: mlops
sitemap:
    changefreq : weekly
comments: true
---

* this list will be replaced by the table of contents
{:toc}

## 🦾 Many Companies are Using Kubernetes

When you look at job postings for "ML Engineer" or "MLOps Engineer," there’s one term that consistently pops up.

![k8s-jd](<../../assets/img/blog/mlops-k8s/mlops-jd.png>)

*Source: Toss, Craft Technologies, MachinaLabs MLOps Engineer job description*

That term is **Kubernetes (k8s)**. What is it about this complex-sounding technology that so many companies are using it to train and deploy machine learning models? Let's delve into the reasons why businesses are adopting Kubernetes.

In this post, we will explore the overall reasons for using Kubernetes within the MLOps framework.

## 😵‍💫 It Feels Like It Could Collapse with a Slight Push

Before we examine why companies choose K8s, let’s take a look at the chart below.

![k8s-complex](../../assets/img/blog/mlops-k8s/complex-mlops.png)

*Source: Machine Learning Operations (MLOps): Overview, Definition, and Architecture*

This flowchart summarizes the steps involved in deploying a model to an actual service within MLOps. Quite complex, isn’t it? Imagine trying to manage and monitor such a convoluted process without a systematic system in place. Even a small problem or error can snowball and halt the entire development flow, inevitably causing bottlenecks that significantly slow down the team's progress. Hence, to create a stable and efficient MLOps environment, tools and systems capable of managing this complexity are essential.

## 🐳 Why Use K8s?

Machine learning and deep learning workloads are resource-intensive, requiring repetitive experiments and stable service operation. Kubernetes offers key features like scalability, portability, reproducibility, and fault tolerance to effectively and reliably manage the training and deployment environments of ML models.

### 1. **Scalability**
   - One of the most important advantages of Kubernetes is its ability to automatically scale resources up or down according to workload and circumstances. For instance, if there’s a sudden increase in traffic during ML model training or inference services, it can automatically expand the number of pods to maintain performance. When usage decreases, it reduces unnecessary resources, cutting costs. This means Kubernetes allows for flexible responses to changing environments, ensuring both stability and efficiency.

### 2. **Portability**
   - A major advantage of Kubernetes is that it is not tied to any specific cloud provider, making it usable anywhere. As an open-source platform, anyone can use it freely, and the standardized APIs allow services to run similarly across different clouds like AWS and GCP. Plus, because it is container-based, it can be transferred across different environments—whether cloud or on-premises—thanks to its cross-platform compatibility (though moving to on-premises may require additional considerations).

### 3. **Reproducibility**
   - ML experimentation and model development are highly repetitive processes, and accurately reproducing experimental results is a fundamental requirement in MLOps. Kubernetes uses containers to create immutable images of everything from learning code and library versions to the operating system environment. This allows for perfect control over datasets, code, and environment variables, enabling repeatable experiments and fundamentally resolving persistent issues like "It works on my computer..."

### 4. **Fault Tolerance**
   - In long-running model training tasks or 24/7 inference services, hardware or software failures can be catastrophic. Kubernetes has built-in self-healing features, automatically rescheduling workloads from nodes or pods that experience failures to healthy nodes to restore services. This robust fault tolerance guarantees the stability of ML pipelines, allowing systems to operate continuously without manual intervention.

## ✅ Conclusion

In this article, we discussed the importance of Kubernetes within the MLOps environment, focusing on key advantages like scalability, portability, reproducibility, and fault tolerance. In summary, Kubernetes serves as a powerful foundation that helps operate complex ML workloads reliably and flexibly. In the next post, we will delve deeper into how Kubernetes is utilized in the actual processes of model training and deployment with concrete examples.

### References
- [Toss MLOps Engineer](https://toss.im/career/job-detail?job_id=6072871003)
- [Craft Technologies MLOps Engineer](https://www.wanted.co.kr/wd/297084)
- [MachinaLabs MLOps Engineer](https://www.wanted.co.kr/wd/302165)
- [Samsung SDS: Adoption of a Kubernetes-based MLOps Platform using Open Source](https://www.samsungsds.com/kr/techreport/kubernetes-mlops.html)
- [Machine Learning Operations (MLOps): Overview, Definition, and Architecture](https://arxiv.org/pdf/2205.02302)