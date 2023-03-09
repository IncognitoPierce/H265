import os
import ffmpeg

def clear():
    # fungsi untuk membersihkan layar konsol
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Menampilkan menu bahasa
    while True:
        clear()
        print("Pilih bahasa / Choose language:")
        print("1. Bahasa Indonesia")
        print("2. English")
        print("3. Keluar / Exit")

        # Meminta pengguna untuk memilih bahasa
        lang_choice = input("Masukkan pilihan bahasa / Enter language choice: ")

        # Pemeriksaan pilihan bahasa pengguna
        if lang_choice == '1':
            clear()
            print("Program Konversi Video H.264 ke H.265\n")
            input_text = "Masukkan nama file input (H.264): "
            output_text = "Masukkan nama file output (H.265): "
            done_text = "\nKonversi video selesai!"
            exit_text = "Tekan ENTER untuk keluar."
            break
        elif lang_choice == '2':
            clear()
            print("H.264 to H.265 Video Conversion Program\n")
            input_text = "Enter input file name (H.264): "
            output_text = "Enter output file name (H.265): "
            done_text = "\nVideo conversion completed!"
            exit_text = "Press ENTER to exit."
            break
        elif lang_choice == '3':
            return
        else:
            print("Pilihan bahasa tidak valid / Invalid language choice")
            input("Tekan ENTER untuk melanjutkan / Press ENTER to continue")

    input_file = input(input_text)
    output_file = input(output_text)

    # Membuat objek konversi menggunakan ffmpeg
    stream = ffmpeg.input(input_file)

    # Mengkonversi video menggunakan format H.265
    stream = ffmpeg.output(stream, output_file, vcodec='libx265')

    # Menjalankan konversi video
    ffmpeg.run(stream)

    print(done_text)
    input(exit_text)

if __name__ == '__main__':
    main()
