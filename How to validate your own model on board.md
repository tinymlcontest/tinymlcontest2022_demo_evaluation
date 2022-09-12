# How to validate the model with framework other than X-CUBE-AI on board

In the folder `framework_your-own`, we provide a compressed evaluation project named `TEST_OwnModel.zip`. In the project, the file `main.c` contains two functions related to the evaluation on board.

<img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220830123056603.png" alt="image-20220830123056603" style="zoom: 33%;" />

1. `MX_X_CUBE_AI_Process()` method is related to model initialization, such as loading of model activation values, etc.

2. `aiRun()` is the method of conducting inference on input IEGM segment.

When validating your own model, you can write your own model initialization and inference methods, and replace both methods. The rest of the code, including data reception, data transmission and serial communication, **MUST** be retained as a template. When loading data, the input data is a three-dimensional array `input[1][1250][1]`.

## Validation

We use usb2micro usb cable to connect the development board and the upper computer to achieve communication. 

<img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220827121203762.png" alt="image-20220827121203762" style="zoom:50%;" />

Afering connect the board to PC, run the `valaditon.py` , when seeing output like below, press the **reset button** shown in the picture, and the validation will start.

![iShot_2022-08-27_12.04.57](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/iShot_2022-08-27_12.04.57.png)

