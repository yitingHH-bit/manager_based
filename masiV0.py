"""Configuration for the MASI excavator robot."""

from __future__ import annotations

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets import ArticulationCfg


##
# Configuration
##

MASI_CFG = ArticulationCfg(
    prim_path="/World/envs/env_.*/Robot",  # where to find the robot prim
    spawn=sim_utils.UsdFileCfg(
        usd_path="/home/jack/NA3/IsaacLab/IsaacSim_Models/Excavator_Model/model2.usd",
        copy_from_source=True,             # copy physical properties and joints from USD
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.09), # Z raised to match lower carriage height
        joint_pos={".*": 0.0},
        joint_vel={".*": 0.0},
    ),
    actuators={
        "main_joints": ImplicitActuatorCfg(
            joint_names_expr=["revolute_cabin", "revolute_lift", "revolute_tilt", "revolute_scoop"],

            stiffness={
                "revolute_cabin": 600.0,
                "revolute_lift": 600.0,
                "revolute_tilt": 600.0,
                "revolute_scoop": 600.0,
            },
            damping={
                "revolute_cabin": 40.0,
                "revolute_lift": 40.0,
                "revolute_tilt": 40.0,
                "revolute_scoop": 40.0,
            },

            velocity_limit={  # in sim deg/s, here rad/s haha
                "revolute_cabin": 10.0, # 1.7
                "revolute_lift": 10.0,
                "revolute_tilt": 10.0,
                "revolute_scoop": 10.0,
            },
            effort_limit={
                "revolute_cabin": 200.0,
                "revolute_lift": 500.0,
                "revolute_tilt": 500.0,
                "revolute_scoop": 500.0,
            },

            friction={
                "revolute_cabin": 0.0,
                "revolute_lift": 0.0,
                "revolute_tilt": 0.0,
                "revolute_scoop": 0.0,
            },

            armature={
                "revolute_cabin": 0.0,
                "revolute_lift": 0.0,
                "revolute_tilt": 0.0,
                "revolute_scoop": 0.0,
            },
        ),

        "tool": ImplicitActuatorCfg(
            joint_names_expr=["revolute_gripper", "revolute_claw_1", "revolute_claw_2"],

            stiffness={
                "revolute_gripper": 1500.0,
                "revolute_claw_1": 3000.0,
                "revolute_claw_2": 3000.0,

            },
            damping={
                "revolute_gripper": 80.0,
                "revolute_claw_1": 120.0,
                "revolute_claw_2": 120.0,

            },
            velocity_limit={
                "revolute_gripper": 3.0,
                "revolute_claw_1": 4.0,
                "revolute_claw_2": 4.0,

            },
            effort_limit={
                "revolute_gripper": 80.0,
                "revolute_claw_1": 250.0,
                "revolute_claw_2": 250.0,

            },
            friction={
                "revolute_gripper": 0.0,
                "revolute_claw_1": 0.0,
                "revolute_claw_2": 0.0,

            },
            armature={
                "revolute_gripper": 0.0,
                "revolute_claw_1": 0.0,
                "revolute_claw_2": 0.0,

            },
        ),
    },
)