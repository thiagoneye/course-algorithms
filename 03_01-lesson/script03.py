"""
Merge Sort
"""

# Classes

class Notebook:
    def __init__(self, title, username, likes):
        self.title = title
        self.username = username
        self.likes = likes

    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)


# Functions

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'

def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'

def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare),
                 merge_sort(objs[mid:], compare),
                 compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

# Main

if __name__ == '__main__':
    # Create Notebooks
    nb0 = Notebook('pytorch-basics', 'aakashns', 373)
    nb1 = Notebook('linear-regression', 'siddhant', 532)
    nb2 = Notebook('logistic-regression', 'vikas', 31)
    nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
    nb4 = Notebook('cifar10-cnn', 'biraj', 2)
    nb5 = Notebook('cifar10-resnet', 'tanya', 29)
    nb6 = Notebook('anime-gans', 'hemanth', 80)
    nb7 = Notebook('python-fundamentals', 'vishal', 136)
    nb8 = Notebook('python-functions', 'aakashns', 74)
    nb9 = Notebook('python-numpy', 'siddhant', 92)

    notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]
    print(notebooks)

    # Sort
    sorted_notebooks = merge_sort(notebooks, compare_likes)
    print(sorted_notebooks)
