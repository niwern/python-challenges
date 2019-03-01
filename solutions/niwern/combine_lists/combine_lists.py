def combine_lists(list1, list2):
    l1 = len(list1)
    l2 = len(list2)
    list = []

    for i in range(max(l1,l2)):
        if i < l1:
            list.append(list1[i])
        if i < l2:
            list.append(list2[i])

    return list