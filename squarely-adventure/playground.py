player_state = {}
current_player_switch_time, last_player_walk_switch_time, player_walk_switch_interval = 0, 0, 0

player_state["direction"]
player_state["is_player_walking"]
player_state["position"]
player_state["vertical_leg_position"]

if player_state["is_player_walking"]:
    if current_player_switch_time >= \
    last_player_walk_switch_time + player_walk_switch_interval:
        if player_state["position"] == "LEFT":
            if player_state["direction"] == "still":
                image_path = "images/blu-guy/left.png"
                player_state["direction"] = "moving"
            elif player_state["direction"] == "moving":
                image_path = "images/blu-guy/left-walk.png"
                player_state["direction"] = "still"
        elif player_state["position"] == "RIGHT":
            if player_state["direction"] == "still":
                image_path = "images/blu-guy/right.png"
                player_state["direction"] = "moving"
            elif player_state["direction"] == "moving":
                image_path = "images/blu-guy/right-walk.png"
                player_state["direction"] = "still"
        elif player_state["position"] == "UP":
            if player_state["direction"] == "still":
                image_path = "images/blu-guy/up.png"
                player_state["direction"] = "moving"
            elif player_state["direction"] == "moving":
               if player_state["vertical_leg_position"] == "left":
                   image_path = "images/blu-guy/up-walk-left.png"
                   player_state["direction"] = "still"
                   player_state["vertical_leg_position"] = "right"
               elif player_state["vertical_leg_position"] == "right":
                   image_path = "images/blu-guy/up-walk-right.png"
                   player_state["direction"] = "still"
                   player_state["vertical_leg_position"] = "left"
        elif player_state["position"] == "DOWN":
            if player_state["direction"] == "still":
                image_path = "images/blu-guy/down.png"
                player_state["direction"] = "moving"
            elif player_state["direction"] == "moving":
               if player_state["vertical_leg_position"] == "left":
                   image_path = "images/blu-guy/down-walk-left.png"
                   player_state["direction"] = "still"
                   player_state["vertical_leg_position"] = "right"
               elif player_state["vertical_leg_position"] == "right":
                   image_path = "images/blu-guy/down-walk-right.png"
                   player_state["direction"] = "still"
                   player_state["vertical_leg_position"] = "left"

        last_player_walk_switch_time = current_player_switch_time
else:
    if player_state["position"] == "LEFT":
        image_path = "images/blu-guy/left.png"
    elif player_state["position"] == "UP":
        image_path = "images/blu-guy/up.png"
    elif player_state["position"] == "RIGHT":
        image_path = "images/blu-guy/right.png"
    elif player_state["position"] == "DOWN":
        image_path = "images/blu-guy/down.png"
