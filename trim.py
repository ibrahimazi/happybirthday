from pydub import AudioSegment

def trim_audio(input_file, output_file, trim_duration=20000):
    # Load audio file
    audio = AudioSegment.from_file(input_file)
    
    # Potong 20 detik pertama
    trimmed_audio = audio[trim_duration:]
    
    # Simpan hasil
    trimmed_audio.export(output_file, format="mp3")
    print(f"Audio berhasil dipotong dan disimpan sebagai {output_file}")

# Contoh penggunaan
trim_audio("input.mp3", "aboutyoutrim.mp3")