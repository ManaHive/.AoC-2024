import time
import numpy as np

DAY = 5
with open(f'day{DAY}/page_order.txt') as i:
    input_nl = i.readlines()
page_order = np.array([l.strip('\n\r') for l in input_nl])
with open(f'day{DAY}/pages.txt') as i:
    test_nl = i.readlines()
pages = np.array([l.strip('\n\r') for l in test_nl])

# with open(f'day{DAY}/test_page_order.txt') as i:
#     input_nl = i.readlines()
# page_order = np.array([l.strip('\n\r') for l in input_nl])
# with open(f'day{DAY}/test_page.txt') as i:
#     test_nl = i.readlines()
# pages = np.array([l.strip('\n\r') for l in test_nl])

start_time = time.time()
#----------------------------------------
# PART 1:
lst_pg_idx = []
lst_pg_order = []
# converting the page orders into list of lists, praying this is easier to work with
for l in np.nditer(page_order):
    order_lst = str(l).split("|")
    order_lst[0] = int(order_lst[0])
    order_lst[1] = int(order_lst[1])
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
                    return pgo
    return -1

for l in pages:
    successFlag = True
    pg_lst = str(l).split(",")
    pg_lst_int = [int(pg) for pg in pg_lst]
    for idx, n in np.ndenumerate(pg_lst_int):
        if eval(pg_lst_int, n) != -1:
            successFlag = False
            break
    if successFlag:
        lst_success.append(pg_lst_int)
    else:
        lst_failure.append(pg_lst_int)

# PART 2: Rearrange numbers in the failed list such that they work, then take the middle numbers from these
fail_sum = 0
lst_corrected_failure = []
for fail in lst_failure:
    curr = [int(f) for f in fail]
    while(True):
        loopFlag = False
        for idx, n in np.ndenumerate(curr):
            eval_result = eval(curr, n)
            if eval_result != -1:
                loopFlag = True
                break
        if loopFlag:
            # strange issue with using curr.index directly causing an infinite loop, must use variables directly...
            n_idx = curr.index(n) 
            eval_idx = curr.index(eval_result)
            curr[eval_idx], curr[n_idx] = curr[n_idx], curr[eval_idx]
            continue
        else:
            #print(curr)
            lst_corrected_failure.append(curr)
            fail_sum += curr[len(curr) // 2]
            break
                
# test = []
# for l in lst_corrected_failure:
#     successFlag = True
#     for idx, n in np.ndenumerate(l):
#         if eval(l, n) != -1:
#             successFlag = False
#             break
#     if successFlag:
#         test.append(l)

# print(len(lst_failure))
# print(len(lst_corrected_failure))
# print(len(test))

# print(lst_success)
# print(lst_corrected_failure)
# grabbing the middle nums
sum = 0
for s in lst_success:
    sum += s[len(s) // 2]
print(f"Sum of middle nums (PART 1): {sum}")
print(f"Sum of middle nums for failed pages (PART 2): {fail_sum}")
print(f"Execution time: {time.time() - start_time} seconds")