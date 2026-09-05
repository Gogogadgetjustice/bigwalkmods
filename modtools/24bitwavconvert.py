import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment

def convert_audio(input_path, output_path, target_format):
    """
    Loads any valid audio format and exports it to the chosen target format.
    Applies 16-bit PCM properties only if exporting to WAV or AIFF.
    """
    audio = AudioSegment.from_file(input_path)
    
    # Core formats mapping for pydub's exporter
    fmt = target_format.lower()
    
    if fmt in ["wav", "aiff"]:
        # Ensure clean, uncompressed 16-bit PCM for WAV/AIFF container environments
        audio.export(output_path, format=fmt, parameters=["-acodec", "pcm_s16le"])
    else:
        # Standard compressed export for MP3, OGG, FLAC, etc.
        audio.export(output_path, format=fmt)

class UniversalAudioConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Audio Converter")
        self.root.geometry("520x350")  # Resized slightly to cleanly hold the format selector
        self.root.resizable(False, False)

        self.selected_files = []
        self.output_dir = ""
        
        # Available export target formats
        self.formats_list = ["WAV", "MP3", "OGG", "AIFF", "FLAC"]
        self.target_format_var = tk.StringVar(root)
        self.target_format_var.set(self.formats_list[0]) # Default to WAV

        # UI Layout - File Selection
        self.btn_select = tk.Button(root, text="Select Audio Files", command=self.select_files, width=20, height=2)
        self.btn_select.pack(pady=(20, 5))

        self.lbl_status = tk.Label(root, text="No files selected", fg="gray")
        self.lbl_status.pack(pady=5)

        # UI Layout - Output Format Target Dropdown
        self.format_frame = tk.Frame(root)
        self.format_frame.pack(pady=5)
        
        self.lbl_format_prompt = tk.Label(self.format_frame, text="Convert To Target Format: ")
        self.lbl_format_prompt.pack(side=tk.LEFT)
        
        self.opt_format = tk.OptionMenu(self.format_frame, self.target_format_var, *self.formats_list)
        self.opt_format.config(width=10)
        self.opt_format.pack(side=tk.LEFT)

        # UI Layout - Output Folder Selection
        self.folder_frame = tk.Frame(root)
        self.folder_frame.pack(pady=15, fill=tk.X, padx=20)
        
        self.btn_folder = tk.Button(self.folder_frame, text="Set Output Folder", command=self.select_output_folder, width=15)
        self.btn_folder.pack(side=tk.LEFT, padx=(0, 10))
        
        self.lbl_folder = tk.Label(self.folder_frame, text="Same folder as original files", fg="gray", anchor="w")
        self.lbl_folder.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # UI Layout - Convert Button
        self.btn_convert = tk.Button(root, text="Convert Files", command=self.convert_files, state=tk.DISABLED, width=20, height=2, bg="#4CAF50", fg="white")
        self.btn_convert.pack(pady=15)

    def select_files(self):
        file_types = [
            ("Audio files", "*.wav *.mp3 *.ogg *.aiff *.aif *.flac *.m4a *.aac *.wma"),
            ("MP3 Files", "*.mp3"),
            ("OGG Files", "*.ogg"),
            ("AIFF Files", "*.aiff *.aif"),
            ("WAV Files", "*.wav"),
            ("FLAC Files", "*.flac"),
            ("All files", "*.*")
        ]

        files = filedialog.askopenfilenames(title="Select Audio Files", filetypes=file_types)
        if files:
            self.selected_files = list(files)
            count = len(self.selected_files)
            self.lbl_status.config(text=f"{count} file(s) selected", fg="black")
            self.btn_convert.config(state=tk.NORMAL)
        else:
            self.selected_files = []
            self.lbl_status.config(text="No files selected", fg="gray")
            self.btn_convert.config(state=tk.DISABLED)

    def select_output_folder(self):
        directory = filedialog.askdirectory(title="Select Destination Folder")
        if directory:
            self.output_dir = directory
            display_path = directory if len(directory) <= 45 else f"...{directory[-42:]}"
            self.lbl_folder.config(text=display_path, fg="black")
        else:
            self.output_dir = ""
            self.lbl_folder.config(text="Same folder as original files", fg="gray")

    def convert_files(self):
        if not self.selected_files:
            return

        success_count = 0
        error_count = 0
        target_ext = self.target_format_var.get().lower()

        for file_path in self.selected_files:
            dir_name, file_name = os.path.split(file_path)
            name_no_ext, _ = os.path.splitext(file_name)
            
            # Clean off any old output tags if re-converting files
            if name_no_ext.endswith("_24bit") or name_no_ext.endswith("_pcm") or name_no_ext.endswith("_converted"):
                name_no_ext = name_no_ext.rsplit('_', 1)[0]

            # Route to target folder or fallback to the source directory
            target_dir = self.output_dir if self.output_dir else dir_name
            output_path = os.path.join(target_dir, f"{name_no_ext}_converted.{target_ext}")

            try:
                convert_audio(file_path, output_path, target_ext)
                success_count += 1
            except Exception as e:
                print(f"Error converting {file_name}: {e}")
                error_count += 1

        if error_count == 0:
            messagebox.showinfo("Success", f"Successfully converted {success_count} file(s) to {target_ext.upper()}!")
        else:
            messagebox.showwarning("Finished with Errors", f"Converted: {success_count}\nFailed: {error_count}\n\nMake sure FFmpeg is installed and matches your target format settings.")

        # Clear active selection queue
        self.selected_files = []
        self.lbl_status.config(text="No files selected", fg="gray")
        self.btn_convert.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversalAudioConverterGUI(root)
    root.mainloop()
