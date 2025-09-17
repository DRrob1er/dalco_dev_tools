#!/bin/bash

# Define the input and output file names
input_file="${HOME}/dr_files/maps/latest_maps/amcl/amcl_map.pgm"
output_file="${HOME}/catkin_ws/install_isolated/share/agv_files/simulate/maps_drawn/from_hlc.png"


# Use GIMP's batch mode to convert the file
gimp -i -b "(let* ((image (car (file-pnm-load RUN-NONINTERACTIVE \"$input_file\" \"$input_file\")))
                   (drawable (car (gimp-image-get-active-layer image))))
             (file-png-save RUN-NONINTERACTIVE image drawable \"$output_file\" \"$output_file\" 0 9 0 0 0 0 0)
             (gimp-image-delete image))"

# add one pixel border for STAGE
convert ${HOME}/catkin_ws/install_isolated/share/agv_files/simulate/maps_drawn/from_hlc.png -bordercolor Black -border 1 ${HOME}/catkin_ws/install_isolated/share/agv_files/simulate/maps_drawn/from_hlc.png