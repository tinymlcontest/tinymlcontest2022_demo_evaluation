# How to validate X-CUBE-AI model on board

## Generate C source code

There are three additional steps compared the original code generation procedures [(Getting Started with STM32CubeAI.md)](https://github.com/tinymlcontest/tinyml_contest2022_demo_example/blob/master/README-Cube.md)：

1. When selecting X-Cube-AI package, you should choose `Application Temp`.

   <img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220826184229102.png" alt="image-20220826184229102" style="zoom:50%;" />

   Under these mode, you don't need to specify the communication serial port, just select the model.

   <img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220826184853048.png" alt="image-20220826184853048" style="zoom:50%;" />

2. The `TIM` must be enabled to perform accurate inference latency measurement: 
   ![image-20220917144705663](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220917144705663.png)
   
   Make sure the Parameter Settings are modified as the figure shown below:

   ![image-20220917144834834](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220917144834834.png)

3. When generating code, make sure to select `Basic` option in `Application Structure`. 

   <img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220915101630837.png" alt="image-20220826184853048" style="zoom:50%;" />

   `TIM` in LL library should be selected in `Project Manager-Advance Settings`.
   
   ![image-20220917145024951](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220917145024951.png)

   In order to operate the header file later, don't forget to check option `Generate peripheral initialization as a pair of '.c/.h' files per peripheral` in the Code Generator when generating code.
   
   <img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220915093242012.png" alt="image-20220915093242012" style="zoom:67%;" />



## Edit project files

1. After generating C source code based project, you should replace certain files in order to enable evaluation. All four files that should be replaced are provided. You could directly copy and paste the files from the folder `framework_x-cube-ai` to the generated project in Keil:

   1. **usart.c**
   2. **app_x-cube-ai.c**
   3. **app_x-cube-ai.h**
   4. **main.c**

2. When build the project, make sure that you check `Use MicroLIB` in `Setting-Target-Code Generation`. 

   <img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220916085712870.png" alt="image-20220915093242012" style="zoom:67%;" />

3. Once connected the board to PC, you should double-check the port number via the `Device Manager` and change it in the `validation.py` file.


## Validation

We use usb2micro usb cable to connect the development board and the upper computer to achieve communication. 

<img src="https://raw.githubusercontent.com/AugustZTR/picbed/master/img/image-20220827121203762.png" alt="image-20220827121203762" style="zoom:50%;" />

Afering connect the board to PC, run the `validation.py` , when seeing output like below, press the **reset button** shown in the picture, and the validation will start.

![iShot_2022-08-27_12.04.57](https://raw.githubusercontent.com/AugustZTR/picbed/master/img/iShot_2022-08-27_12.04.57.png)

