import os
import subprocess
import csv

def m4a_to_wav():
    # Ensure the output folder exists, or create it if it doesn't
    src_folder = '/Users/apple/Desktop/coquiTTS/fine-tune_dataset/new_m4as'
    dst_folder = '/Users/apple/Desktop/Practicum/self-collect-dataset-2/dev-clean/14/7'
    test_dst_folder = '/Users/apple/Desktop/Practicum/self-collect-dataset-2/test-clean/14/7'
    os.makedirs(dst_folder, exist_ok=True)
    os.makedirs(test_dst_folder, exist_ok=True)
    # Loop through all files in the input folder
    for filename in os.listdir(src_folder):
        if filename.endswith('.aifc'):
            input_file = os.path.join(src_folder, filename)
            file_index = os.path.splitext(filename)[0]
            if int(file_index) in [37, 38, 39, 40]:
                output_file = os.path.join(test_dst_folder, f'14_7_{file_index}.wav')
            else:
                output_file = os.path.join(dst_folder, f'14_7_{file_index}.wav')
            # Use subprocess to run FFmpeg to convert the file
            cmd = ['ffmpeg', '-i', input_file, '-acodec', 'pcm_s16le', '-ar', '24000', output_file]
            try:
                subprocess.run(cmd, check=True)
                print(f"Converted {input_file} to {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {input_file}: {e}")

def create_txt_transcriptions():
    # Open the input text file with transcriptions
    input_file = "/Users/apple/Desktop/coquiTTS/fine-tune_dataset/new_m4as/new_train.txt"
    dest_folder = '/Users/apple/Desktop/Practicum/self-collect-dataset-2/dev-clean/14/7'
    os.makedirs(dest_folder, exist_ok=True)
    test_folder = '/Users/apple/Desktop/Practicum/self-collect-dataset-2/test-clean/14/7'
    os.makedirs(test_folder, exist_ok=True)
    # Open the file for reading
    transcriptions = []
    test_transcriptions = []
    with open(input_file, "r", encoding="utf-8") as file:
        # Read each line
        for line_number, line in enumerate(file, start=1):
            line = line.split('|')[2]
            line = line[:len(line)-1]
            if(line_number < 37):
                transcriptions.append((f'14_7_{line_number}', line, line, None, None, None, 20.0))
                # Clean and create a filename for the new text file
                filename = f"{dest_folder}/14_7_{line_number}.original.txt"
                with open(filename, "w", encoding="utf-8") as output_file:
                    output_file.write(line)
                filename = f"{dest_folder}/14_7_{line_number}.normalized.txt"
                with open(filename, "w", encoding='utf-8') as output_file:
                    output_file.write(line)
            else:
                test_transcriptions.append((f'14_7_{line_number}', line, line, None, None, None, 20.0))
                filename = f"{test_folder}/14_7_{line_number}.original.txt"
                with open(filename, "w", encoding="utf-8") as output_file:
                    output_file.write(line)
                filename = f"{test_folder}/14_7_{line_number}.normalized.txt"
                with open(filename, "w", encoding="utf-8") as output_file:
                    output_file.write(line)

    print(transcriptions)
    # Path to the TSV file
    tsv_file = "/Users/apple/Desktop/Practicum/self-collect-dataset-2/dev-clean/14/7/14_7.trans.tsv"
    # Open the TSV file for writing
    with open(tsv_file, "w", newline="", encoding="utf-8") as file:
        for t in transcriptions:
            writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            row = f"{t[0]}\t{t[1]}\t{t[2]}"
            writer.writerow(row.split("\t"))
    tsv_file = "/Users/apple/Desktop/Practicum/self-collect-dataset-2/dev-clean/14/7/14_7.book.tsv"
    # Open the TSV file for writing
    with open(tsv_file, "w", newline="", encoding="utf-8") as file:
        for t in transcriptions:
            writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            row = f"{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t{t[4]}\t{t[5]}\t{t[6]}"
            writer.writerow(row.split("\t"))
    # Path to the TSV file
    tsv_file = "/Users/apple/Desktop/Practicum/self-collect-dataset-2/test-clean/14/7/14_7.trans.tsv"
    # Open the TSV file for writing
    with open(tsv_file, "w", newline="", encoding="utf-8") as file:
        for t in test_transcriptions:
            writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            row = f"{t[0]}\t{t[1]}\t{t[2]}"
            writer.writerow(row.split("\t"))
    tsv_file = "/Users/apple/Desktop/Practicum/self-collect-dataset-2/test-clean/14/7/14_7.book.tsv"
    # Open the TSV file for writing
    with open(tsv_file, "w", newline="", encoding="utf-8") as file:
        for t in test_transcriptions:
            writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
            row = f"{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t{t[4]}\t{t[5]}\t{t[6]}"
            writer.writerow(row.split("\t"))


if __name__ == '__main__':
    #m4a_to_wav()
    create_txt_transcriptions()

            

