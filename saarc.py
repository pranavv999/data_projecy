import csv
from collections import OrderedDict
import matplotlib.pyplot as plt


saarc_countries = [
    "Afghanistan",
    "Bangladesh",
    "Bhutan",
    "India",
    "Maldives",
    "Nepal",
    "Pakistan",
    "Sri Lanka",
]

over_years = [
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
]


def extract_data(file_name):

    data = OrderedDict()
    with open(file_name, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row["Region"] in saarc_countries and row["Year"] in over_years:
                value = float(row["Population"])
                data[row["Year"]] = data.get(row["Year"], 0) + value
    return data


def graph_plot():
    # Data
    values = extract_data("population-estimates.csv")
    population = list(values.values())
    labels = over_years

    width = [0.45, 0.45, 0.45, 0.45, 0.5, 0.55, 0.6, 0.6, 0.6, 0.6, 0.6]
    plt.bar(
        labels,
        population,
        width,
        color="orange",
        edgecolor="blue",
        zorder=2,
    )

    plt.grid(axis="y")
    plt.xlabel("Year", {"size": 20, "color": "k"}, labelpad=10, alpha=0.5)
    plt.ylabel(
        "Population 1 x 10^6",
        {"size": 20, "color": "k"},
        labelpad=10,
        alpha=0.5,
    )
    plt.title(
        "SAARC countries population for year 2004 to 2014",
        {"size": 20, "color": "b"},
    )
    return plt.show()


if __name__ == "__main__":
    graph_plot()
