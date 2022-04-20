test_list = [[(5,6), (17,8)], [(1,3),(16, 17)], [(0, 4), (10, 11)]]
print("The original list is : " + str(test_list))
temp=[ele for sub in test_list for ele in sub]
res=list(zip(*temp))
print("The converted tuple is:"+str(res)) 