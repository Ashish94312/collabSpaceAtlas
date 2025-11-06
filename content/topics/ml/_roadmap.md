---
title: "Machine Learning Learning Path"
description: "A visual roadmap for learning machine learning"
nodes:
  - id: "intro"
    label: "Introduction to ML"
    slug: "intro-to-ml"
    level: 1
    type: "foundation"
  - id: "data-prep"
    label: "Data Preparation"
    slug: "data-preparation"
    level: 2
    type: "foundation"
  - id: "linear-reg"
    label: "Linear Regression"
    slug: "linear-regression"
    level: 3
    type: "supervised"
  - id: "classification"
    label: "Classification"
    slug: "classification-basics"
    level: 3
    type: "supervised"
  - id: "ensemble"
    label: "Ensemble Methods"
    slug: "ensemble-methods"
    level: 4
    type: "advanced"
  - id: "clustering"
    label: "Clustering"
    slug: "clustering"
    level: 4
    type: "unsupervised"
  - id: "neural-nets"
    label: "Neural Networks"
    slug: "neural-networks"
    level: 5
    type: "deep-learning"
  - id: "cnn"
    label: "CNNs"
    slug: "cnn"
    level: 6
    type: "deep-learning"
  - id: "rnn"
    label: "RNNs"
    slug: "rnn"
    level: 6
    type: "deep-learning"
connections:
  - from: "intro"
    to: "data-prep"
  - from: "data-prep"
    to: "linear-reg"
  - from: "data-prep"
    to: "classification"
  - from: "linear-reg"
    to: "ensemble"
  - from: "classification"
    to: "ensemble"
  - from: "data-prep"
    to: "clustering"
  - from: "ensemble"
    to: "neural-nets"
  - from: "neural-nets"
    to: "cnn"
  - from: "neural-nets"
    to: "rnn"
---

# Machine Learning Roadmap

This visual roadmap shows the recommended learning path through machine learning concepts.

## Learning Path

Follow the connections from left to right to build your knowledge progressively.

