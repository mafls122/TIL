import math

# 최고 00:20.686 기록
def reward_function(params):
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    speed = params['speed']

    SPEED_THRESHOLD = 1.0
    DIRECTION_THRESHOLD = 10.0
    reward = 1.0

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)

    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5
    elif speed < SPEED_THRESHOLD:
        reward *= 0.5

    return float(reward)

