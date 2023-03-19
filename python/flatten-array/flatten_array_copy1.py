    
# def flatten_1(iterable: list) -> list:
#     flat_list: list = []
#     if isinstance(iterable, list):
#         for item in flatten(iterable):
#             flat_list.append(item)
#     else:
#         flat_list.append(iterable)
    
# #     return flat_list

# def flatten_2(iterable: list) -> list:
#     flat_list: list = []
    
#     def recur_flat(coll):
#         if isinstance(coll, list):
#             for item in coll:
#                 recur_flat(item)
#         elif coll != None:
#             #return coll
#             flat_list.append(coll)
#     #flat_list.append(recur_flat(iterable))
#     recur_flat(iterable)
    
#     return flat_list

def flatten_answ(ary):
    flattr = [ ]
    for item in ary:
        if type(item) is list:
            # recursively add the list items
            for flat in flatten(item):
                flattr.append(flat)
        elif type(item) is int or type(item) is str:
            # add the item as is
            flattr.append(item)
    return flattr

def flatten(iterable: list) -> list:
    flat_list: list = []
    
    def recur_flat(coll):
        if isinstance(coll, list):
            for item in coll:
                recur_flat(item)
        elif coll != None:
            flat_list.append(coll)
	    
    recur_flat(iterable)
	    
    return flat_list

"""
if elem[i] is list
  ret + func(elem[i])
else
 ret << elem[i]
 
 """