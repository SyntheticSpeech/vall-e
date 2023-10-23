import os
import subprocess
import csv

def m4a_to_wav(ar):
    # Ensure the output folder exists, or create it if it doesn't
    src_folder = '/Users/apple/Desktop/coquiTTS/fine-tune_dataset/m4as'
    dst_folder = '/Users/apple/Desktop/Practicum/self-collect-dataset/dev-clean/14/7'
    os.makedirs(dst_folder, exist_ok=True)
    # Loop through all files in the input folder
    for filename in os.listdir(src_folder):
        if filename.endswith('.m4a'):
            input_file = os.path.join(src_folder, filename)
            output_file = os.path.join(dst_folder, os.path.splitext(filename)[0] + '.wav')
            # Use subprocess to run FFmpeg to convert the file
            cmd = ['ffmpeg', '-i', input_file, '-acodec', 'pcm_s16le', '-ar', ar, output_file]
            try:
                subprocess.run(cmd, check=True)
                print(f"Converted {input_file} to {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {input_file}: {e}")

def create_txt_transcriptions():
    # Open the input text file with transcriptions
    input_file = "/Users/apple/Desktop/coquiTTS/fine-tune_dataset/train.txt"
    dest_folder = '/Users/apple/Desktop/Practicum/self-collect-dataset/dev-clean/14/7'
    os.makedirs(dest_folder, exist_ok=True)
    # Open the file for reading
    transcriptions = []
    with open(input_file, "r", encoding="utf-8") as file:
        # Read each line
        for line_number, line in enumerate(file, start=1):
            line = line.split('|')[2]
            line = line[:len(line)-1]
            transcriptions.append((f'14_7_{line_number}', line, line, True, 23.61, 25.17, 29.87104))
            # Clean and create a filename for the new text file
            filename = f"{dest_folder}/{line_number}.original.txt"
            # Open the new text file and write the transcription
            with open(filename, "w") as output_file:
                output_file.write(line)
            filename = f"{dest_folder}/{line_number}.normalized.txt"
            # Open the new text file and write the transcription
            with open(filename, "w") as output_file:
                output_file.write(line)
            print(f"Transcription {line_number} saved as {filename}")
    print(transcriptions)
    # Path to the TSV file
    tsv_file = "/Users/apple/Desktop/Practicum/self-collect-dataset/dev-clean/14/7/14_7.trans.tsv"
    # Open the TSV file for writing
    with open(tsv_file, "w", newline="", encoding="utf-8") as file:
        for index in range(len(transcriptions)):
            writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)

            # Write the transcriptions to the TSV file
            t = transcriptions[index]
            row = f"{t[0]}\t{t[1]}\t{t[2]}"
            writer.writerow(row.split("\t"))
    tsv_file = "/Users/apple/Desktop/Practicum/self-collect-dataset/dev-clean/14/7/14_7.book.tsv"
    # Open the TSV file for writing
    with open(tsv_file, "w", newline="", encoding="utf-8") as file:
        for index in range(len(transcriptions)):
            writer = csv.writer(file, delimiter='\t', quoting=csv.QUOTE_MINIMAL)

            # Write the transcriptions to the TSV file
            t = transcriptions[index]
            row = f"{t[0]}\t{t[1]}\t{t[2]}\t{t[3]}\t{t[4]}\t{t[5]}"
            writer.writerow(row.split("\t"))


if __name__ == '__main__':
    m4a_to_wav('24000')
    # create_txt_transcriptions()

            

