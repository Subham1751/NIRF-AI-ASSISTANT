from matplotlib.figure import Figure

def create_primary_graph():
    FQ = 4.65
    FE = 7.11
    FQE = 11.76

    fig = Figure(figsize=(5, 3))
    ax = fig.add_subplot(111)

    labels = ["FQ (10)", "FE (10)", "FQE (20)"]
    values = [FQ, FE, FQE]
    ax.bar(labels, values, color=["#4e79a7", "#f28e2b", "#59a14f"])

    ax.set_ylabel("Score")
    ax.set_title("FQ, FE, and FQE – Example Scores")

    return fig