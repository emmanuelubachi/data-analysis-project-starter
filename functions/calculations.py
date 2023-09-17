class Calculations:
    """
    A class that performs calculations on a DataFrame.
    """

    def __init__(self, data):
        """
        Initialize the Calculations object.

        Parameters:
        - data (pandas.DataFrame): The DataFrame on which calculations will be performed.
        """
        self.data = data

    def add_new_columns(
        self,
        value_column: str,
        column1: str,
        column2: str,
        new_column1: str,
        new_column2: str,
    ):
        """
        Add new columns to the DataFrame based on specific calculations.

        Args:
        - value_column (str): Name of the column containing the value.
        - column1 (str): Name of the first multiplying column.
        - column2 (str): Name of the second multiplying column.
        - new_column1 (str): Name of the new column corresponding to column1 calculations.
        - new_column2 (str): Name of the new column corresponding to column2 calculations.

        Returns:
        - pd.DataFrame: The modified DataFrame with the new columns.

        Example:
        >>> data = {'FOB': [155, 200, 350, 400, 570], 'CO': ['0', '1', '0.2', '0.6', '0'], 'CU': ['1', '0', '0.7', '0', '0.6']}
        >>> df = pd.DataFrame(data)
        >>> modified_df = add_new_columns(df, 'FOB', 'CO', 'CU', 'new_CO', 'new_CU')
        >>> print(modified_df)
        FOB   CO   CU  new_CO  new_CU
        0  155    0    1     0.0   155.0
        1  200    1     0   200.0     0.0
        2  350  0.2  0.7   115.5   201.5
        3  400  0.6    0   400.0     0.0
        4  570    0  0.6     0.0   570.0
        """
        new_CO = []
        new_CU = []

        for i in range(len(self.data)):
            value = self.data[value_column][i]
            CO = float(self.data[column1][i])
            CU = float(self.data[column2][i])

            if CO == 1:
                new_CO.append(value)
                new_CU.append(0)
            elif CU == 1:
                new_CO.append(0)
                new_CU.append(value)
            elif 0 < CO < 1 and CU == 0:
                new_CO.append(value)
                new_CU.append(0)
            elif 0 < CO < 1 and 0 < CU < 1:
                total = CO + CU
                new_CO.append((CO / total) * value)
                new_CU.append((CU / total) * value)
            elif CO == 0 and 0 < CU < 1:
                new_CO.append(0)
                new_CU.append(value)

        # Check for length mismatch
        if len(new_CO) != len(self.data) or len(new_CU) != len(self.data):
            raise ValueError(
                "Length of the new columns does not match the length of the DataFrame."
            )

        self.data[new_column1] = new_CO
        self.data[new_column2] = new_CU

        return self.data
