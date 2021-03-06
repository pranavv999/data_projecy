import csv
import matplotlib.pyplot as plt

# Following are the ASEAN countries
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
    """Return the population data for ASEAN countries for year 2004"""
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

    data = dict()

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
    # width for each coloumn is different
    width = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75]
    fig, ax = plt.subplots()
    plt.bar(
        asean_countries,
        population,
        width,
        color="orange",
        edgecolor="blue",
        zorder=2,
    )
    # Add Title and x-axis tick, set frame dimensions etc.
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
    # plt.xticks(fontsize=15, rotation=-45)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=12)
    ax.spines["top"].set_linewidth(1.7)
    ax.spines["right"].set_linewidth(1.7)
    ax.spines["bottom"].set_linewidth(1.7)
    ax.spines["left"].set_linewidth(1.7)
    return plt.show()


if __name__ == "__main__":
    graph_plot()
