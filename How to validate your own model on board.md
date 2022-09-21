# How to validate the model with framework other than X-CUBE-AI on board

In the folder `framework_your-own`, we provide a compressed evaluation C code based project named `TEST_OwnModel.zip`. In the project, the file `main.c` contains two functions related to the evaluation on board. Those two functions should be modified by the team with their own implementations. 

1. `Model_Init()` method is the function to load model weights, activation values, etc.

2. `aiRun()` is the function to conduct inference on the input IEGM segment.

![iShot_2022-08-27_12.04.57](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220921101009276.png)

When validating your own model, you can write your own model weights loading and inference functions, and replace the aforementioned two functions with your own design. The rest of the code, including data reception, data transmission and serial communication, **MUST** be retained as a template. 

## Validation

We use usb2micro usb cable to connect the development board and the upper computer to achieve communication. 

<img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220827121203762.png" alt="image-20220827121203762" style="zoom:50%;" />

Afering connect the board to PC, run the `validation.py` , when seeing output like below, press the **reset button** shown in the picture, and the validation will start.

![iShot_2022-08-27_12.04.57](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/iShot_2022-08-27_12.04.57.png)

