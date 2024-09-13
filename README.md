# lidarld06visualizer

The LD06 is an inexpensive LiDAR sensor, ideal for applications that do not require high-end precision.  It is usually used as an entry level system for training and in cleaning robots, due to its limited Vertical FoV of only 3 degrees, when compared with other models which offer 40 degrees. It measures 4500 times each second using a infrared laser forward and a time of flight calculation (how long it takes to reflect and come back) and uses serial communications to send the data. To that end, 

Still, the manufacturer's repo is written in C and depends on ROS to run, thereby creating a barrier to those who want a quick and simple solution to see it working. As such, we created this code based on the repo https://github.com/henjin0/LIDAR_LD06_python_loder, simplifying it into a single module and adding a function to 

The code is written in python and tested on an Nvidia Jetson AGX Orin under Ubuntu 22.05 Jammy, but should run with Rasperry also. To that, type python -r requirements.txt to install the required libraries

You will need an adapter such as the CP2012 TLL to serial to connect the unit through USB. 
