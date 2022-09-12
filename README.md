# Evaluation code for the ACM/IEEE TinyML Contest at ICCAD 2022

## What's in this repository?

This repository contains evaluation code to evaluate three metrics of the neural network implemented with either X-CUBE-AI or other frameworks. 

This code uses four main scripts, described below, to evaluate your model on the testing dataset.

## How the evaluation is conducted?

The evaluation is mainly based on MCU. In evaluation, the PC sends one IEGM segment to the board. The board will conduct inference on the received IEGM segment and sends the inference result back to the PC. The communication is through UART. 

## How do I run these scripts?

You can run this classifier code by installing the requirements

    pip install requirements.txt

and referring to [How to validate X-CUBE-AI model on board.md](https://github.com/tinymlcontest/tinyml_contest2022_demo_evaluation/blob/main/How%20to%20validate%20X-CUBE-AI%20model%20on%20board.md) or [How to validate your own model on board.md](https://github.com/tinymlcontest/tinyml_contest2022_demo_evaluation/blob/main/How%20to%20validate%20your%20own%20model%20on%20board.md) to modify the C source code project to be deployed on board

and running

    python Validation.py

After running the scripts, the metrics
1. F_Beta score **F-B** 
2. Average latency **L** over all segments from testing dataset 

will be reported. 

The metric Flash Usage **F** is based on `Code + RO Data + RW Data` reported by Keil when building and loading the C code on board. 


## How do I obtain the final scoring?
After obtaining three metrics, you can evaluate the scores of your models using the scoring function specified in [TinyML Contest 2022 evaluation](https://tinymlcontest.github.io/TinyML-Design-Contest/Problems.html). 