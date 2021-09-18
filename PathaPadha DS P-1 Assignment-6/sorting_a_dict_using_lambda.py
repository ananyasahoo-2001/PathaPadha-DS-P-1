# Write a Python Program to sort a list of dictionaries by model using Lambda

models = [{'make':'Nokia' , 'model':216 , 'color':'Black'},{'make':'Mi Max' , 'model':2 , 'color':'Gold'} , {'make':'Samsung','model':7,'color':'Blue'}]
sorted_model = sorted(models , key = lambda x : x['model'])
print(list(sorted_model))
