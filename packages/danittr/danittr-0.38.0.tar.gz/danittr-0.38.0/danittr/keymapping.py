"""Facility for key mapping management."""

from pygame import locals as constants
from pygame.key import name as name_key


DEFAULT_KEYS_MAP = {
    "player_left": constants.K_a,
    "player_right": constants.K_d,
    "player_up": constants.K_w,
    "player_down": constants.K_s,
    "jump": constants.K_k,
    "fire_item": constants.K_j,
    "interact": constants.K_e,
    "advance_deny": constants.K_SPACE,
    "accept_prompt": constants.K_RETURN,
}

VALID_KEYS_MAP = {
    name_key(eval("constants." + item)): eval("constants." + item)
    for item in dir(constants)
    if item.startswith("K_")
    if not "ALT" in item
    if not "SHIFT" in item
    if not "CTRL" in item
    if not "LOCK" in item
    if item != "K_ESCAPE"
}
