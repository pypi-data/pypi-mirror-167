from .dict_printer import pretty_print_dict
from .list_printer import (
    list_as_fitted_table_string,
    pretty_print_list,
    pretty_print_sym_double_list,
)
from .percentage import progress_printer, main_and_sub_progress_printer

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from . import _version
__version__ = _version.get_versions()['version']
