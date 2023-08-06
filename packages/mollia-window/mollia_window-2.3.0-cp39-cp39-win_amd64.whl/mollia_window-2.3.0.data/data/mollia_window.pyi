from typing import Callable, Dict, List, Literal, Tuple, TypedDict

Key = Literal[
    'mouse1', 'mouse2', 'mouse3', 'tab', 'left_arrow', 'right_arrow', 'up_arrow', 'down_arrow', 'pageup', 'pagedown',
    'home', 'end', 'insert', 'delete', 'backspace', 'space', 'enter', 'escape', 'apostrophe', 'comma', 'minus',
    'period', 'slash', 'semicolon', 'equal', 'left_bracket', 'backslash', 'right_bracket', 'graveaccent', 'capslock',
    'scrolllock', 'numlock', 'printscreen', 'pause', 'keypad_0', 'keypad_1', 'keypad_2', 'keypad_3', 'keypad_4',
    'keypad_5', 'keypad_6', 'keypad_7', 'keypad_8', 'keypad_9', 'keypad_decimal', 'keypad_divide', 'keypad_multiply',
    'keypad_subtract', 'keypad_add', 'keypad_enter', 'left_shift', 'left_ctrl', 'left_alt', 'left_super',
    'right_shift', 'right_ctrl', 'right_alt', 'right_super', 'menu', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
]


class UI_Variable(TypedDict, total=False):
    type: Literal['int', 'float', 'str']
    value: int | float | str | bool
    min: int | float
    max: int | float
    options: List[str]


class UI_Console(TypedDict):
    open: bool
    lines: List[str]
    line: str


class UI_Item(TypedDict, total=False):
    type: Literal['text', 'button', 'checkbox', 'slider', 'drag', 'input', 'combo', 'image', 'header', 'tree', 'table', 'line', 'separator']
    content: List[UI_Item]
    open: bool
    text: str
    variable: str
    speed: float
    step: float
    format: str
    width: float
    height: float
    columns: int
    texture: str
    click: str


class UI_Sidebar(TypedDict):
    open: bool
    content: List[UI_Item]


class UI(TypedDict):
    callbacks: Dict[str, Callable]
    variables: Dict[str, UI_Variable]
    console: UI_Console
    sidebar: UI_Sidebar
    tooltip: str | None


class MainWindow:
    size: Tuple[int, int]
    ratio: float
    mouse: Tuple[int, int]
    mouse_wheel: int
    text: str
    ui: UI

    def key_pressed(self, key: Key) -> bool: ...
    def key_released(self, key: Key) -> bool: ...
    def key_down(self, key: Key) -> bool: ...
    def key_up(self, key: Key) -> bool: ...
    def update(self) -> None: ...
    def demo(self) -> None: ...


def main_window(size: Tuple[int, int] = (1800, 960), title: str = 'Mollia Window') -> MainWindow: ...
def update() -> None: ...


wnd: MainWindow
keys: Dict[str, int]
