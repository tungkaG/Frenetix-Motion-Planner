FROM ros:humble

# deps for building Python packages and rosbridge
RUN apt-get update && apt-get install -y \
    python3-pip python3-colcon-common-extensions \
    ros-humble-rosbridge-server \
    && rm -rf /var/lib/apt/lists/*

# workspace
WORKDIR /root/ros2_ws
COPY ./ros2_ws/src ./src

# build
RUN . /opt/ros/humble/setup.sh && \
    colcon build && \
    echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc && \
    echo "source /root/ros2_ws/install/setup.bash" >> /root/.bashrc

# default command: just keep container alive with a shell
CMD ["bash"]
