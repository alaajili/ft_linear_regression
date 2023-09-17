import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv");
_mileages = data['km'].tolist()
_prices = data['price'].tolist()

min_mileage = min(_mileages)
max_mileage = max(_mileages)
mileages = [(x - min_mileage) / (max_mileage - min_mileage) for x in _mileages]

min_price = min(_prices)
max_price = max(_prices)
prices = [(x - min_price) / (max_price - min_price) for x in _prices]


theta0 = 0
theta1 = 0

# scaled_x = (x - min) / (max - min)
# x- min = scaled_x * (max - min)
# x  = scaled_x * (max - min) + min


learning_rate = 0.1
epochs = 500

m = len(data)

# hypothesis function
def estimatePrice(mileage):
    scaled_mileage = (mileage - min_mileage) / (max_mileage - min_mileage)
    scaled_price = (theta0 + (theta1 * scaled_mileage))
    price = scaled_price * (max_price - min_price) + min_price
    return price; 


for epoch in range(epochs):
    # here we calculate the predictions
    predictions = [ (theta0 + (theta1 * x)) for x in mileages]

    # here we calculate the errors of the predictions
    errors = [x - y for x, y in zip(predictions, prices)]


    # we calculate tmpTheta0 and tmpTheta1
    tmpTheta0 = learning_rate * (1/m) * sum(errors)
    tmpTheta1 = learning_rate * (1/m) * sum([x * y for x, y in zip(errors, mileages)])

    theta0 -= tmpTheta0
    theta1 -= tmpTheta1


est_price = estimatePrice(22899)
print(est_price)

est_prices = [estimatePrice(mileage) for mileage in _mileages]


plt.scatter(_mileages, _prices)
plt.plot(_mileages, est_prices, color="red");

plt.show()


