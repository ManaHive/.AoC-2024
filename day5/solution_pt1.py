import time
import numpy as np

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

lst_success = []
lst_failure = []

def eval(pg_lst, n):
    find = np.where(lst_pg_order == n)
    clean_result = [(int(row), int(col)) for row, col in zip(find[0], find[1])]
    for f in clean_result:
        # just check for violations due to reversed order
        if f[1] == 0:
            # logic run through
            # l = current line (61,13,29)
            # n = current number of the page input (29)
            # find = list of indexes in page_order where n is found (29 found at (0,4)..(4,0))
            # run through find with for loop, find the row that starts with n [f[1] == 0]
            # if f[1] == 0, run through that row in lst_pg_order and compare with previous numbers in the line
            for pgo in lst_pg_order[f[0]]:
                previous_nums = pg_lst[:pg_lst.index(n)]
                if pgo in previous_nums:
                    #print(f"Moment of failure: l:{l} f:{f} n:{n} pgo:{pgo} previousnums: {previous_nums}")
                    return False
    return True

for l in pages:
    successFlag = True
    pg_lst = str(l).split(",")
    for idx, n in np.ndenumerate(pg_lst):
        if not eval(pg_lst, n):
            successFlag = False
            break
    if successFlag:
        lst_success.append(pg_lst)
    else:
        lst_failure.append(pg_lst)

print(lst_success)
# grabbing the middle nums
sum = 0
for s in lst_success:
    sum += int(s[len(s) // 2])
print(f"Sum of middle nums: {sum}")
print(f"Execution time: {time.time() - start_time} seconds")