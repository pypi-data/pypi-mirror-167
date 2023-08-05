
from typing import Dict, Tuple, List

from ..cell.cell_styles import (
    style_names,
    Style
)
from ..utils.constants import (
    ACCEPTED_WIDTHS,
    ALIGNMENTS,
    BOLD_WIDTH_NAME,
    CENTERED,
    DEFAULT_CELL_ALIGNMENT,
    DEFAULT_MISSING_VALUE,
    DEFAULT_STYLE_NAME,
    DEFAULT_BORDER_WIDTH,
    LEFT_ALIGNED,
    RIGHT_ALIGNED,
    THIN_WIDTH_NAME,
    TO_CENTER,
    TO_RIGHT_ALIGN
)

class Cell:
    
    def __init__(self) -> None:
        self.__style_name: str = DEFAULT_STYLE_NAME
        self.__value = DEFAULT_MISSING_VALUE
        self.__width: int = 0
        self.__border_width: Dict[str, bool] = {
            'left': DEFAULT_BORDER_WIDTH,
            'right': DEFAULT_BORDER_WIDTH,
            'up': DEFAULT_BORDER_WIDTH,
            'down': DEFAULT_BORDER_WIDTH,
            'up_left_corner': DEFAULT_BORDER_WIDTH,
            'up_right_corner': DEFAULT_BORDER_WIDTH,
            'down_left_corner': DEFAULT_BORDER_WIDTH,
            'down_right_corner': DEFAULT_BORDER_WIDTH,
            'align_sign_left': DEFAULT_BORDER_WIDTH,
            'align_sign_right': DEFAULT_BORDER_WIDTH,
            'align_sign_center': DEFAULT_BORDER_WIDTH,
        }
        self.__text_width: str = ''
        self.__text_color: str = ''
        self.__formatted_value: str = ''
        self.__value_line: str = ''
        self.__upper_border: str = ''
        self.__lower_border: str = ''
        self.__alignment: str = DEFAULT_CELL_ALIGNMENT
        self.__float_column_widths: Tuple[int, int, int] = []
        self.__show_upper_border = True
        self.__show_lower_border = True
        self.__show_left_border = True
        self.__show_right_border = True
        self.__show_upper_align_sign = False
        self.__show_lower_align_sign = False
        self.__persistent_cell_size = False
        self.__keep_upper_left_corner = False
        self.__keep_upper_right_corner = False
        self.__keep_lower_left_corner = False
        self.__keep_lower_right_corner = False
        
    def craft(self) -> List[str]:
        cell_parts = []
        
        self.__format_up_line()
        if self.__persistent_cell_size or self.__show_upper_border:
            cell_parts.append(self.__upper_border)
        self.__format_value()
        self.__format_value_line()
        cell_parts.append(self.__value_line)
        self.__format_down_line()
        if self.__persistent_cell_size or self.__show_lower_border:
            cell_parts.append(self.__lower_border)

        return cell_parts
        
    @staticmethod
    def __check_border_width(width_name) -> bool:
        try:
            return ACCEPTED_WIDTHS[width_name]
        except KeyError:
            return DEFAULT_BORDER_WIDTH
        
    @staticmethod
    def __empty_placeholder(value) -> str:
        return ' ' * value.__len__()
    
    @staticmethod
    def __empty_placeholder_no_value(width: int) -> str:
        return ' ' * width
    
    # (o==================================================================o)
    #   CELL PROPERTIES SECTION (START)
    # (o-----------------------------------------------------------\/-----o)
    
    # (o-----------------------------------------( PUBLIC ))
    
    @property
    def style(self) -> Style:
        return style_names[self.__style_name]

    @property
    def margin(self) -> int:
        return self.style.margin
    
    @property
    def alignment(self) -> str:
        """
        The way the value is padded.

        One of::
        
            'l', 'r', 'c', 'f', 'b'
        """ 
        return self.__alignment
    
    @property
    def value(self) -> str:
        return self.__value
    
    @property
    def width(self) -> int:
        return self.__width
    
    @property
    def left_width(self) -> str:
        return self.__get_border_width(
            'left'
        )
        
    @property
    def right_width(self) -> str:
        return self.__get_border_width(
            'right'
        )
        
    @property
    def up_width(self) -> str:
        return self.__get_border_width(
            'up'
        )
        
    @property
    def down_width(self) -> str:
        return self.__get_border_width(
            'down'
        )
        
    @property
    def up_left_corner_width(self) -> str:
        return self.__get_border_width(
            'up_left_corner'
        )
        
    @property
    def up_right_corner_width(self) -> str:
        return self.__get_border_width(
            'up_right_corner'
        )
        
    @property
    def down_left_corner_width(self) -> str:
        return self.__get_border_width(
            'down_left_corner'
        )
        
    @property
    def down_right_corner_width(self) -> str:
        return self.__get_border_width(
            'down_right_corner'
        )
        
    @property
    def align_sign_left_width(self) -> str:
        return self.__get_border_width(
            'align_sign_left'
        )
        
    @property
    def align_sign_right_width(self) -> str:
        return self.__get_border_width(
            'align_sign_right'
        )
        
    @property
    def align_sign_center_width(self) -> str:
        return self.__get_border_width(
            'align_sign_center'
        )
        
    @property
    def bold_text(self):
        return self.__text_width

    @property
    def float_widths(self):
        return self.__float_column_widths
    
    @property
    def show_upper_border(self) -> bool:
        return self.__show_upper_border
    
    @property
    def show_left_border(self) -> bool:
        return self.__show_left_border
    
    @property
    def show_lower_border(self) -> bool:
        return self.__show_lower_border
    
    @property
    def show_right_border(self) -> bool:
        return self.__show_right_border
    
    @property
    def show_upper_align_sign(self) -> bool:
        return self.__show_upper_align_sign
    
    @property
    def show_lower_align_sign(self) -> bool:
        return self.__show_lower_align_sign
    
    @property
    def persistent_cell_size(self) -> bool:
        return self.__persistent_cell_size
    
    @property
    def keep_upper_left_corner(self) -> bool:
        return self.__keep_upper_left_corner

    @property
    def keep_upper_right_corner(self) -> bool:
        return self.__keep_upper_right_corner

    @property
    def keep_lower_left_corner(self) -> bool:
        return self.__keep_lower_left_corner

    @property
    def keep_lower_right_corner(self) -> bool:
        return self.__keep_lower_right_corner

    # (o-----------------------------------------( PRIVATE ))
    
    @property
    def __middle_line_width(self):
        return self.__width + (self.margin * 2)
    
    
    # (o-----------------------------------------------------------/\-----o)
    #   CELL PROPERTIES SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   SETTERS SECTION (START)
    #   Setters for the Cell properties
    # (o-----------------------------------------------------------\/-----o)
    
    @alignment.setter
    def alignment(self, alignment) -> None:
        try:
            ALIGNMENTS[alignment]
            self.__alignment = alignment
        except KeyError:
            pass
    
    @value.setter
    def value(self, new_value):
        self.__value = str(new_value)
        
    @width.setter
    def width(self, new_width):
        try:
            self.__width = int(new_width)
        except ValueError:
            pass
    
    @left_width.setter    
    def left_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['left'] = width_to_set

    @right_width.setter        
    def right_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['right'] = width_to_set

    @up_width.setter        
    def up_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['up'] = width_to_set

    @down_width.setter        
    def down_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['down'] = width_to_set

    @up_left_corner_width.setter        
    def up_left_corner_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['up_left_corner'] = width_to_set

    @up_right_corner_width.setter        
    def up_right_corner_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['up_right_corner'] = width_to_set

    @down_left_corner_width.setter        
    def down_left_corner_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['down_left_corner'] = width_to_set

    @down_right_corner_width.setter        
    def down_right_corner_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['down_right_corner'] = width_to_set

    @align_sign_left_width.setter        
    def align_sign_left_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['align_sign_left'] = width_to_set

    @align_sign_right_width.setter        
    def align_sign_right_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['align_sign_right'] = width_to_set

    @align_sign_center_width.setter        
    def align_sign_center_width(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__border_width['align_sign_center'] = width_to_set

    @bold_text.setter
    def bold_text(self, new_width) -> str:
        width_to_set = self.__check_border_width(new_width)
        self.__text_width = width_to_set

    # @property
    # def float_widths(self):
    #     return self.__float_column_widths
    
    @show_upper_border.setter    
    def show_upper_border(self, value):
        self.__show_upper_border = bool(value)

    @show_left_border.setter        
    def show_left_border(self, value):
        self.__show_left_border = bool(value)

    @show_lower_border.setter        
    def show_lower_border(self, value):
        self.__show_lower_border = bool(value)

    @show_right_border.setter        
    def show_right_border(self, value):
        self.__show_right_border = bool(value)

    @show_upper_align_sign.setter        
    def show_upper_align_sign(self, value):
        self.__show_upper_align_sign = bool(value)

    @show_lower_align_sign.setter        
    def show_lower_align_sign(self, value):
        self.__show_lower_align_sign = bool(value)
    
    @persistent_cell_size.setter
    def persistent_cell_size(self, value):
        self.__persistent_cell_size = bool(value)
        
    @keep_upper_left_corner.setter
    def keep_upper_left_corner(self, value):
        self.__keep_upper_left_corner = bool(value)

    @keep_upper_right_corner.setter
    def keep_upper_right_corner(self, value):
        self.__keep_upper_right_corner = bool(value)

    @keep_lower_left_corner.setter
    def keep_lower_left_corner(self, value):
        self.__keep_lower_left_corner = bool(value)

    @keep_lower_right_corner.setter
    def keep_lower_right_corner(self, value):
        self.__keep_lower_right_corner = bool(value)
        
    
    # (o-----------------------------------------------------------/\-----o)
    #   SETTERS SECTION (END)
    # (o==================================================================o)
    
    
    def __format_value(self) -> None:
        margin = self.margin
        width = self.__width
        value = self.__value
        alignment = self.__check_alignment()
        self.__formatted_value =  (
            f'{"":{margin}}{value:{alignment}{width}}{"":{margin}}'
        )   
    
    def __format_value_line(self) -> None:
        parts = []
        
        left = self.__get_border_part(
            self.style.left,
            'left'
        )
        if self.__show_left_border:
            parts.append(left)
        else:
            if self.__persistent_cell_size:
                parts.append(
                    self.__empty_placeholder(left)
                )
        parts.append(self.__formatted_value)
        right = self.__get_border_part(
            self.style.right,
            'right'
        )
        if self.__show_right_border:
            parts.append(right)
        else:
            if self.__persistent_cell_size:
                parts.append(
                    self.__empty_placeholder(right)
                )
            
        self.__value_line = (
            ''.join(parts)
        )
        
    def __format_up_line(self) -> None:
        
        up = self.__get_border_part(
            self.style.up,
            'up'
        )
        if not self.__show_upper_border:
            up = self.__empty_placeholder(up)
        
        left_corner = self.__get_border_part(
            self.style.up_left_corner,
            'up_left_corner'
        )
        if not self.__keep_upper_left_corner:
            if not self.__show_left_border and not self.__show_upper_border:
                if self.__persistent_cell_size:
                    left_corner = self.__empty_placeholder(left_corner)
                else:
                    left_corner = ''
            elif not self.__show_left_border and self.__show_upper_border:
                if self.__persistent_cell_size:
                    left_corner = up
                else:
                    left_corner = ''
            elif self.__show_left_border and not self.__show_upper_border:
                if self.__persistent_cell_size:
                    left_corner = self.__get_border_part(
                        self.style.left,
                        'left'
                    )
                else:
                    left_corner = ''
        
        right_corner = self.__get_border_part(
            self.style.up_right_corner,
            'up_right_corner'
        )
        if not self.__keep_upper_right_corner:
            if not self.__show_right_border and not self.__show_upper_border:
                if self.__persistent_cell_size:
                    right_corner = self.__empty_placeholder(right_corner)
                else:
                    right_corner = ''
            elif not self.__show_right_border and self.__show_upper_border:
                if self.__persistent_cell_size:
                    right_corner = up
                else:
                    right_corner = ''
            elif self.__show_right_border and not self.__show_upper_border:
                if self.__persistent_cell_size:
                    right_corner = self.__get_border_part(
                        self.style.right,
                        'right'
                    )
                else:
                    right_corner = ''
            
        self.__upper_border = self.__format_mid_line(
            left=left_corner,
            middle=up,
            right=right_corner
        )
        
    def __format_down_line(self) -> None:
            
        down = self.__get_border_part(
            self.style.down,
            'down'
        )
        if not self.__show_lower_border:
            down = self.__empty_placeholder(down)
            
        left_corner = self.__get_border_part(
            self.style.down_left_corner,
            'down_left_corner'
        )
        if not self.keep_lower_left_corner:
            if not self.__show_left_border and not self.__show_lower_border:
                if self.__persistent_cell_size:
                    left_corner = self.__empty_placeholder(left_corner)
                else:
                    left_corner = ''
            elif not self.__show_left_border and self.__show_lower_border:
                if self.__persistent_cell_size:
                    left_corner = down
                else:
                    left_corner = ''
            elif self.__show_left_border and not self.__show_lower_border:
                if self.__persistent_cell_size:
                    left_corner = self.__get_border_part(
                        self.style.left,
                        'left'
                    )
                else:
                    left_corner = ''
            
        right_corner = self.__get_border_part(
            self.style.down_right_corner,
            'down_right_corner'
        )
        if not self.keep_lower_right_corner:
            if not self.__show_right_border and not self.__show_lower_border:
                if self.__persistent_cell_size:
                    right_corner = self.__empty_placeholder(right_corner)
                else:
                    right_corner = ''
            elif not self.__show_right_border and self.__show_lower_border:
                if self.__persistent_cell_size:
                    right_corner = down
                else:
                    right_corner = ''
            elif self.__show_right_border and not self.__show_lower_border:
                if self.__persistent_cell_size:
                    right_corner = self.__get_border_part(
                        self.style.right,
                        'right'
                    )
                else:
                    right_corner = ''
            
        self.__lower_border = self.__format_mid_line(
            left=left_corner,
            middle=down,
            right=right_corner
        )
    
    def __format_mid_line(self, left, middle, right) -> str:
        mid_width = self.__middle_line_width
        return f'{left}{middle*mid_width}{right}'
        
    def __get_border_part(self, part, part_name: str) -> str:
        width = self.__get_border_width(part_name)
        return part[width]
        
    def __get_border_width(self, part_name: str) -> str:
        if self.__border_width[part_name] is True:
            return BOLD_WIDTH_NAME
        else:
            return THIN_WIDTH_NAME
    
    def __check_alignment(self):
        if self.__alignment in TO_RIGHT_ALIGN:
            return RIGHT_ALIGNED
        elif self.__alignment in TO_CENTER:
            return CENTERED
        else:
            return LEFT_ALIGNED
    
    
    