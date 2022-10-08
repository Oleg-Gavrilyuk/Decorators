from logger import decorator
import os

nested_list2 = [
    [['a'], 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [[1, [2]], None],
]
path = os.path.abspath('logs.txt')

@decorator(path)
def hard_generator(main_list):
    for lists in main_list:
        if isinstance(lists, list):
            for lis in hard_generator(lists):
                yield lis
        else:
            yield lists


if __name__ == '__main__':
    for item in hard_generator(nested_list2):
        print(item)
