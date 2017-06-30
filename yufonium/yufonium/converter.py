import subprocess


# For now, we will use the libav's avconv called through subprocess.
# Some kind of library or C wrapping library should be use later

def convert(input_path):
    filename = input_path.split("/")[-1]
    output_ext = "mp3"
    # This is very ugly. Is there a better way?
    output_path = "/".join(input_path.split("/")[:-1] + ["".join(filename.split(".")[:-1] + [".", output_ext])])
    print(subprocess.check_output(['/usr/local/bin/avconv',
                                   '-i', input_path,
                                   output_path]).decode("utf-8"))
