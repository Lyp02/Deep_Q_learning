import gym
from wrapper_gym import KFrames
from deepq import train_deepq
from neural_nets import CNN
from utils import preprocess

AGENT_HISTORY_LENGTH = 4
NB_ACTIONS = 4
env = gym.make("BreakoutNoFrameskip-v4")
env = KFrames(env, AGENT_HISTORY_LENGTH)
Q_network = CNN(AGENT_HISTORY_LENGTH, NB_ACTIONS)

train_deepq(
    env=env,
    nb_actions=NB_ACTIONS,
    Q_network=Q_network,
    preprocess_fn=preprocess,
    demo_tensorboard=True,
    )