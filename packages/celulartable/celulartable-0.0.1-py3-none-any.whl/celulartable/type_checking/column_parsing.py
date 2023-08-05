from typing import List, Set

from ..utils.constants import (
    TYPE_NAMES,
    COLUMN_TYPES
)


# Type hierarchy for this package
#   None
#   bool
#   int
#   float | exponential
#   str
#   (Any other)


__fast_check = { True: None }


def __check_column_type(reduced_column_set: Set[str],
                        admitted_types: List[str]
                       ) -> bool:
    return reduced_column_set.issubset(admitted_types)


def get_column_type_name(column: List[str]) -> str:
    reduced = set(column)
    
    try:
        is_none = __check_column_type(reduced, COLUMN_TYPES.none_)
        __fast_check[is_none]
        return TYPE_NAMES.none_type_
    except KeyError:
        pass
    try:
        is_bool = __check_column_type(reduced, COLUMN_TYPES.bool_)
        __fast_check[is_bool]
        return TYPE_NAMES.bool_
    except KeyError:
        pass
    try:
        is_int = __check_column_type(reduced, COLUMN_TYPES.int_)
        __fast_check[is_int]
        return TYPE_NAMES.int_
    except KeyError:
        pass
    try:
        is_float = __check_column_type(reduced, COLUMN_TYPES.float_)
        __fast_check[is_float]
        return TYPE_NAMES.float_
    except KeyError:
        pass
    # try:
    #     __fast_check[is_exponential]
    #     return TYPE_NAMES.exponential
    # except KeyError:
    #     pass
    
    return TYPE_NAMES.str_