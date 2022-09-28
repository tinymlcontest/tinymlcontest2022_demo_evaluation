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

    python validation.py

After running the scripts, the metrics
1. F_Beta score **F-B** 
2. Average latency **L** over all segments from testing dataset 

will be reported. 

The metric Flash Usage **F** is based on `Code + RO Data + RW Data` reported by Keil when building and loading the C code on board. 

## Which part of the C code I could change?
For teams using X-Cube-AI, you do not need to modify any files after replacing the 4 files to the generated C code project. If you do have some implementation to be integrated into the project, you should only make the changes inside the function [aiRun()](https://github.com/tinymlcontest/tinyml_contest2022_demo_evaluation/blob/e1c4ee97eda10267eac7a6021daf86372d506b7b/framework_x-cube-ai/main.c#L142) and [MX_CUBE_AI_Init()](https://github.com/tinymlcontest/tinyml_contest2022_demo_evaluation/blob/e1c4ee97eda10267eac7a6021daf86372d506b7b/framework_x-cube-ai/main.c#L115). 

For teams using their own framework, you should only make the changes inside the function aiRun() and Model_Init() as indicated in [How to validate the model with framework other than X-CUBE-AI on board](https://github.com/tinymlcontest/tinyml_contest2022_demo_evaluation/blob/main/How%20to%20validate%20your%20own%20model%20on%20board.md). 

The rest provided functions must be retained to enable the evaluation and fair evaluation. 

## How do I obtain the final scoring?
After obtaining three metrics, you can evaluate the scores of your models using the scoring function specified in [TinyML Contest 2022 evaluation](https://tinymlcontest.github.io/TinyML-Design-Contest/Problems.html). 

## How do I submit the design?
You can refer to [TinyML Contest 2022 Submission](https://tinymlcontest.github.io/TinyML-Design-Contest/Submission.html) for submission instructions. 
