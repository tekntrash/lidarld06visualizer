# lidarld06visualizer

The LD06 is an inexpensive LiDAR sensor, ideal for applications that do not require high-end precision.  It is usually used as an entry level system for training and in cleaning robots, due to its limited Vertical FoV of only 3 degrees, when compared with much more expensive models from manufacturers such as Velodyne which offer 40 degrees or more. 

It measures 4500 times each second using a infrared laser forward and a time of flight calculation (how long it takes to reflect and come back) and uses serial communications to send the data. To that end, you will need an adapter such as the CP2102 USB to TTL UART Serial Converter to connect the LD06 through the USB ports. Connect the cables using the 2 images included in this repo. There is no need to install any driver if you are running Ubuntu, and you will see a new port appearing if you type "dir /dev/tty*". You will need to edit the code and replace that port: to us it came out as "/dev/ttyUSB0" 

Still, the manufacturer's repo is written in C and depends on ROS to run, thereby creating a barrier to those who want a quick and simple solution to see it working. As such, we created this code based on the repo https://github.com/henjin0/LIDAR_LD06_python_loder, simplifying it into a single module and adding a function to show the intensity of each dot. This is useful if the unit will be used in moving robots, as higher intensity values usually correspond to stronger reflections, which can indicate more reflective surfaces like metal or glass, while lower values might indicate less reflective surfaces like asphalt or vegetation.

The visualization is done through the matplotlib library. The code is written in python and tested on an Nvidia Jetson AGX Orin under Ubuntu 22.05 Jammy, but should run with Rasperry also. To that, type python -r requirements.txt to install the required libraries, and then simply type "python visualizer.py" and you will see an image like the one included here

**TODO**

It is theoretically possible to visualize the data using the popular RVIZ tool without having to install ROS, create packages, etc. That would greatly help those who want to experiment with LIDAR without having to install ROS (which changes drastically between versions 1 and 2 for example), running colcon build (which usually fails), etc. For that, all is required isto run apt install ros-humble-rviz2. Still, the topic protocol is  challenging, also requiring transformations in order to make the dots appear in a logical fashion. Stay tuned!

