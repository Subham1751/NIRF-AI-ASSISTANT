from matplotlib.figure import Figure

def create_experience_graph():
    total_faculty = 240
    F1 = 143 / total_faculty
    F2 = 59 / total_faculty
    F3 = 38 / total_faculty

    actual_values = [F1 * 100, F2 * 100, F3 * 100]
    ideal_values = [33.33, 33.33, 33.33]
    labels = ["≤ 8 yrs", "8–15 yrs", "> 15 yrs"]

    fig = Figure(figsize=(5, 3))
    ax = fig.add_subplot(111)

    width = 0.35
    x = range(len(labels))

    ax.bar([i - width/2 for i in x], actual_values, width, label="Actual", color="#4e79a7")
    ax.bar([i + width/2 for i in x], ideal_values, width, label="Ideal (33%)", color="#f28e2b")

    ax.set_ylabel("Percentage (%)")
    ax.set_title("Faculty Experience Distribution – Actual vs Ideal")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()

    return fig
