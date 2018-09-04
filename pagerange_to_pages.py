#Function transforms list with numbers and ranges to singular list with numbers
def ranges_to_numbers(page_ranges):
    true_page_numbers = []
    for value in page_ranges:
        if isinstance(value, list):
            for page in range(value[0], value[1]+1):
                true_page_numbers.append(page-1)
        else:
            true_page_numbers.append(value-1)

    return true_page_numbers
