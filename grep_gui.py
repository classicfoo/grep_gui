import tkinter as tk
import pickle

def extract_lines_with_keywords(text, keywords):
    lines = text.split("\n")
    keywords = [keyword.lower() for keyword in keywords.split()]
    result = []
    for line in lines:
        if all(keyword in line.lower() for keyword in keywords):
            result.append(line)
    return result

def save_text(*args):
    text = text_input.get("1.0", 'end-1c')
    with open("text.pkl", "wb") as f:
        pickle.dump(text, f)

def load_text():
    try:
        with open("text.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return ""

def update_result(*args):
    text = text_input.get("1.0", 'end-1c')
    keyword = keyword_input.get()
    result = extract_lines_with_keywords(text, keyword)
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert("1.0", "\n".join(result))
    result_text.config(state="disabled")

root = tk.Tk()
root.title("Grep Gui")

keyword_frame = tk.Frame(root)
keyword_frame.pack(fill="x")

keyword_label = tk.Label(keyword_frame, text="Keywords:")
keyword_label.pack(side="left")

keyword_input = tk.Entry(keyword_frame)
keyword_input.pack(fill="x", expand=True)
keyword_input.bind("<KeyRelease>", update_result)

text_frame = tk.Frame(root)
text_frame.pack(side="left", fill="both", expand=True)

text_input = tk.Text(text_frame, height=10, width=30)
text_input.pack(fill="both", expand=True)
text_input.insert("1.0", load_text())
text_input.bind("<KeyRelease>", update_result)
text_input.bind("<KeyRelease>", save_text)

result_text = tk.Text(root, height=10, width=30, state="disabled")
result_text.pack(fill="both", expand=True)

root.mainloop()
