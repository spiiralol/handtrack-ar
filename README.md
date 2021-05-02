# HandTrack AR

HandTrack is based of of [this code/video](https://www.youtube.com/watch?v=NZde8Xt78Iw) but I've ajdusted it and improved it.

> SIGN IN NEEDED: [Original Source Code](https://www.murtazahassan.com/courses/advance-computer-vision/lesson/basics-and-module-code/)

## Table of Contents
* [Usage](#usage)
  * [Prerequisites](#prerequisites)
  * [Download Source](#download-source)
  * [Download Module](#download-module)
* [Modules](#modules)
  * [Volume](#volume)
* [Acknowledgements](#acknowledgements)

## Usage

### Prerequisites

To use HandTrack you need Python3.7 or above or it will not run (older versions have not been tested). When installing, make sure to check the Add to PATH checkbox or Python will most likley not run on your system.

Install: [OpenCV](https://pypi.org/project/opencv-python/) and [MediaPipe](https://pypi.org/project/mediapipe/)
> Click on the links, taking you to the PyPi page which has the commands to help install.

### Download-Source

Goto [this script](https://github.com/spiiralol/handtrack-ar/blob/main/HandTrackMin.py) and download/copy & paste the code into a new python file call `handtarck.py`.

Then open a Command Prompt window which is in that directory and run
> ```python3 handtrack.py```

And there you go! When your done, just press Q to close out the window.

> To remove it saying the coords of your hands, just comment out line 27 or `print(id, cx, cy)`

### Download-Module

Goto [this script](https://github.com/spiiralol/handtrack-ar/blob/main/HandTrackModule.py) and download/copy & paste the code into a file called `HandTrackModule.py`.
Then in an existing or new app copy and paste the code from [this file](https://github.com/spiiralol/handtrack-ar/blob/main/ModuleCode.py) into that app.

Then open a Command Prompt into that directory and run
> ```python3 {file name here}.py``` replacing {file name here} with the name of your app.
> 
> To remove the printing of the hand coords, comment out `print(lmList[4])` that line of code in your app file.

## Modules

### Volume

To use the volume module, make sure you have the HandTrackModule in the same directory and download/copy & paste [this file]https://github.com/spiiralol/handtrack-ar/blob/main/modules/volume.py) and put it in the same dir (directory) as the module.

Make sure to install `pycaw` with `pip install pycaw` otherwise it won't work!


## Acknowledgements

Origin code: Murztas Workshop (YT)
Contributors: spiiralol/GateLogic
