from matplotlib.figure import Figure

AVG_NT = 4899
AVG_NE = 4751

def create_capacity_graph(user_nt, user_ne):
    labels = ["NT (Sanctioned)", "NE (Enrolled)"]
    user_values = [user_nt, user_ne]
    avg_values = [AVG_NT, AVG_NE]

    fig = Figure(figsize=(5, 3))
    ax = fig.add_subplot(111)

    width = 0.35
    x = range(len(labels))

    ax.bar([i - width/2 for i in x], user_values, width, label="Your Institution", color="#4e79a7")
    ax.bar([i + width/2 for i in x], avg_values, width, label="National Average", color="#f28e2b")

    ax.set_ylabel("Number of Students")
    ax.set_title("Sanctioned vs Enrolled Seats (Compared to National Average)")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()

    return fig