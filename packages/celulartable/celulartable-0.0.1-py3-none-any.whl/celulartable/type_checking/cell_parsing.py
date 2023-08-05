from typing import Any, Tuple, Union

from ..utils.micro_classes import Empty

from .type_parsers import (
    is_none,
    is_bool,
    is_int,
    is_float,
    is_exponential,
)
from ..utils.constants import (
    TYPE_NAMES,
    TYPE_NAME_I,
    TYPE_PARSER_I,
)


__fast_check = { True: None }
__is_empty = {Empty: None}

__parse_groups = {
    TYPE_NAMES.none_type_: is_none,
    TYPE_NAMES.bool_: is_bool,
    TYPE_NAMES.int_: is_int,
    TYPE_NAMES.float_: is_float,
    TYPE_NAMES.exponential: is_exponential,
}


def try_evey_type(piece: Any):
    try:
        __is_empty[piece]
        return TYPE_NAMES.empty
    except KeyError:
        pass
    for parse_group in __parse_groups.items():
        match = __use_parse_group(parse_group, piece)
        try:
            __parse_groups[match]
            return match
        except KeyError:
            pass
    else:
        return TYPE_NAMES.str_
    

def __use_parse_group(parse_group: Tuple[str, 'function'],
                      piece: Any,
                     ) -> Union[str, None]:
    type_name = parse_group[TYPE_NAME_I]
    parser_function = parse_group[TYPE_PARSER_I]
    result: bool = parser_function(piece)
    try:
        __fast_check[result]  # If result is True
        return type_name
    except KeyError:
        return TYPE_NAMES.no_match  # If result is False
    


    
    