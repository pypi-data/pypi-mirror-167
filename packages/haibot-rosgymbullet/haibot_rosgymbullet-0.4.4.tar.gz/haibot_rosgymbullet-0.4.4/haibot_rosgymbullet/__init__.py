from gym.envs.registration import register
register(
    id='HaIBotEnv-v4.4', 
    entry_point='haibot_rosgymbullet.envs:DiffBotDrivingEnv'
)