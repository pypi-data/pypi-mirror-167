"""
|  Wrapper for pyreadstat to easily read, create and adjust .sav files.
|
|  **Requirements:**
|       `pyreadstat 1.1.6 <https://ofajardo.github.io/pyreadstat_documentation/_build/html/index.html>`_
|       pandas
"""

import pyreadstat as prs
import pandas as pd

class Meta:
    """
    Wrapper for pyreadstat to easily read, create and adjust .sav files.

    :param path: path to an SPSS file. The DataFrame and metadata object will be constructed from this file, if provided.
    :type path: str, optional
    :param df: pandas DataFrame. The DataFrame will be used to construct the metadata, if only a DataFrame is provided
    :type df: DataFrame, optional
    :param meta: pyreadstat metadata object from SPSS file
    :type meta: object, optional
    :example (from path):
        >>> M = Meta(path="path_to_file.sav")
        >>> print(M.names)
        ['list', 'of', 'column', 'names']

    :example (df only):
        >>> df = pd.DataFrame({'col1': [1,2,3], 'col2': ['hi','hi','hi']})
        >>> M = Meta(df=df)
        >>> print(M.types['col2])
        A2

    :example (df + meta):
        >>> M = Meta(df=df, meta=meta)
        >>> print(M.names)
        ['list', 'of', 'column', 'names']

    """
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self._build()

    
    def _build(self):
        """
        Building class instance from file, pandas DataFrame, or both a DataFrame and metadata object
        """
        # Read from file
        if 'path' in list(self.kwargs.keys()):
            try:
                self.df, self.meta = prs.read_sav(self.kwargs['path'])
                self._get()
            except Exception as e:
                raise FileNotFoundError(f"meta cannot load file from path. prs: {e}")
        elif 'df' in list(self.kwargs.keys()):
            # Read from dataframe
            if isinstance(self.kwargs['df'], pd.DataFrame) and not self.kwargs['df'].empty and not 'meta' in list(self.kwargs.keys()):
                self.df = self.kwargs['df']
                self._set()
            # Read from dataframe + metadata
            elif isinstance(self.kwargs['df'], pd.DataFrame) and not self.kwargs['df'].empty and 'meta' in list(self.kwargs.keys()):
                self.df = self.kwargs['df']
                self.meta = self.kwargs['meta']
                self._get()
        else:
            raise ValueError("unable to make an instance of class Meta with the given parameters")

    
    def _get(self):
        """ 
        Get metadata from class parameter
        """
        self.names = self.meta.column_names
        self.labels = self.meta.column_names_to_labels
        self.value_labels = self.meta.variable_value_labels
        self.types = self._fix_empty_cols(self.meta.original_variable_types, self.value_labels)
        self.measures = self.meta.variable_measure
        self.missing = self.meta.missing_ranges


    def _set(self): 
        """
        Build metadata from DataFrame
        """ 
        self.names = []
        self.labels = {}
        self.value_labels = {}
        self.types = {}
        self.measures = {}
        self.missing = {}
        for col in self.df.columns:
            self.new(col)


    def _check_col(self, col_name: str):
        """
        Checks input type of col_name and whether the column exists
        :param col_name: column name
        """
        if not isinstance(col_name, str):
            raise TypeError(f"parameter 'col_name' should be a string, but the given object is of type {type(col_name)}")
        if not col_name in self.df.columns:
            raise KeyError(f"'{col_name}' does not exist in DataFrame")
        if col_name not in self.names:
            self.names.append(col_name)


    def _fix_empty_cols(self, original_variable_types: dict[str,str], variable_value_labels: dict, default='F1.0') -> list:
        """
        Patching an issue where empty columns of undefined type may result in an error when writing to file

        :param original_variable_types: variable types as defined by pyreadstat
        :param variable_value_labels: variable value labels as defined by pyreadstat
        :param default: datatype of empty columns, default = 'F1.0' (integer)
        :type default: str, optional
        """
        empty_cols = [col for col in self.names if self.df[col].isnull().all()]
        for col in empty_cols:
            if variable_value_labels[col] == {}:
                original_variable_types[col] = default
        return original_variable_types


    def add_column_label(self, col_name: str, col_label: str) -> None:
        """
        Adds column names to metadata

        :param col_name: column name
        :param col_label: column label
        :example:
            >>> M.add_column_label("my_column", "This is my column")
            >>> print(M.labels["my_column"])
            This is my column

        """
        self._check_col(col_name)
        if not isinstance(col_label, str):
            raise TypeError("col_label (param 2) should be a string")
        self.labels[col_name] = col_label


    def add_value_labels(self, col_name: str, val_label: dict[int, str]) -> None:
        """
        Adds a column's value labels to metadata

        :param col_name: column name
        :param val_label: values mapped to labels
        :example:
            >>> labels = {0: 'Not selected', 1: 'Selected'}
            >>> M.add_value_labels('my_column', labels)
            >>> print(M.value_labels['my_column'])
            {0: 'Not selected', 1: 'Selected'}

        """
        self._check_col(col_name)
        if not isinstance(val_label, dict):
            raise TypeError("val_lables (param 2) should be a dict")
        self.value_labels[col_name] = val_label


    def add_type(self, col_name: str, col_type: str='int', decimals: int=0) -> None:
        """
        Adds a column's type to metadata

        :param col_name: column name
        :param col_type: any of *str*, *int*, *float*. default = *int*
        :type col_type: str, optional
        :param decimals: the number of decimals that numeric values should display, default = 0
        :type decimals: int, optional
        :example:
            >>> M.df['my_column'] = [12.3311, 15.2224, 9.8832]          
            >>> M.add_type('my_column', 'float', decimals=3)
            >>> print(M.types['my_column'])
            F6.3

        """
        self._check_col(col_name)
        if not isinstance(col_type, str):
            raise TypeError("col_type should be defined as a string - e.g.: 'int'")
        if not isinstance(decimals, int):
            raise TypeError("decimals (param 3) should be an integer")

        max_width = max([len(a) for a in self.df[col_name].astype('str')])

        if col_type == 'str':
            self.types[col_name] = f'A{max_width}'

        elif col_type == 'int':
            if self.df[col_name].dtype == 'object':
                self.types[col_name] = f'A{max_width}'
            else:
                self.types[col_name] = f'F{max_width}.0'

        elif col_type == 'float':
            if decimals <= 1:
                dec = max([len(str(c).split('.')[-1]) for c in self.df[col_name]])
                self.types[col_name] = f'F{max_width}.{dec}'
            else:
                if max_width <= decimals:
                    raise ValueError(f"'decimals' ({decimals}) cannot be larger than the length of the LONGEST value ({max_width})")
                self.types[col_name] = f'F{max_width}.{decimals}'
        else:
            raise ValueError(f"{col_type} is not a valid argument. Use any of 'str', 'int', 'float'")


    def add_measures(self, col_name: str, measures: str) -> None:
        """
        Adds the 'measures' of a column to metadata

        :param col_name: column name
        :param measures: any of *nominal*, *ordinal*, *scale*
        :example:
            >>> M.add_measures('my_column', 'nominal')
            >>> print(M.measures['my_column'])
            nominal

        """
        self._check_col(col_name)
        if not isinstance(measures, str):
            raise TypeError("measures (param 2) should be a string")
        if measures.lower() in ["nominal", "ordinal", "scale"]:
            self.measures[col_name] = measures
        else:
            raise ValueError(f"'{measures}' is not a valid argument, use any of 'nominal', 'ordinal', 'scale'")


    def new(self, col_name: str, col_type: str='int') -> None:
        """ 
        Add a new column to the metadata
        
        :param col_name: column name
        :param col_type: any of *int*, *str*, *float*. default = *int*
        :type col_type: str, optional
        :example:
            >>> M.new('my_column')
            >>> M.types['my_column']
            F1.0
            >>> M.measures['my_column']
            nominal

        """
        self._check_col(col_name)   
        t = self.df[col_name].dtype
        self.add_column_label(col_name, col_name)
        if col_type == 'str' or self.df[col_name].dtype == 'object':
            self.add_type(col_name, 'str')
            self.add_measures(col_name, 'nominal')
        elif col_type == 'int' and str(self.df[col_name].dtype).startswith('int'):  
            self.add_type(col_name, 'int')
            if self.df[col_name].max() > 50:
                self.add_measures(col_name, 'scale')
            else:
                self.add_measures(col_name, 'nominal')
        elif col_type == 'float' or str(self.df[col_name].dtype).startswith('float'):
            self.add_type(col_name, 'float')
            self.add_measures(col_name, 'scale')


    def view(self, col_name: str):
        """
        Prints all of the metadata for a given column
        
        :param col_name: column name
        :example:
            >>> M.df['my_column] = [1,2,3]
            >>> M.new('my_column')
            >>> M.view('my_column)
            my_column
            type: numeric (F1.0)
            measure: nominal
            label: my_column
            value labels: undefined
            missing ranges: undefined

        """
        self._check_col(col_name)
        print(col_name)
        if not col_name in list(self.types.keys()):
            print('type: undefined')
        elif self.types[col_name].startswith('F'):
            print(f'type: numeric ({self.types[col_name]})')
        elif self.types[col_name].startswith('A'):
            print(f'type: string ({self.types[col_name]})')
        
        if not col_name in list(self.measures.keys()):
            print('measure: undefined')
        else:
            print(f'measure: {self.measures[col_name]}')

        if not col_name in list(self.labels.keys()):
            print('label: undefined')
        else:
            print(f'label: {self.labels[col_name]}')

        if not col_name in list(self.value_labels.keys()):
            print('value labels: undefined')
        else:
            print(f'value labels: {self.value_labels[col_name]}')

        if not col_name in list(self.missing.keys()):
            print('missing ranges: undefined')
        else:
            print(f'missing ranges: {self.missing[col_name]}') 


    def write_to_file(self, filename: str="output.sav") -> None:
        """
        Writes the DataFrame and metadata to an SPSS file

        :param filename: name of the new file
        :type filename: str, optional
        """
        if not isinstance(filename, str):
            raise TypeError("filename (param 1) should be a string")
        if not filename.endswith('.sav'):
            filename = filename + '.sav'
        prs.write_sav(self.df, 
                      filename, 
                      column_labels=self.labels,
                      variable_value_labels=self.value_labels,
                      missing_ranges=self.missing,
                      variable_measure=self.measures,
                      variable_format=self.types
                      )
        
        
