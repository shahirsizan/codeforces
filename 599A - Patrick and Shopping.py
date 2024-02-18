a, b, c= list( map(int,input().split()) )
total_dist_1 = a + a + b + b
total_dist_2 = a + c + b
total_dist_3 = a + c + c + a
total_dist_4 = b + c + c + b
print(min(total_dist_1, total_dist_2, total_dist_3, total_dist_4))