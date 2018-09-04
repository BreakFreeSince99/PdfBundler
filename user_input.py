import os
from collections import OrderedDict
books_pages_dict = OrderedDict()
art_bun = []

'''
1. Add bookname.pdf to bundler folder
2. Specify booknames and associated pages into books_and_pages
3. Specify with True or False if book cover(s) should be included in bundle
'''

#Format of books_pages_dict is - books_pages_dict['bookname.pdf'] = [pages] 
#Format of [pages] is - [pagenumber, [pagerange_firstpage, pagerange_lastpage], pagenumber] - ad infinitum
books_pages_dict['Quick.pdf'] = [[41, 55], [201, 219], [234, 246]]
books_pages_dict['McRae.pdf'] = [[247, 249], [269, 271], [272, 273], 
[275, 282], [284, 288], 290, 294, [296, 299]]
books_pages_dict['Kumar.pdf'] = [0]

art_bun.append('genga2017.pdf')
art_bun.append('lameire2005.pdf')

output_folder_dest = None
folder_index = 1

def set_path():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    main_folder = 'Reading Material'
    new_folder = 'Week ' + str(folder_index)
    path = os.path.join(current_folder, main_folder, new_folder)
    return path

while True:
    if not os.path.exists(set_path()):
        os.makedirs(set_path())
        os.makedirs(os.path.join(set_path(), 'Bundles'))
        output_folder_dest = (set_path())
    else:
        folder_index += 1
        continue
    break

#Format of book_cover_included is - True or False 
book_cover_included = True