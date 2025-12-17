from matplotlib.figure import Figure

AVG_SS = 14.06

def create_ss_score_graph(user_ss_score):
    labels = ["SS Score"]
    user_values = [user_ss_score]
    avg_values = [AVG_SS]

    fig = Figure(figsize=(5, 3))
    ax = fig.add_subplot(111)

    width = 0.35
    x = range(len(labels))

    ax.bar([i - width/2 for i in x], user_values, width, label="Your Score", color="#4e79a7")
    ax.bar([i + width/2 for i in x], avg_values, width, label="National Average", color="#f28e2b")

    ax.set_ylabel("Score")
    ax.set_title("SS Score vs National Average")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()

    return fig