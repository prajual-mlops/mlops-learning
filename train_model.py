from sklearn.tree import DecisionTreeClassifier

#Features
x = [
    [25, 30000],
    [40, 70000],
    [35, 50000],
    [28, 35000],
    [50, 90000]
]

#Target
y = [
    0,
    1,
    1,
    0,
    1
]

model = DecisionTreeClassifier()

model.fit(x, y)

prediction = model.predict([[30, 40000]])

print("Prediction:", prediction)
