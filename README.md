# lidarld06visualizer

The LD06 is an inexpensive LiDAR sensor, ideal for applications that do not require high-end precision.  It is usually used as an entry level system for training and in cleaning robots, due to its limited Vertical FoV of only 3 degrees, when compared with other models which offer 40 degrees. It measures 4500 times each second using a infrared laser forward and a time of flight calculation (how long it takes to reflect and come back). 

Still, the manufacturer's repo is written in C and depends on ROS to run, thereby creating a barrier to those who want a quick and simple solution to see it working

This code is based on the repo https://github.com/henjin0/LIDAR_LD06_python_loder
