import csv
from collections import OrderedDict
import matplotlib.pyplot as plt

asean_countries = [
    "Brunei",
    "Combodia",
    "Indonesia",
    "Laos",
    "Malaysia",
    "Myanmar",
    "Philippines",
    "Singapore",
    "Thailand",
    "Vietnam",
]


def extract_data(file):
    countries = [
        "Brunei Darussalam",
        "Cambodia",
        "Indonesia",
        "Lao People's Democratic Republic",
        "Malaysia",
        "Myanmar",
        "Philippines",
        "Singapore",
        "Thailand",
        "Viet Nam",
    ]

    data = OrderedDict()

    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if row["Region"] in countries and row["Year"] == "2014":
                value = int(float(row["Population"]))
                data[row["Region"]] = value

    return data


def graph_plot():
    # Data
    data = extract_data("population-estimates.csv")
    population = list(data.values())

    width = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    plt.bar(asean_countries, population, width, color="orange", zorder=2)

    plt.grid(axis="y")
    plt.xlabel("Countries", {"size": 20, "color": "k"}, labelpad=10, alpha=0.5)
    plt.ylabel(
        "Population ",
        {"size": 20, "color": "k"},
        labelpad=10,
        alpha=0.5,
    )
    plt.title(
        "Population of ASEAN countries for year 2014",
        {"size": 20, "color": "b"},
    )
    return plt.show()


if __name__ == "__main__":
    graph_plot()
