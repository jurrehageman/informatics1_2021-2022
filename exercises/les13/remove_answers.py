import sys

infile_name = sys.argv[1]
outfile_name = sys.argv[2]
if infile_name == outfile_name:
    print("Warning! filenames are identical")
    sys.exit()
infile_obj = open(infile_name)
outfile_obj = open(outfile_name, "w")

flag = True

for num, line in enumerate(infile_obj):
    if "###ANSWER###" in line:
        flag = False
    if flag:
        outfile_obj.write(line)
    if "###END ANSWER###" in line:
        flag = True
        outfile_obj.write('    "\\n"\n')

outfile_obj.close()
print("Done")