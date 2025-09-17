#!/usr/bin/env python3
import yaml
import os
from PIL import Image
home_path = os.path.expanduser('~')
print(home_path)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_image_size(image_path):
    with Image.open(image_path) as img:

        return img.size  # returns (width, height)

def write_world_file(size_x, size_y, pose_0, pose_1, bitmap="from_hlc.png", world_file_path = home_path + "/catkin_ws/install_isolated/share/agv_files/simulate/maps_drawn/kas.world"):
    with open(world_file_path, 'r') as file:
        lines = file.readlines()

    new_floorplan = f"""floorplan
(
  name "maze"
  bitmap "{bitmap}"
  size [ {size_x} {size_y} {1} ]
  pose [ {pose_0} {pose_1} {0} {0} ]
)\n"""

    start = None
    end = None
    for i, line in enumerate(lines):
        if line.strip() == "floorplan":
            start = i
        if start is not None and ')' in line:
            end = i
            break

    if start is not None and end is not None:
        lines[start:end+1] = [new_floorplan]

    with open(world_file_path, 'w') as file:
        file.writelines(lines)

yaml_data = read_yaml(home_path+'/dr_files/maps/latest_maps/amcl/amcl_map.yaml')
image_size = get_image_size(home_path + "/catkin_ws/install_isolated/share/agv_files/simulate/maps_drawn/from_hlc.png")  # Replace with your image path

size_x = image_size[0]*0.05
size_y = image_size[1]*0.05



# Assuming your yaml file has the field 'pose'
map_pose = yaml_data['origin']

pose_0 = map_pose[0] + (size_x/2)
pose_1 = map_pose[1] + (size_y/2)

write_world_file(size_x,size_y,pose_0, pose_1)
print(size_x,size_y,pose_0, pose_1)