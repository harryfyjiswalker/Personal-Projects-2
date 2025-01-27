def distinct_numbers(list1):
    no_dup = set(list1)
    return sorted(no_dup)


if __name__ == "__main__":
    list1 = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(list1))


#model soln:
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
 
    results.sort()
    return results
