# manager_based

Heres the direct env I did on Friday. This uses the "model2.usd" from Github.

Drop these files to:
...\IsaacLab\5.0.0\IsaacLab\source\isaaclab_tasks\isaaclab_tasks\direct\masi

run with (windows):
isaaclab.bat -p scripts/reinforcement_learning/rl_games/train.py --task=Isaac-Masi-v0 --num_envs 512


for linux just use ./isaaclab.sh -p

[14:15, 12/21/2025] Eetu: Also, to be safe I increased the MASIV2_CFG joint effort limits to 1000 for the main joints and 50 for the gripper. Im not sure if this is necessary though
[14:19, 12/21/2025] Eetu: I also have this feeling that you need to add one import line somwhere, at least that had to be done with older IsaacLab-version. Can't find that atm...

But message me if the rl_games command cannot find the task, that means that the import is missing!
