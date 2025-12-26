import tkinter as tk
from tkinter import ttk
from ui.OI.rd_calculator import RDCalculatorFrame
from ui.OI.wd_calculator import WDCalculatorFrame
from ui.TLR.ss_calculator import SSCalculatorFrame
from ui.TLR.fsr_calculator import FSRCalculatorFrame
from ui.TLR.fqe_calculator import FQECalculatorFrame
from ui.TLR.fru_calculator import FRUCalculatorFrame
from ui.GO.gph_calculator import GPHCalculatorFrame
from ui.GO.gui_calculator import GUICalculatorFrame
from ui.GO.gms_calculator import GMSCalculatorFrame
from ui.GO.gphd_calculator import GPHDCalculatorFrame
from ui.OI.escs_calculator import ESCSCalculatorFrame
from ui.RP.fppp_calculator import FPPPCalculatorFrame
from ui.score_frame_toggle import create_toggle_function, create_score_table_builder
from ui.geimini_recommendation.gemini_recommendation import GeminiRecommendationFrame

def main():
    root = tk.Tk()
    root.title("NIRF TLR Assistant")
    root.geometry("1200x1000")
    
    calculator_frames = {}
    
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=0)
    root.grid_rowconfigure(4, weight=0)
    root.grid_rowconfigure(5, weight=10)
    
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    
    # Create content frame for dynamic UI loading
    content_frame = ttk.Frame(root)
    content_frame.grid(row=1, column=0, columnspan=2, rowspan=2, sticky="nsew")
    content_frame.grid_rowconfigure(0, weight=1, uniform="row")
    content_frame.grid_rowconfigure(1, weight=1, uniform="row")
    content_frame.grid_columnconfigure(0, weight=1, uniform="col")
    content_frame.grid_columnconfigure(1, weight=1, uniform="col")
    
    # Score table frame with border
    score_table_frame = ttk.Frame(root, relief="solid", borderwidth=2)
    
    # Dictionary to store score label references
    score_labels = {}
    
    # Configure column weights for proper spacing (will be updated dynamically)
    for col in range(4):
        score_table_frame.grid_columnconfigure(col, weight=1)
    
    # Initially hide the score frame
    score_table_frame.grid_remove()
    
    # Gemini recommendation frame
    gemini_frame = GeminiRecommendationFrame(root)
    gemini_frame.grid(row=5, column=0, columnspan=2, sticky="nsew")
    
    # Create score table builder and toggle function
    rebuild_score_table = create_score_table_builder(score_table_frame, calculator_frames, score_labels)
    toggle_score_frame, score_visible = create_toggle_function(
        score_table_frame, gemini_frame, calculator_frames, score_labels
    )
    
    # Center button frame (created after toggle function is defined)
    overall_score_frame = ttk.Frame(root)
    overall_score_frame.grid(row=3, column=0, columnspan=2, pady=10)
    overall_score_btn = ttk.Button(overall_score_frame, text="Show Overall Scores", command=toggle_score_frame)
    overall_score_btn.pack()
    
    def clear_content_frame():
        for widget in content_frame.winfo_children():
            widget.destroy()
    
    def load_tlr_ui():
        clear_content_frame()
        
        # Clear and rebuild calculator_frames for TLR
        calculator_frames.clear()
        
        ss_frame = SSCalculatorFrame(content_frame)
        ss_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        fsr_frame = FSRCalculatorFrame(content_frame)
        fsr_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    
        fqe_frame = FQECalculatorFrame(content_frame)
        fqe_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
        fru_frame = FRUCalculatorFrame(content_frame)
        fru_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        calculator_frames["ss"] = ss_frame
        calculator_frames["fsr"] = fsr_frame
        calculator_frames["fqe"] = fqe_frame
        calculator_frames["fru"] = fru_frame
        
        ss_frame.set_gemini_frame(gemini_frame)
        fsr_frame.set_gemini_frame(gemini_frame)
        fqe_frame.set_gemini_frame(gemini_frame)
        fru_frame.set_gemini_frame(gemini_frame)
        
        # Rebuild score table with TLR headers
        rebuild_score_table(["SS", "FSR", "FQE", "FRU"])
    
    def load_go_ui():
        clear_content_frame()
        
        # Clear and rebuild calculator_frames for GO
        calculator_frames.clear()
        
        gph_frame = GPHCalculatorFrame(content_frame)
        gph_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        gui_frame = GUICalculatorFrame(content_frame)
        gui_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        gms_frame = GMSCalculatorFrame(content_frame)
        gms_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        gphd_frame = GPHDCalculatorFrame(content_frame)
        gphd_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        calculator_frames["gph"] = gph_frame
        calculator_frames["gui"] = gui_frame
        calculator_frames["gms"] = gms_frame
        calculator_frames["gphd"] = gphd_frame
        
        gms_frame.set_gemini_frame(gemini_frame)
        gui_frame.set_gemini_frame(gemini_frame)
        gphd_frame.set_gemini_frame(gemini_frame)
        gph_frame.set_gemini_frame(gemini_frame)
        
        # Rebuild score table with GO headers
        rebuild_score_table(["GPH", "GUI", "GMS", "GPHD"])
    
    def load_io_ui():
        clear_content_frame()
        
        # Clear and rebuild calculator_frames for OI
        calculator_frames.clear()
        
        rd_frame = RDCalculatorFrame(content_frame)
        rd_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        wd_frame = WDCalculatorFrame(content_frame)
        wd_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    
        escs_frame = ESCSCalculatorFrame(content_frame)
        escs_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        calculator_frames["rd"] = rd_frame
        calculator_frames["wd"] = wd_frame
        calculator_frames["escs"] = escs_frame
        
        escs_frame.set_gemini_frame(gemini_frame)
        wd_frame.set_gemini_frame(gemini_frame)
        rd_frame.set_gemini_frame(gemini_frame)
        
        # Rebuild score table with OI headers
        rebuild_score_table(["RD", "WD", "ESCS"])
    
    def load_rp_ui():
        clear_content_frame()
        
        calculator_frames.clear()
        
        fppp_frame = FPPPCalculatorFrame(content_frame)
        fppp_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        calculator_frames["fppp"] = fppp_frame
        
        fppp_frame.set_gemini_frame(gemini_frame)
        
        # Rebuild score tables with RP headers
        rebuild_score_table(["FPPP", "IPR", "QP", "PU"])
        
    button_frame = ttk.Frame(root)
    button_frame.grid(row=0, column=0, columnspan=2, sticky="n")
    
    tlr_button = ttk.Button(button_frame, text="TLR", command=load_tlr_ui)
    go_button = ttk.Button(button_frame, text="GO", command=load_go_ui)
    oi_button = ttk.Button(button_frame, text="OI", command=load_io_ui)
    rp_button = ttk.Button(button_frame, text="RP", command=load_rp_ui)
    
    tlr_button.pack(side="left", padx=5)
    go_button.pack(side="left", padx=5)
    oi_button.pack(side="left", padx=5)
    rp_button.pack(side="left", padx=5)
    
    # Load TLR UI by default
    load_tlr_ui()
    
    print("UI Loaded Successfully")
    root.mainloop()

if __name__ == "__main__":
    main()