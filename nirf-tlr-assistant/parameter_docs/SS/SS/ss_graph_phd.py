from matplotlib.figure import Figure

AVG_NP = 487

def create_phd_graph(user_np):
    labels = ["PhD Students"]
    user_values = [user_np]
    avg_values = [AVG_NP]

    fig = Figure(figsize=(5, 3))
    ax = fig.add_subplot(111)

    width = 0.35
    x = range(len(labels))

    ax.bar([i - width/2 for i in x], user_values, width, label="Your Institution", color="#4e79a7")
    ax.bar([i + width/2 for i in x], avg_values, width, label="National Average", color="#f28e2b")

    ax.set_ylabel("Students")
    ax.set_title("PhD Strength Comparison")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()

    return fig