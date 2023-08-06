from matplotlib import pyplot as plt


def show_swiss_roll(X, color):
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.rainbow)
    plt.title('Swiss Roll in 3D')
    plt.show()


def test_model(model, X, color):
    x = model.fit_transform(X)
    plt.figure(figsize=(6, 6))
    plt.grid(linestyle="dotted")
    plt.scatter(x[:, 0], x[:, 1], c=color, cmap=plt.cm.rainbow)
    plt.show()
