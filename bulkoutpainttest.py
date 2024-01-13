# apply asyncoutpainttest to all folders in a directory
# save results in a text file

import os
import sys
import subprocess

def main():
    if len(sys.argv) != 3:
        print("usage: python bulkoutpainttest.py <folder> <output>")
        return

    folder = sys.argv[1]
    output = sys.argv[2]

    # create output file
    f = open(output, "w")

    # for each folder in directory
    for filename in os.listdir(folder):
        # run asyncoutpainttest.py
        p = subprocess.Popen(["python", "asyncoutpainttest.py", os.path.join(folder, filename)], stdout=subprocess.PIPE)
        out, err = p.communicate()
        # write results to file
        f.write(filename + "\n")
        f.write(out.decode("utf-8") + "\n")

    f.close()

if __name__ == "__main__":
    main()
