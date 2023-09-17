import pandas as pd

data = pd.read_csv("data.csv");
mileages = data['km'].tolist()
prices = data['price'].tolist()


theta0 = 0
theta1 = 0
# predictions = [ (theta0 + (theta1 * x)) for x in mileages]
# print(sum(predictions))


learning_rate = 0.0001
epochs = 1000

m = len(data)
print(m)

# hypothesis function
def estimatePrice(mileage):
    return theta0 + (theta1 * mileage)


for epoch in range(epochs):
    # here we calculate the predictions
    predictions = [ (theta0 + (theta1 * x)) for x in mileages]

    # here we calculate the errors of the predictions
    errors = [x - y for x, y in zip(predictions, prices)]


    # we calculate tmpTheta0 and tmpTheta1
    tmpTheta0 = learning_rate * (1/m) * sum(errors)
    tmpTheta1 = learning_rate * (1/m) * sum([x * y for x, y in zip (errors, mileages)])

    






print(estimatePrice(240000))


