#!/usr/bin/env python3
"""
pagination class
"""

import csv
import math
from typing import Dict, List


class Server:
    """
    pagination using given baby name file
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """the dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """calculate index range
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        hyper index
        """
        focus = []
        dataset = self.indexed_dataset()
        index = 0 if index is None else index
        keys = sorted(dataset.keys())
        assert index >= 0 and index <= keys[-1]
        [focus.append(i)
         for i in keys if i >= index and len(focus) <= page_size]
        data = [dataset[v] for v in focus[:-1]]
        next_index = focus[-1] if len(focus) - page_size == 1 else None
        return {'index': index, 'data': data,
                'page_size': len(data), 'next_index': next_index}
