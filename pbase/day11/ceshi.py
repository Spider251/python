L = [{'name':'zs','age':15,'score':50},{'name':'ls','age':16,'score':555}]
def get_score(x):
    return x['score']
# def student_score5(L): 
#     for x in L:
#         sorted(L,key=get_score)
#     return L
# print(student_score5(L))
def student_score5(L): 
    for x in L:
        sorted(L,key=get_score,reverse=True)
    return L
print(student_score5(L))


