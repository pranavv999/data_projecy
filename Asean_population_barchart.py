import csv
from collections import OrderedDict
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
# We are refering data from year 2004 to 2014
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


def extract_data(file):
    """Return the population data for ASEAN countries in a OrderedDict"""
    data = OrderedDict(
        {
            "Brunei Darussalam": [],
            "Cambodia": [],
            "Indonesia": [],
            "Lao People's Democratic Republic": [],
            "Malaysia": [],
            "Myanmar": [],
            "Philippines": [],
            "Singapore": [],
            "Thailand": [],
            "Viet Nam": [],
        }
    )
    with open(file, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=",")

        for row in csv_reader:
            if row["Region"] in data and row["Year"] in over_years:
                value = int(float(row["Population"]))
                data[row["Region"]].append(value)

    return data


def graph_plot():
    # Data
    values = extract_data("population-estimates.csv")
    labels = over_years
    # width of the bar
    width = 0.37
    # Label Locations
    bar1 = [(i * 4) for i in range(len(labels))]
    bar2 = [(i + width) for i in bar1]
    bar3 = [(i + width * 2) for i in bar1]
    bar4 = [(i + width * 3) for i in bar1]
    bar5 = [(i + width * 4) for i in bar1]
    bar6 = [(i + width * 5) for i in bar1]
    bar7 = [(i + width * 6) for i in bar1]
    bar8 = [(i + width * 7) for i in bar1]
    bar9 = [(i + width * 8) for i in bar1]
    bar10 = [(i + width * 9) for i in bar1]

    fig, ax = plt.subplots()
    ax.bar(bar1, values["Brunei Darussalam"], width, label="Brunei")
    ax.bar(bar2, values["Cambodia"], width, label="Combodia")
    ax.bar(bar3, values["Indonesia"], width, label="Indonesia")
    ax.bar(
        bar4,
        values["Lao People's Democratic Republic"],
        width,
        label="Laos"
        )
    ax.bar(bar5, values["Malaysia"], width, label="Malaysia")
    ax.bar(bar6, values["Myanmar"], width, label="Myanmar")
    ax.bar(bar7, values["Philippines"], width, label="Philippins")
    ax.bar(bar8, values["Singapore"], width, label="Singapore")
    ax.bar(bar9, values["Thailand"], width, label="Thailand")
    ax.bar(bar10, values["Viet Nam"], width, label="Vietnam")

    # Add some Labels, Title and x-axis tick
    ax.set_title("Population Growth in ASEAN Countries")
    ax.set_ylabel(
        "Population",
        {"size": 15, "color": "k"},
        labelpad=10,
        alpha=0.5
        )
    ax.set_xlabel("Years", {"size": 15, "color": "k"}, labelpad=10, alpha=0.5)
    ax.set_xticks(bar5)
    ax.set_xticklabels(labels)
    ax.legend(loc="upper right", bbox_to_anchor=(1, 1))
    fig.set_figwidth(8)
    # return plt.savefig("mygraph.png")
    return plt.show()


if __name__ == "__main__":
    graph_plot()
