# User Manual of Noor

## Interfacing with Noor 
1- Install NoMachine.
2- Connect to WIFI (USERNAME: TP-Link_4C6b , PASSWORD: 50441284)
3- In NoMachine, Enter USERNAME: jestson , password: 2020


# First turn on Master (start functionalities of Noor)
$roslaunch nourrobot bringup.launch

# Second runing stt node  to start detecting voice
$rosrun openai_chat stt_node.py

# start the tts node to convert text to speach to run the chat gpt output 
$rosrun openai_chat tts_node.py


# start  open ai node to convert the text to text through chat gpt 
1-To run this node you should run it from a ROS noetic not ROS melodic (Note: requires python3)

2-Make sure to run the following commands before running the node
$export ROS_IP=192.168.0.147 (change this to your IP)
$export ROS_HOSTNAME=192.168.0.147 (change this to your IP)
$export ROS_MASTER_URI=http://192.168.0.193:11311
 
3-run openAi Node
$python3 openAiNode.py

# Note
to change the language you can change the var lang input on those files stt.py, tts.py and openai.py (from en to the desired language)
