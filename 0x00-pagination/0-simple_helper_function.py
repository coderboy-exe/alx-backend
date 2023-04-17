#!usr/bin/env python3
""" Module definition """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        given 'page' and 'page_size', returns the start index and end index
        coreesponding to the range of indexes to return in a list for those
        particular pagination
    """
    start_idx = ((page - 1) * page_size)
    return (start_idx, start_idx + page_size)
    
