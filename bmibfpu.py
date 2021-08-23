# calculating BMI
h = input('Please enter your height: ')
w = input('Please enter your weight: ')
a = input('Please enter your age: ')
g = input('Please enter the code of your gender (if male, insert 1; if female, insert 0): ')
h = float(h)
w = float(w)
a = float(a)
g = float(g)
h = h / 100
bmi = w / h / h
bfp = (1.39 * bmi) + (0.16 * a) - (10.34 * g) - 9
if bmi < 18.5:
	print('Your bmi is:', bmi, 'you are underweight, your body fat percentage is:', bfp )
elif bmi >= 18.5 and bmi < 24.9:
	print('Your bmi is:', bmi, 'you are in normal weight, your body fat percentage is:', bfp )
elif bmi >= 25 and bmi < 29.9:
	print('Your bmi is:', bmi, 'you are overweight, your body fat percentage is:', bfp )
elif bmi >= 30 and bmi < 34.9:
	print('Your bmi is:', bmi, 'you are in obesity class 1, your body fat percentage is:', bfp )
elif bmi >= 35 and bmi < 39.9: 
	print('Your bmi is:', bmi, 'you are in obesity class 2, your body fat percentage is:', bfp )
else:
	print('Your bmi is:', bmi, 'you are in obesity class 3, your body fat percentage is:', bfp )