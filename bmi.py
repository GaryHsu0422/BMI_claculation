# Calculating BMI
h = input('Please enter your height: ')
w = input('Please enter your weight: ')
h = float(h)
w = float(w)
h = h / 100
bmi = w / h / h
if bmi < 18.5:
	print('Your bmi is:', bmi, 'you are underweight')
elif bmi >= 18.5 and bmi < 24.9:
	print('Your bmi is:', bmi, 'you are in normal weight')
elif bmi >= 25 and bmi < 29.9:
	print('Your bmi is:', bmi, 'you are overweight')
elif bmi >= 30 and bmi < 34.9:
	print('Your bmi is:', bmi, 'you are in obesity class 1')
elif bmi >= 35 and bmi < 39.9: 
	print('Your bmi is:', bmi, 'you are in obesity class 2')
else:
	print('Your bmi is:', bmi, 'you are in obesity class 3')
