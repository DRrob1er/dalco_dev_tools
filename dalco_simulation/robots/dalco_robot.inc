define laser ranger
(
  sensor
  (
    range [ 0.0  14.0 ]
    fov 360.0
    samples 1200
  )
  # generic model properties
  color "black"
  size [ 0.06 0.15 0.03 ]
)

#
# Robot model:
# footprint (counter-clockwise): [-0.1,-0.125], [0.5,-0.125], [0.5,0.125], [-0.1,0.125]
# center of rotation: [0,0]
# wheelbase: 0.44

define carlike_robot position
(
  pose [ 0.0 0.0 0.0 0.0 ]

  odom_error [0.01 0.01 999999 999999 999999 0.001]

  size [ 0.75 0.45 2.00 ] # this models the footprint (rectangular), but shifted such that the bottom-left corner is in [0,0]. The center of rotation now here at [0.3, 0.125, 0.2]
  # correct center of rotation:
  origin [ 0.16 0.0 0.0 0.0]
  gui_nose 1
  color "red"

  # kinematics
  drive "car"
  wheelbase 0.44 # distance between both axles

  # spawn sensors
  laser(pose [ -0.1 0.0 -1.5 0.0 ])
)

#define myobstacle position
#(
#  localization "gps"
#  size [ 0.25 0.25 0.40 ]
#  gui_nose 1
#  drive "omni"
#  color "blue"
#)
