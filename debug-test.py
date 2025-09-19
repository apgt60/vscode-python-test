import numpy as np
import pandas as pd

print("-------------------")

list_mul = ['2','2','2']
list_mul*2
# print("answer:", list_mul*2)

def function(var1=2, var2=4):
    var2 = 6
    var1 = 5
    # print(var1, var2)

function(10, 20)


sports = ['Cricket', 'Football', 'Tennis', 'Golf', 'Baseball']
sports_new = np.array(sports)
# print(sports_new)

mat = np.array([[1,2,1],[4,5,9],[1,8,9]])
# print(mat)

# adding a step size of 5 to create an array
arr3  = np.arange(10, 20, 3)
# print(arr3)

vec = np.linspace(10,20,3)
#print(vec)

vec1 = np.arange(0, 12)
vec2 = vec1.reshape(4, 3)
#print(vec2)

vec = np.arange(0,5) 
# print(vec.reshape((2,3)))

vec1 = [10,15,20]
vec2 = [15,25,35]
# print(vec1+vec2)

vec1 = np.linspace(20,50,4)
# print("vec1:", vec1)
vec2 = np.linspace(100,120,3)
# print("vec2:", vec2)
# print(vec1 + vec2)

vec = np.arange(2,5,1)
# print("vec:", vec)
# print(1/vec)
# print(vec**2)

mat1 = np.arange(1,5).reshape(2,2)
# print("mat1:", mat1)
mat2 = np.eye(2)
# print("mat2:", mat2)
# print(mat1/mat2)

r1 = np.random.rand(5)
# print("r1:", r1)
r2 = np.random.randint(5) #gives random value between 0 and 5
# print("r2:", r2)

mat1 = np.arange(-9,0,1).reshape(3,3)
# print("mat1:", mat1)
# print("min:", np.min(mat1))
# print("max:", np.max(mat1))

rand = np.random.rand()


rand = np.random.randn()
#print("rand:", rand)

arange = np.arange(8)
#print("arange:", arange)

arange = np.arange(1, 10, 2)
#print("arange:", arange)

np_array = np.arange(6)
# print("np_array:", np_array)
np_array_mod = np_array[np_array==5]
# print("np_array_mod:", np_array_mod)
np_array_mod2 = np_array[np_array>3]=99
# print("np_array_mod2", np_array_mod2)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix[1][1])

vec = np.array([4,7,8,9,10,6,1])
# print(vec[vec>6])

vec1 = np.array([4, 7, 8, 9, 10, 6, 1])
vec1[vec1>6] = 2
# print(vec1)

matrix = np.arange(1,10).reshape(3,3)
matrix[0:2,1:2] = 0
# print(matrix)

array1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array2 = array1.copy()
array2[array2>5] = 0
# print("array1",array1)
# print("array2",array2)

newDf = pd.DataFrame()
# print("newDf",newDf, "type", type(newDf))
calorie_data = pd.DataFrame({'day': ['day1','day2','day3','day4','day5']
                           ,'calories': [450, 300, 345, 520, 600]
                           ,'duration_min': [30, 25, 29, 39, 48]
                           })
# print(calorie_data[::2])

calorie_data = pd.DataFrame({'day': ['day1','day2','day3','day4','day5']
                           ,'calories': [450, 300, 345, 520, 600]
                           ,'duration_min': [30, 25, 29, 39, 48]
                           })
# print("calorie_data.iloc[[1,2],[1]]:\n", calorie_data.iloc[[1,2],[1]])
# print("calorie_data.loc[[1,2],['calories']]:\n", calorie_data.loc[[1,2],['calories']])

calorie_data = pd.DataFrame({'day': ['day1','day2','day3','day4','day5']
                           ,'calories': [450, 300, 345, 520, 600]
                           ,'duration_min': [30, 25, 29, 39, 48]
                           })
# print("result:\n", calorie_data.loc[calorie_data['calories']>500])


demo_matrix = np.array(([13,35,74,48], [23,37,37,38],[73,39,93,39]))
# print("q1\n", demo_matrix[0:3, 1:3])

demo_array = np.arange(0,10)
# print("demo_array", demo_array)
# print("demo_array", demo_array<3)

flowers = pd.Series([2, 3, 5, 4], index=['lily', 'rose', 'daisy', 'lotus'])
# print("flowers['daisy']", flowers['daisy'])


df = calorie_data

booksdf = pd.read_csv('books.csv')

df = booksdf
# print("booksdf.shape:", booksdf.shape)

print("df.shape1",df.shape)

dfdropped = df.drop('year', axis = 1)
print("dfdropped.shape", dfdropped.shape)
print("df.shape2",df.shape)


counts = df['language_code'].value_counts()
# print("counts\n", counts)

dawCond1 = df['publisher'] == 'DAW'
dawCond2 = df['average_rating'] > 4
booksCond12 = df[dawCond1 & dawCond2]

# print("booksCond12\n", booksCond12)
books500and2010 = df[(df['num_pages'] > 500) & (df['year'] > 2010)]
# print("books500and2010\n", books500and2010)

booksAgatha = df[df['author'] == 'Agatha Christie']
# print("booksAgatha", booksAgatha)

spanish2000 = df[(df['language_code'] == 'spa') & (df['year'] > 2000)]
# print("spanish2000", spanish2000)

books2010 = df[df['year'] == 2010].count()
# print("books2010", books2010)

mean = df['num_pages'].mean()
# print("booksdf:", "mean", mean)

# dfsub1 = df.iloc[0:5, 0:4]
# print("dfsub1.shape", dfsub1.shape)


filtereddf = df[(df['average_rating'] > 4.5) & (df['ratings_count'] < 10)]
# print("filtereddf.shape", filtereddf.shape)

#What is the mean of ‘average_rating’ for the books where ‘language_code’ is ‘eng’?
# (Hint: You can use groupby() to group the data)
# grouped_mean = df.groupby('Category')['Value'].mean()
grouped_mean = df.groupby('language_code')['average_rating'].mean()
# print("grouped_mean:", grouped_mean)


# print("booksdf.describe()", booksdf.describe())
# print(booksdf.dtypes)
condition = booksdf['average_rating'] > 4
booksRatingGt4 = booksdf[condition]
# age_filtered = df['calories'] > 23
# print("booksRatingGt4:\n", booksRatingGt4.shape)


n1 = np.matrix([[121, 144, 169], [196, 225, 256], [ 289, 324, 361]])
n2 = np.matrix([[ 1, 4, 9], [ 1, 5, 4], [ 9, 4, 8]])
dot_product = np.dot(n1, n2)
# print("dot_product:\n", dot_product)

# print("np.ones([2,2]):\n", np.ones([2,2]))

array_1 = np.array([1, 2, 3, 5, 8])
array_2 = np.array([0, 3, 4, 2, 1])
new_array = array_1+ array_2
final_array = new_array*array_1
# print("final_array[2]:", final_array[2])

mat = np.array([[1, 2, 1], [4, 5, 9],[1, 8, 9]])
# print("matb4\n", mat)
mat[1]=5
# print('matafter\n', mat)

list_1 = [1,2,3] 
list_2 = [4,5,6]
new_list = list_1 + list_2
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
new_array = array_1 + array_2
# print("new_list", new_list)
# print("new_array", new_array)



a = np.arange(-2,20)
spl27 = a[2:7]
# print("spl27", spl27)
lt0 = a[a<0]
# print("lt0", lt0)
npcos = np.cos([0, 1, 2, 3, 4]) 
# print("npcos", npcos)

mat = np.matrix([[ 1, 4, 9, 121, 144, 169],
                [ 16, 25, 36, 196, 225, 256], 
                [ 49, 64, 81, 289, 324, 361]])

matmean = mat.mean()
# print("matmean", matmean)

array_1 = np.linspace(0,20,6)
array_2 = np.arange(0,20,6)
# print("array_1", array_1)
# print("array_2", array_2)

arr3x3 = np.arange(start=1, stop=10, step=1).reshape(3,3)
# print("arr3x3", arr3x3)

sales_data = [150, 200, 250, 300, 350]
array = np.array(sales_data)
sliced_array = array[1:4]

sales_data = np.array([100, 150, 200, 250, 300])
new_sale = 350
updated_sales_data = np.append(sales_data, new_sale)

team_a_scores = np.array([80,85,90,95,100])
team_b_scores = np.array([70,75,80,85,90])
all_team_scores = np.concatenate((team_a_scores, team_b_scores))

# group = df.groupby('calories')
# merged = pd.merge(df, df, how='inner', on="calories")


# min_cal = group['duration_min'].min()
# print("min_cal:", min_cal)

# age_filtered = df['calories'] > 23
# result = df[age_filtered]
# mean = df['calories'].mean()
# min_amount = df['calories'].min()

#print("mean calories:", mean)
#print("min calories", min_amount)



