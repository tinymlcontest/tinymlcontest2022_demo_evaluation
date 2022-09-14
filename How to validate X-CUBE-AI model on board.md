# How to validate X-CUBE-AI model on board

## Generate C source code

For details, please refer to [Getting Started with STM32CubeAI.md](https://github.com/tinymlcontest/tinyml_contest2022_demo_example/blob/master/README-Cube.md)

There is one difference from the above document：

1. When selecting X-Cube-AI package, you should choose `Application Temp`.

   <img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220826184229102.png" alt="image-20220826184229102" style="zoom:50%;" />

   Under these mode, you don't need to specify the communication serial port, just select the model.

   <img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220826184853048.png" alt="image-20220826184853048" style="zoom:50%;" />



## Edit project files

After generating project file, you should change certain files to enable validation. The modified code refers to the codes of CubeAI version 7.2.0.

All modified files are provided. Four files should be modified in order to run the inference on board. You could directly copy and paste the files from the folder `framework_x-cube-ai` to the generated project in Keil:

1. usart.c
2. app_x-cube-ai.c
3. app_x-cube-ai.h
4. main.c

Once connected the board with PC, you should check the port number through the device manager and change it in the `validation.py` file.


## Validation

We use usb2micro usb cable to connect the development board and the upper computer to achieve communication. 

<img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220827121203762.png" alt="image-20220827121203762" style="zoom:50%;" />

Afering connect the board to PC, run the `validation.py` , when seeing output like below, press the **reset button** shown in the picture, and the validation will start.

![iShot_2022-08-27_12.04.57](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/iShot_2022-08-27_12.04.57.png)

