import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment

def convert_to_pcm_wav(input_path, output_path):
    """
    Loads any valid audio format (even if misnamed as .wav) 
    and exports it as a clean, uncompressed 16-bit PCM WAV.
    """
    # Load audio file (pydub auto-detects format even if headers/extensions are mismatched)
    audio = AudioSegment.from_file(input_path)

    # Export strictly as uncompressed PCM WAV
    audio.export(output_path, format="wav", parameters=["-acodec", "pcm_s16le"])

class WavConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal WAV / Audio Converter")
        self.root.geometry("480x220")
        self.root.resizable(False, False)

        self.selected_files = []

        # UI Layout
        self.btn_select = tk.Button(root, text="Select Audio Files", command=self.select_files, width=20, height=2)
        self.btn_select.pack(pady=15)

        self.lbl_status = tk.Label(root, text="No files selected", fg="gray")
        self.lbl_status.pack(pady=5)

        self.btn_convert = tk.Button(root, text="Convert to PCM WAV", command=self.convert_files, state=tk.DISABLED, width=20, height=2, bg="#4CAF50", fg="white")
        self.btn_convert.pack(pady=15)

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Select Audio Files",
            filetypes=[("Audio files", "*.wav *.mp3 *.ogg *.flac *.m4a"), ("All files", "*.*")]
        )
        if files:
            self.selected_files = list(files)
            count = len(self.selected_files)
            self.lbl_status.config(text=f"{count} file(s) selected", fg="black")
            self.btn_convert.config(state=tk.NORMAL)
        else:
            self.selected_files = []
            self.lbl_status.config(text="No files selected", fg="gray")
            self.btn_convert.config(state=tk.DISABLED)

    def convert_files(self):
        if not self.selected_files:
            return

        success_count = 0
        error_count = 0

        for file_path in self.selected_files:
            dir_name, file_name = os.path.split(file_path)
            name_no_ext, _ = os.path.splitext(file_name)
            
            # Remove existing suffix if re-converting
            if name_no_ext.endswith("_24bit") or name_no_ext.endswith("_pcm"):
                name_no_ext = name_no_ext.rsplit('_', 1)[0]

            output_path = os.path.join(dir_name, f"{name_no_ext}_pcm.wav")

            try:
                convert_to_pcm_wav(file_path, output_path)
                success_count += 1
            except Exception as e:
                print(f"Error converting {file_name}: {e}")
                error_count += 1

        if error_count == 0:
            messagebox.showinfo("Success", f"Successfully converted {success_count} file(s) to PCM WAV!")
        else:
            messagebox.showwarning("Finished with Errors", f"Converted: {success_count}\nFailed: {error_count}\n\nMake sure FFmpeg is installed.")

        self.selected_files = []
        self.lbl_status.config(text="No files selected", fg="gray")
        self.btn_convert.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = WavConverterGUI(root)
    root.mainloop()