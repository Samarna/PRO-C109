import statistics
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
math_list = df["math score"].tolist()
math_mode = statistics.mode(math_list)
math_mean = statistics.mean(math_list)
math_median = statistics.median(math_list)

print("Mean, median & mode of height is {},{},{}".format(math_mean,math_mode,math_median))
m_stddev = statistics.stdev(math_list)
print("Standard deviation is ",m_stddev)

h_std1_start, h_std1_end = math_mean-m_stddev , math_mean+m_stddev
h_std2_start, h_std2_end = math_mean-m_stddev*2 , math_mean+m_stddev*2
h_std3_start, h_std3_end = math_mean-m_stddev*3 , math_mean+m_stddev*3

list1 = [result for result in math_list if result > h_std1_start and result < h_std1_end]
list2 = [result for result in math_list if result > h_std2_start and result < h_std2_end]
list3 = [result for result in math_list if result > h_std3_start and result < h_std3_end]

print("{}% of data lies within 1st standard deviation".format(len(list1)*100/len(math_list)))
print("{}% of data lies within 2nd standard deviation".format(len(list2)*100/len(math_list)))
print("{}% of data lies within 3rd standard deviation".format(len(list3)*100/len(math_list)))
