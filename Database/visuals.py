import matplotlib.pyplot as plt


def bar_chart(x, y, labelx, labely, title):
    plt.bar(x, y, color="green")
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

def 