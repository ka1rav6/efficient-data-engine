import sys
import io
import contextlib
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import inputProcessing as ip
import errorHandling as err
import data_engine as de  # type: ignore


def capture_output(func, *args):
    """Run func(*args) and return whatever it printed as a string."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        func(*args)
    return buf.getvalue()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Data Engine")
        self.master.geometry("900x650")
        self.master.resizable(True, True)

        self.current_op   = StringVar(value="(none selected)")
        self.loaded_file  = None   # path of the CSV currently open
        self.file_mode    = False  # True while a file is loaded

        self.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self._build_menu()
        self._build_ui()

    def _build_menu(self):
        menubar = Menu(self.master)
        basic = Menu(menubar, tearoff=0)
        for op in ["mean", "median", "mode", "var", "std_dev",
                   "min", "max", "range", "zscore", "percentile"]:
            basic.add_command(label=op.capitalize(),
                              command=lambda o=op: self.setOp(o))
        menubar.add_cascade(label="Basic Data", menu=basic)

        sort = Menu(menubar, tearoff=0)
        for op in ["quicksort", "bubblesort", "insertionsort"]:
            sort.add_command(label=op.capitalize(),
                             command=lambda o=op: self.setOp(o))
        menubar.add_cascade(label="Sorting", menu=sort)

        mat = Menu(menubar, tearoff=0)
        for op in ["matmul", "matadd", "matsub"]:
            mat.add_command(label=op.capitalize(),
                            command=lambda o=op: self.setOp(o))
        menubar.add_cascade(label="Matrix", menu=mat)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Load CSV…", command=self._load_file)
        file_menu.add_command(label="Close File", command=self.closeFile)
        file_menu.add_separator()
        file_menu.add_command(label="Display all", command=self.displayFile)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_command(label="Help", command=self.showHelp)
        menubar.add_command(label="Exit",  command=lambda: sys.exit(0))

        self.master.config(menu=menubar)


    def _build_ui(self):
        status_frame = Frame(self, relief=SUNKEN, bd=1)
        status_frame.pack(fill=X, pady=(0, 6))

        Label(status_frame, text="Operation:").pack(side=LEFT, padx=4)
        Label(status_frame, textvariable=self.current_op,
              fg="blue", font=("TkDefaultFont", 10, "bold")).pack(side=LEFT)

        self.file_status = Label(status_frame, text="No file loaded",
                                 fg="grey", anchor="e")
        self.file_status.pack(side=RIGHT, padx=6)

        input_frame = Frame(self)
        input_frame.pack(fill=X, pady=4)

        Label(input_frame, text="Input:").pack(side=LEFT, padx=(0, 4))
        self.entry = Entry(input_frame, font=("Consolas", 11))
        self.entry.pack(side=LEFT, fill=X, expand=True)
        self.entry.bind("<Return>", lambda e: self.run())

        Button(input_frame, text="Run ▶", command=self.run,
               bg="#4CAF50", fg="white", padx=8).pack(side=LEFT, padx=(6, 0))

        self.hint_label = Label(self, text="", fg="grey", anchor="w",
                                font=("TkDefaultFont", 9, "italic"))
        self.hint_label.pack(fill=X, padx=2)

        out_frame = Frame(self)
        out_frame.pack(fill=BOTH, expand=True, pady=(6, 0))

        Label(out_frame, text="Output:", anchor="w").pack(fill=X)

        self.output_text = Text(out_frame, font=("Consolas", 11),state=DISABLED, wrap=NONE, bg="#1e1e1e", fg="#d4d4d4", insertbackground="white", relief=SUNKEN, bd=2)
        vsb = Scrollbar(out_frame, orient=VERTICAL,
                        command=self.output_text.yview)
        hsb = Scrollbar(out_frame, orient=HORIZONTAL,
                        command=self.output_text.xview)
        self.output_text.configure(yscrollcommand=vsb.set,
                                   xscrollcommand=hsb.set)

        vsb.pack(side=RIGHT, fill=Y)
        hsb.pack(side=BOTTOM, fill=X)
        self.output_text.pack(side=LEFT, fill=BOTH, expand=True)

        # ── quick-action buttons ──
        btn_frame = Frame(self)
        btn_frame.pack(fill=X, pady=(6, 0))
        Button(btn_frame, text="Load CSV…",
               command=self._load_file).pack(side=LEFT, padx=2)
        Button(btn_frame, text="Close File",
               command=self.closeFile).pack(side=LEFT, padx=2)
        Button(btn_frame, text="Display File",
               command=self.displayFile).pack(side=LEFT, padx=2)
        Button(btn_frame, text="Clear Output",
               command=self._clear_output).pack(side=RIGHT, padx=2)

    def _show(self, text):
        self.output_text.config(state=NORMAL)
        self.output_text.delete("1.0", END)
        self.output_text.insert(END, text.rstrip())
        self.output_text.config(state=DISABLED)

    def _append(self, text):
        self.output_text.config(state=NORMAL)
        self.output_text.insert(END, text)
        self.output_text.config(state=DISABLED)

    def _clear_output(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete("1.0", END)
        self.output_text.config(state=DISABLED)


    # Hints shown under the input box for each operation
    _HINTS = {
        "mean":          "Enter numbers  separated by spaces or commas, e.g.:  10 20 30",
        "median":        "Enter numbers  separated by spaces or commas, e.g.:  10 20 30",
        "mode":          "Enter numbers  separated by spaces or commas, e.g.:  10 10 20",
        "var":           "Enter numbers  separated by spaces or commas, e.g.:  10 20 30",
        "std_dev":       "Enter numbers  separated by spaces or commas, e.g.:  10 20 30",
        "min":           "Enter numbers  separated by spaces or commas, e.g.:  10 20 30",
        "max":           "Enter numbers  separated by spaces or commas, e.g.:  10 20 30",
        "range":         "Enter numbers  separated by spaces or commas, e.g.:  10 20 30",
        "zscore":        "Enter value then data, e.g.:  15 10 20 30 40",
        "percentile":    "Enter value then data, e.g.:  25 10 20 30 40",
        "quicksort":     "Enter datatype (int/float) then numbers, e.g.:  int 5 2 8 1",
        "bubblesort":    "Enter datatype (int/float) then numbers, e.g.:  int 5 2 8 1",
        "insertionsort": "Enter datatype (int/float) then numbers, e.g.:  int 5 2 8 1",
        "matmul":        "Enter datatype then number of matrices, e.g.:  float 2  (then follow prompts — use the terminal)",
        "matadd":        "Enter datatype then number of matrices, e.g.:  float 2",
        "matsub":        "Enter datatype then number of matrices, e.g.:  float 2",
        # file-mode operations
        "mean_file":     "Leave blank for all columns, or type a label name, e.g.:  Age",
        "median_file":   "Leave blank for all columns, or type a label name",
        "mode_file":     "Leave blank for all columns, or type a label name",
        "var_file":      "Leave blank for all columns, or type a label name",
        "std_dev_file":  "Leave blank for all columns, or type a label name",
        "min_file":      "Leave blank for all columns, or type a label name",
        "max_file":      "Leave blank for all columns, or type a label name",
        "range_file":    "Leave blank for all columns, or type a label name",
        "zscore_file":   "Enter value then optional label, e.g.:  15 Age",
        "percentile_file":"Enter value then optional label, e.g.:  25 Age",
        "display_file":  "Leave blank to display all, or type a label name",
    }

    def setOp(self, op):
        """Called when user picks an operation from the menu."""
        # If file is loaded, tag the op as a file-mode op for hint lookup
        hint_key = (op + "_file") if self.file_mode else op
        self.current_op.set(op)
        self.hint_label.config(text=self._HINTS.get(hint_key,
                               self._HINTS.get(op, "")))
        self.entry.focus()
    def run(self):
        op   = self.current_op.get()
        text = self.entry.get().strip()

        if op == "(none selected)":
            messagebox.showwarning("No operation", "Please select an operation from the menu first.")
            return
        try:
            if self.file_mode:
                self.run_file_op(op, text)
            else:
                self.run_normal_op(op, text)
        except err.InvalidInstructionTypeError:
            self._show(f"Invalid arguments for '{op}'.\n\n"
                       + self._HINTS.get(op, "Check your input and try again."))
        except err.LabelDoesNotExist:
            self._show("That label does not exist in the loaded file.")
        except ValueError as e:
            self._show(f"Value error: {e}")
        except Exception as e:
            self._show(f"Error: {e}")
    def run_normal_op(self, op, text):
        """Run a standard (non-file) command."""
        raw = f"{op} {text}".strip()
        command = ip.process(raw)
        output = capture_output(ip.identify(command), command)
        self._show(output if output else f"Done (no output for '{op}').")

    def run_file_op(self, op, text):
        """Run a file-mode command against self.loaded_file."""
        if op not in ip.FILE_COMMANDS:
            messagebox.showerror("Unknown operation", f"'{op}' is not supported in file mode.")
            return
        file = self.loaded_file
        command = [op]
        if text:
            command += text.strip().split()

        whole_func, label_func = ip.FILE_COMMANDS[op]
        if op in ["zscore", "percentile"]:
            func = whole_func if len(command) == 2 else label_func
        else:
            func = whole_func if len(command) == 1 else label_func

        output = capture_output(func, file, command)
        self._show(output if output else "Done.")

    def _load_file(self):
        path = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            labels = de.getLabels(path)
            if not labels:
                raise ValueError("No labels found in file.")
        except Exception as e:
            messagebox.showerror("File Error",
                                 f"Could not load file:\n{e}")
            return

        self.loaded_file = path
        self.file_mode   = True
        short = path.split("/")[-1]
        self.file_status.config(
            text=f"{short}  ({len(labels)} columns)", fg="green")
        self._show(f"Loaded: {path}\nColumns: {', '.join(labels)}\n\n"
                   "Use the Basic Data menu or File > Display all to query the data.")

    def closeFile(self):
        if not self.file_mode:
            self._show("No file is currently loaded.")
            return
        self.loaded_file = None
        self.file_mode   = False
        self.file_status.config(text="No file loaded", fg="grey")
        self._show("File closed.")

    def displayFile(self):
        if not self.file_mode:
            messagebox.showwarning("No file", "Please load a CSV file first.")
            return
        try:
            output = capture_output(ip.wholeDisplay, self.loaded_file, ["display"])
            self._show(output)
        except Exception as e:
            self._show(f"Error displaying file: {e}")

    def showHelp(self):
        help_text = (
            "DATA ENGINE — QUICK HELP\n"
            "═══════════════════════════════════════\n\n"
            "NORMAL MODE (no file loaded)\n"
            "  Select an operation from the menu, then type\n"
            "  your numbers into the input box and press Run.\n\n"
            "  mean / median / mode / var / std_dev\n"
            "    Input:  10 20 30 40\n\n"
            "  min / max / range\n"
            "    Input:  5 10 15\n\n"
            "  zscore / percentile\n"
            "    Input:  <value> <data…>  e.g.:  15 10 20 30\n\n"
            "  quicksort / bubblesort / insertionsort\n"
            "    Input:  <int|float> <numbers…>  e.g.:  int 3 1 4 1\n\n"
            "FILE MODE (after loading a CSV)\n"
            "  Load a CSV via File > Load CSV…\n"
            "  Then select any operation from Basic Data.\n"
            "  • Leave input blank  → applies to ALL columns\n"
            "  • Type a label name  → applies to that column only\n"
            "  • zscore / percentile: type the value, then\n"
            "    optionally a label name.\n"
        )
        win = Toplevel(self.master)
        win.title("Help")
        win.geometry("480x480")
        txt = Text(win, wrap=WORD, font=("Consolas", 10),
                   padx=10, pady=10)
        txt.insert(END, help_text)
        txt.config(state=DISABLED)
        txt.pack(fill=BOTH, expand=True)
        Button(win, text="Close", command=win.destroy).pack(pady=6)

if __name__ == "__main__":
    root = Tk()
    app  = Window(root)
    root.mainloop()