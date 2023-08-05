from gym.envs.registration import register
register(
    id='HaIBotEnv-v5.8', 
    entry_point='haibot_rosgymbullet.envs:DiffBotDrivingEnv'
)