#!/usr/bin/env python3
""" Module definition """

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        given 'page' and 'page_size', returns the start index and end index
        coreesponding to the range of indexes to return in a list for those
        particular pagination
    """
    start_idx = ((page - 1) * page_size)
    return (start_idx, start_idx + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Gets data from a page

            Args:
                page: int && > 0
                page_size: int && > 0
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page > 0

        idx = index_range(page, page_size)
        dataset = self.dataset()
        if idx[0] >= len(dataset):
            return []
        return dataset[idx[0]:idx[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
            returns a dictionary of key-value pairs
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': page + 1 if page + 1 <= total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages,
                }
