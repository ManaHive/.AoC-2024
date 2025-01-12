import time
import numpy as np

# turning the strings into list of chars in order to make 2D arrays
DAY = 5
# with open(f'day{DAY}/page_order.txt') as i:
#     input_nl = i.readlines()
# page_order = np.array([l.strip('\n\r') for l in input_nl])
# with open(f'day{DAY}/pages.txt') as i:
#     test_nl = i.readlines()
# pages = np.array([l.strip('\n\r') for l in test_nl])

with open(f'day{DAY}/test_page_order.txt') as i:
    input_nl = i.readlines()
page_order = np.array([l.strip('\n\r') for l in input_nl])
with open(f'day{DAY}/test_page.txt') as i:
    test_nl = i.readlines()
pages = np.array([l.strip('\n\r') for l in test_nl])

start_time = time.time()
#----------------------------------------
# PART 1:
lst_pg_idx = []
lst_pg_order = []
# converting the page orders into list of lists, praying this is easier to work with
for l in np.nditer(page_order):
    order_lst = str(l).split("|")
    if order_lst[0] not in lst_pg_idx:
        lst_pg_idx.append(order_lst[0])
        lst_pg_order.append([order_lst[0],order_lst[1]])
    else:
        lst_pg_order[lst_pg_idx.index(order_lst[0])].append(order_lst[1])
max_length = max(len(sublist) for sublist in lst_pg_order)
lst_pg_order = np.array([sublist + [-1] * (max_length - len(sublist)) for sublist in lst_pg_order])

successFlag = True
for l in np.nditer(pages):
    pg_lst = str(l).split(",")
    for idx, n in np.ndenumerate(pg_lst):
        find = np.where(lst_pg_order == n)
        # clean_result = [(int(row), int(col)) for row, col in zip(find[0], find[1])]
        # print(f"{n} found at {clean_result}")
        for f in find:
            # just check for violations due to checking behind
            if f[1] != 0:
                if lst_pg_order[f[0]][0] == n:
                    successFlag = False
                    break
                else:
                    successFlag = True


            






print(f"Execution time: {time.time() - start_time} seconds")