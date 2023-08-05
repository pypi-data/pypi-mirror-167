# pyimpspec is licensed under the GPLv3 or later (https://www.gnu.org/licenses/gpl-3.0.html).
# Copyright 2022 pyimpspec developers
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# The licenses of pyimpspec's dependencies and/or sources of portions of code are included in
# the LICENSES folder.

from os.path import exists
from pyimpspec.data.data_set import (
    DataSet,
    dataframe_to_dataset,
)
from pandas import (
    DataFrame,
    read_csv,
)


def parse_csv(path: str, **kwargs) -> DataSet:
    """
    Parse a file containing data as character-separated values.

    Parameters
    ----------
    path: str
        The path to the file to process.

    Returns
    -------
    DataSet
    """
    assert type(path) is str and exists(path)
    df: DataFrame = read_csv(path, engine="python", **kwargs)
    return dataframe_to_dataset(df, path=path)
