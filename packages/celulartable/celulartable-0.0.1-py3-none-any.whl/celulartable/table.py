from typing import Any, List, Tuple, Union

from .cell.cell import Cell
from .cell.cell_rows import create_rows_config
from .type_checking.cell_parsing import try_evey_type
from .type_checking.column_parsing import get_column_type_name
from .utils.constants import (
    ALIGNMENTS_PER_TYPE,
    AT_LEAST_THREE,
    DEFAULT_MISSING_VALUE, 
    SECOND_TO_ANTE_PENULT,
    AT_LEAST_ONE,
    AT_LEAST_TWO,
    AT_LEAST_FOUR,
    FIRST,
    PENULT,
    LAST,
    HEADER_I,
    CONTENT_I,
    HEADER_ROW,
    UPPER_ROW,
    MIDDLE_ROW,
    PENULT_ROW,
    LOWER_ROW,
)
from .utils.micro_classes import (
    Empty,
    VoidCell
)


class CelularTable:
    
    def __init__(self) -> None:
        self.headers = []
        self.rows = []
        self.column_count = 0
        self.row_count = 0
        self.show_headers = True
        self.cell_types = {}
        self.column_types = []
        self.column_alignments = []
        self.column_widths = []
        self.missing_value = DEFAULT_MISSING_VALUE
        self.no_border_cells: List[Tuple[int, int]] = []
        self.no_border_header_cells: List[int] = []
        self.__rows_config = create_rows_config()
        
    def __repr__(self) -> str:
        return self.craft()
        
    def __str__(self) -> str:
        return self.craft()        
        
    # (o==================================================================o)
    #   COLUMN GETTING SECTION (START)
    #   to get specific columns, or all of them
    # (o-----------------------------------------------------------\/-----o)

    # (o-----------------------------------------( PUBLIC INTERFACE ))
    
    def get_column(self, 
                   index: Union[int, Any],
                   missing_vals: bool=True
                  ) -> dict:
        """
        ## Get column
        
        Returns a dict with the following structure::
        
            {'header': Any, 'content': [Any]}
            
        If there's columns with no header, its index
        takes place of the said one.
            
        ### Params::
        
            index: int | Any    # Specify index or header of column.
            missing_vals: bool  # False: Uses "Empty" class.
                                # True: Uses self.missing_value
        """
        header = self.__validate_header_with_number(index)
        column_body = self.__validate_col_with_number(
            index,
            missing_vals,
        )
        if header is None and column_body is None:
            header = self.__validate_header_with_value(value=index)             
            column_body = self.__validate_col_with_value(value=index)
        
        column = {'header': header, 'content': column_body}
        
        return column
    
    def get_columns(self, 
                    range_to_get: range=None, 
                    missing_vals: bool=True
                   ) -> dict:
        """
        ## Get columns
        
        Returns a dict with the following structure::
        
            {Any: [Any], ...}
            
        ### Params::
        
            range_to_get: range     # Specify range of columns
            missing_vals: bool      # False: Uses "Empty" class.
                                    # True: Uses self.missing_value
        """
        columns = {}
        range_to_get = self.__validate_range_for_cols(range_to_get)
        for index in range_to_get:
            column = self.get_column(index, missing_vals)
            columns[column['header']] = column['content']

        return columns

    # (o-----------------------------------------( PRIVATE ))
    
    def __validate_range_for_cols(self, range_to_check: range):
        if range_to_check is None or range_to_check is not range:
            return range(0, self.column_count)
        return range_to_check
    
    def __validate_header_with_value(self, value: Any):
        header = None
        try:
            self.headers.index(value)
            header = value
        except ValueError:
            pass
        
        return header
    
    def __validate_col_with_value(self, value: Any, missing_vals: bool):
        column_body = None
        try:
            col_index = self.headers.index(value)
            column_body = list(map(
                lambda row: self.__get_cell(row, col_index, missing_vals), 
                self.rows
            ))
        except ValueError:
            pass
        
        return column_body
    
    def __validate_header_with_number(self, index: int):
        header = None
        try:
            header = self.headers[index]
        except TypeError:
            pass
        except IndexError:
            header = index
        
        return header
    
    def __validate_col_with_number(self, index: int, missing_vals: bool):
        column_body = None
        try:
            column_body = list(map(
                lambda row: self.__get_cell(row, index, missing_vals), 
                self.rows
            ))
        except (TypeError, IndexError):
            pass
        
        return column_body         
    
    def __get_cell(self, row: list, index: int, missing_vals: bool) -> list:
        try:
            return row[index]
        except IndexError:
            if missing_vals:
                return self.missing_value
            else:
                return Empty
    
    # (o-----------------------------------------------------------/\-----o)
    #   COLUMN GETTING SECTION (END)
    # (o==================================================================o)

    
    # (o==================================================================o)
    #   CELL ADDING SECTION (START)
    #   adding and processing of cells
    # (o-----------------------------------------------------------\/-----o)
    
    # (o-----------------------------------------( PUBLIC INTERFACE ))
    
    def add_cell(self, 
                 value = Empty,
                 row_i: int = None, 
                 column_i: int = None, 
                ) -> None:
        row_i = self.__validate_row_i(row_i)
        column_i = self.__validate_column_i(row_i, column_i)
        value = self.__validate_value(value, row_i, column_i)
        if value is not None:
            self.__add_value_to_row(value, row_i, column_i)
    
    def add_header_cell(self, 
                        header_i: int,
                        value = None,
                        column_i: int = None,
                       ) -> None:
        column_i = self.__validate_header_column_i(column_i)
        value = self.__validate_header_name(value, header_i)
        if value is not None:
            self.headers.insert(column_i, value)
        
    def add_row(self,
                data: list,
                row_i: int = None,
               ) -> None:
        for piece in data:
            self.add_cell(
                value=piece, 
                row_i=row_i
            )
            
    def add_headers(self, headers: list) -> None:
        for header_i, header in enumerate(headers):
            self.add_header_cell(header_i, header)
        
    # (o-----------------------------------------( PRIVATE ))
    
    def __validate_header_name(self, header: str, column_i: int) -> str:
        if header is VoidCell:
            self.no_border_header_cells.append(column_i)
            return
        if header in self.headers:
            count = self.headers.count(header) + 1
            return f'{header} {count}'
        return header
    
    def __validate_value(self, value, row_i: int, column_i: int):
        if value is VoidCell:
            self.no_border_cells.append((row_i, column_i))
            return 
        if value is Empty:
            return self.missing_value
        return value
      
    def __add_value_to_row(self,
                           value,
                           row_i: int,
                           column_i: int,
                          ) -> None:
        try:
            self.rows[row_i].insert(column_i, value)
        except IndexError:
            self.rows.append([])
            self.add_cell(
                value,
                row_i, 
                column_i, 
            )
    
    def __validate_row_i(self, row_i: int) -> int:
        if row_i is None:
            row_i = self.rows.__len__()
        if row_i + 1 > self.row_count:
            self.row_count = row_i + 1
        return row_i
            
    def __validate_column_i(self, row_i: int, column_i: int) -> int:
        if column_i is None:
            try:
                column_i = self.rows[row_i].__len__()
            except IndexError:
                column_i = 0
        if column_i + 1 > self.column_count:
            self.column_count = column_i + 1
        return column_i
    
    def __validate_header_column_i(self, column_i) -> int:
        if column_i is None:
            column_i = self.headers.__len__()
        if column_i + 1 > self.column_count:
            self.column_count = column_i + 1
        return column_i 
     
    # (o-----------------------------------------------------------/\-----o)
    #   CELL ADDING SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   DATA FORMATTING SECTION (START)
    #   width finding, type formatting & alignments
    # (o-----------------------------------------------------------\/-----o)
    
       
    def find_types(self):
        columns_to_parse = self.get_columns(missing_vals=False)
        list(map(
            self.__parse_one_column, 
            columns_to_parse.items()
        ))
        return self.column_types
        
    def find_column_alignments(self):
        alignments = list(map(
            lambda type_: ALIGNMENTS_PER_TYPE[type_],
            self.column_types
        ))
        self.column_alignments = alignments
        return alignments
    
    def find_column_widths(self) -> List[int]:
        widths = []
        columns = self.get_columns()
        for header, data in columns.items():
            header_width = 0
            if self.show_headers:
                header_width = self.__get_piece_width(header)
            col_width = max(list(map(
                self.__get_piece_width,
                data
            )))
            max_width = max([header_width, col_width])
            widths.append(max_width)
            
        self.column_widths = widths
        
        return widths
    
    def __parse_one_column(self, column: Tuple[str, list]):
        column_content = column[CONTENT_I]
        column_name = column[HEADER_I]
        parsed_column = list(map(try_evey_type, column_content))
        column_type = get_column_type_name(parsed_column)
        self.cell_types[column_name] = parsed_column
        self.column_types.append(column_type)
        return {
            'header': column_name,
            'cell_types': parsed_column,
            'column_type': column_type,
        }
            
    @staticmethod
    def __get_piece_width(piece: str) -> int:
        try:
            return piece.__len__()    
        except AttributeError:
            return str(piece).__len__()
    
    # (o-----------------------------------------------------------/\-----o)
    #   DATA FORMATTING SECTION (END)
    # (o==================================================================o)

    
    # (o==================================================================o)
    #   TABLE CRAFTING SECTION (START)
    #   processing of all the cells
    # (o-----------------------------------------------------------\/-----o)
    
    # (o-----------------------------------------( PUBLIC INTERFACE ))
    
    def craft(self):
        if self.headers.__len__() == 0:
            self.show_headers = False
        self.find_types()
        self.find_column_alignments()
        self.find_column_widths()
        all_rows = self.__create_all_rows(
            alignment=self.column_alignments,
            cols_widths=self.column_widths
        )
        headers = self.__create_row(
            **self.__rows_config[HEADER_ROW],
            value=self.headers,
            alignment=self.column_alignments,
            width=self.column_widths,
            show_lower_border=[False]*self.column_count
            
        )
        table = []
        if headers is not None:
            table += headers
        table += all_rows
        
        return '\n'.join(table)
        

    
    # (o-----------------------------------------( PRIVATE ))
    
    def __create_all_rows(self, alignment, cols_widths):
        rows = []
        
        # UPPER ROW
        try:
            self.rows[AT_LEAST_TWO]
            rows.append('\n'.join(self.__create_row(
                **self.__rows_config[UPPER_ROW],
                value=self.rows[FIRST],
                alignment=alignment,
                width=cols_widths,
                # show_upper_border=show_upper_border,
                )))
        except IndexError:
            pass
        
        # MIDDLE ROWS
        try:
            # At least four rows needed
            self.rows[AT_LEAST_FOUR]
            for mid_row in self.rows[SECOND_TO_ANTE_PENULT]:
                rows.append('\n'.join(self.__create_row(
                    **self.__rows_config[MIDDLE_ROW],
                    value=mid_row,
                    alignment=alignment,
                    width=cols_widths
                )))
        except IndexError:
            pass
        
        # PENULT ROW
        try:
            self.rows[AT_LEAST_THREE]
            rows.append('\n'.join(self.__create_row(
                **self.__rows_config[PENULT_ROW],
                value=self.rows[PENULT],
                alignment=alignment,
                width=cols_widths
            )))
        except IndexError:
            try:
                self.rows[AT_LEAST_ONE]
                rows.append('\n'.join(self.__create_row(
                    **self.__rows_config[PENULT_ROW],
                    value=self.rows[LAST],
                    alignment=alignment,
                    width=cols_widths
                )))
            except IndexError:
                pass
        
        # LOWER ROW
        try:
            self.rows[AT_LEAST_THREE]
            rows.append('\n'.join(self.__create_row(
                **self.__rows_config[LOWER_ROW],
                value=self.rows[LAST],
                alignment=alignment,
                width=cols_widths
            )))
        except IndexError:
            pass
        
        return rows
            
    def __cell_row_config(self, 
                          cell_quantity: int,
                          left,
                          penult,
                          right,
                         ) -> list:
        row_config = []
        if cell_quantity == 1:
            row_config.append(penult)
        elif cell_quantity >= 2:
            left_to_ante_penult = cell_quantity - 2
            for _ in range(left_to_ante_penult):
                row_config.append(
                    left
                )
            row_config.append(penult)
            row_config.append(right)
        
        return row_config
    
    def __create_row(self, 
                     left_cell,
                     penult_cell,
                     right_cell,
                     row_height,
                     row_type: str,
                     **cells_parameters
                     ) -> List[str]:
        """
        Pass parameters to modify the cell of each value as a list
        of the same size as the values.
        
        Cell parameters::
            
            alignment
            value
            width
            left_width
            right_width
            up_width
            down_width
            up_left_corner_width
            up_right_corner_width
            down_left_corner_width
            down_right_corner_width
            align_sign_left_width
            align_sign_right_width
            align_sign_center_width
            bold_text
            show_upper_border
            show_left_border
            show_lower_border
            show_right_border
            show_upper_align_sign
            show_lower_align_sign
            persistent_cell_size
            keep_upper_left_corner
            keep_upper_right_corner
            keep_lower_left_corner
            keep_lower_right_corner
        """
        try:
            quantity_of_values = cells_parameters['width'].__len__()
            cells_to_craft = cells_parameters['width']
        except KeyError:
            quantity_of_values = 0
            cells_to_craft = []
        row_config = self.__cell_row_config(
            cell_quantity=quantity_of_values,
            left=left_cell,
            penult=penult_cell,
            right=right_cell,
        )
        
        param_groups = self.__get_groups_of_parameters(
            cells_parameters,
            row_type
        )
        if param_groups is None:
            return None
        unjoined_cells = []
        for cell_config_i, _ in enumerate(cells_to_craft):
            cell_creator = row_config[cell_config_i]
            obj_cell: Cell = self.__create_cell(
                cell_creator=cell_creator,
                parameters=param_groups[cell_config_i]
            )
            cell_parts = obj_cell.craft()
            unjoined_cells.append(cell_parts)
            
        
        joined_cell_parts = []
        for part_i in range(row_height):
            joined_part = ''.join(list(
                map(
                    lambda cell: cell[part_i], 
                    unjoined_cells
                )
            ))
            joined_cell_parts.append(joined_part)
        

        return joined_cell_parts
    
    def __get_groups_of_parameters(self, 
                                   parameters: dict,
                                   row_type: str,
                                  ) -> List[dict]:
        if not self.show_headers and row_type is HEADER_ROW:
            return
        keys = list(parameters.keys())
        values = list(parameters.values())
        column_quantity = self.column_count
        
        param_groups = []
        [param_groups.append({}) for _ in range(column_quantity)]
        for key_i, key in enumerate(keys):
            for column_i in range(column_quantity):
                try:
                    param_groups[column_i][key] = values[key_i][column_i]
                except IndexError:
                    if row_type != HEADER_ROW:
                        param_groups[column_i]['value'] = self.missing_value
                
        return param_groups
        
    
    def __create_cell(self, cell_creator, parameters: dict) -> Cell:
        return cell_creator(parameters)
    
    # (o-----------------------------------------------------------/\-----o)
    #   TABLE CRAFTING SECTION (END)
    # (o==================================================================o)
    


    

        
        
    
