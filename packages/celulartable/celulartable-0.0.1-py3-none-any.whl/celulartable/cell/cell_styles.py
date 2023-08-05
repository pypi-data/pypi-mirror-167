
from typing import Dict, NamedTuple

# The composition of the style of a single cell
class Style(NamedTuple):
    left: Dict[str, str]
    right: Dict[str, str]
    up: Dict[str, str]
    down: Dict[str, str]
    up_left_corner: Dict[str, str]
    up_right_corner: Dict[str, str]
    down_left_corner: Dict[str, str]
    down_right_corner: Dict[str, str]
    align_sign_left: Dict[str, str]
    align_sign_right: Dict[str, str]
    align_sign_center: Dict[str, str]
    margin: int
    

# All the implemented styles
style_names = {
    'grid': Style(
        left={'thin': '|', 'bold': '‖'},
        right={'thin': '|', 'bold': '‖'},
        up={'thin': '-', 'bold': '='},
        down={'thin': '-', 'bold': '='},
        up_left_corner={'thin': '+', 'bold': '#'},
        up_right_corner={'thin': '+', 'bold': '#'},
        down_left_corner={'thin': '+', 'bold': '#'},
        down_right_corner={'thin': '+', 'bold': '#'},
        align_sign_left={'thin': '‹', 'bold': '«'},
        align_sign_right={'thin': '›', 'bold': '»'},
        align_sign_center={'thin': '~', 'bold': '≈'},
        margin=1,
    )
}