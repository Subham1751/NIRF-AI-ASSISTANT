from tkinter import ttk

def create_score_table_builder(score_table_frame, calculator_frames, score_labels):
    def rebuild_score_table(headers):
        # Clear existing widgets in the score table
        for widget in score_table_frame.winfo_children():
            widget.destroy()
        
        # Clear the score_labels dictionary
        score_labels.clear()
        
        # Create header row
        for col, header in enumerate(headers):
            lbl = ttk.Label(
                score_table_frame, text=header, relief="solid", borderwidth=1,
                padding=5, font=("Arial", 10, "bold")
            )
            lbl.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)
        
        # Create data row with dynamic labels
        for col, header in enumerate(headers):
            score_lbl = ttk.Label(
                score_table_frame, text="N/A", relief="solid", borderwidth=1, padding=5
            )
            score_lbl.grid(row=1, column=col, sticky="nsew", padx=1, pady=1)
            # Store reference using lowercase header as key
            score_labels[header.lower()] = score_lbl
        
        # Configure column weights
        for col in range(len(headers)):
            score_table_frame.grid_columnconfigure(col, weight=1)
    
    return rebuild_score_table


def create_toggle_function(score_table_frame, gemini_frame, calculator_frames, score_labels):

    score_visible = [False]  # Using list to allow modification in nested function
    
    def get_score_from_frame(key, frame):
        # Totals for specific TLR and RP scores
        totals = {
            'ss': 20,
            'fsr': 30,
            'fqe': 20,
            'fru': 30,
            # RP scores
            'pu': 35,
            'qp': 40,
            'ipr': 15,
            'fppp': 10,
            # GO scores
            'gph': 40,
            'gui': 15,
            'gms': 25,
            'gphd': 20,
            # OI scores
            'rd': 30,
            'wd': 30,
            'escs': 20,
            'pcs': 20,
        }
        try:
            if frame and hasattr(frame, 'output_entry'):
                score_text = frame.output_entry.get().strip()
                # Try to convert to float to validate it's a number
                score = float(score_text)
                formatted = f"{score:.2f}"
                if key in totals:
                    return f"{formatted}/{totals[key]}"
                return formatted
        except (ValueError, AttributeError):
            pass
        return "N/A"
    
    def update_scores():
        for key in score_labels.keys():
            if key in calculator_frames:
                score_labels[key].config(text=get_score_from_frame(key, calculator_frames.get(key)))
    
    def toggle_score_frame():
        if score_visible[0]:
            # Hide the score frame
            score_table_frame.grid_remove()
            gemini_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")
            score_visible[0] = False
        else:
            # Update scores before showing
            update_scores()
            # Show the score frame
            score_table_frame.grid(row=4, column=0, columnspan=2)
            gemini_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")
            score_visible[0] = True
    
    return toggle_score_frame, score_visible
