from collections import OrderedDict
books_pages_dict = OrderedDict()
add_to_bundle = []

'''
1. Add bookname.pdf to bundler folder
2. Specify booknames and associated pages into books_and_pages
3. Specify output name of your new bundle 
4. Specify with True or False if book cover(s) should be included in bundle
'''

#Format of books_pages_dict is - books_pages_dict['bookname.pdf'] = [pages] 
#Format of [pages] is - [pagenumber, [pagerange_firstpage, pagerange_lastpage], pagenumber] - ad infinitum
#books_pages_dict['Quick.pdf'] = [[41, 55], [201, 219], [234, 246]]
#books_pages_dict['McRae.pdf'] = [[247, 249], [269, 271], [272, 273], 
#[275, 282], [284, 288], 290, 294, [296, 299]]
books_pages_dict['Kumar.pdf'] = [133, 134]

add_to_bundle.append('genga2017.pdf')
add_to_bundle.append('lameire2005.pdf')

#Format of output_bundle_name is - 'Your_Bundle.pdf'
output_bundle_name = 'My_Bundle.pdf'

#Format of book_cover_included is - True or False 
book_cover_included = True