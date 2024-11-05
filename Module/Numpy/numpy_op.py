import numpy as np
"""
initail_array = np.array([11,23,33])
print("initail_array", initail_array)
print('the datatypes of the initail_array is \n',type(initail_array))
print("- " * 40)


send_array= np.array([[[1,2,3],
                        [4,5,6]],
                        [[7,8,9],
                        [9,5,1]]])
print("send_array",send_array)
print(type(send_array))
print(send_array.shape)


#create dummy data 
zero_data= np.zeros((3,2,3))
print(zero_data)

one_data= np.ones((2,2,3))
print(one_data)

one_data= np.full((2,3), 5)


identity_matrix= np.eye(5)
print(identity_matrix)

a_data= np.arange(5)
print(a_data)


a_data= np.arange(5, 6, .2) #  giving a range to data 
print(a_data)


lin_data = np.linspace(2,4)
print(lin_data)
print(len(lin_data))

lin_data = np.linspace(2,4,5)
print(lin_data)



new_array= np.array([np.arange(2,20,2)])
print(new_array)

new_array= np.array(np.arange(2,20,2))
print(new_array[2: 10])

new_array= np.array([np.arange(2,50,3), np.arange(3,51,3)])
print(new_array)
print('#' *20)
print(new_array[1, :])
print("->" *30)
print(new_array[: ,3])


array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
new_arr = array_1 + array_2
print(new_arr)
print("->" *50)
ano_arr = array_1 * array_2
print(ano_arr)
print("->" *50)
power_arr = array_1 ** array_2
print(power_arr)
print("->" *50)
new = np.dot(array_1,array_2)
print(new)
print("->" *50)

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
new_a = np.std(a2)
print(new_a)
print("->" *50)
new_2 = np.var(a2)
print(new_2)
new_1 = np.min(a1)
print(new_1)
print("->" *50)

a3= a2 > 5
print(a3)

"""
random_data = np.random.randint(1,11,size= (4,5))
print(np.sort(random_data))