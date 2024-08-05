# joining all preamble file into a combined preamble.
import os
import re

# Define the base directory
base_dir = "/home/veritas/latex-templates"

# Define the input file (basic.tex)
input_file = os.path.join(base_dir, "templates/article/basic.tex")

# Define the output file
output_file = "combined-preamble.tex"

# Regular expression to match \input{filename}
input_pattern = re.compile(r'\\input\{(.+?)\}')

# Set to keep track of already included files to avoid duplicates
included_files = set()

def process_file(file_path, outfile):
    """Recursively process a LaTeX file to include its content."""
    with open(file_path, 'r') as infile:
        for line in infile:
            match = input_pattern.search(line)
            if match:
                nested_file = match.group(1)
                nested_file_path = os.path.join(base_dir, nested_file)
                if nested_file_path not in included_files:
                    included_files.add(nested_file_path)
                    outfile.write(f"%%%%% {nested_file}\n")
                    process_file(nested_file_path, outfile)
                    outfile.write("\n" * 2)
                    outfile.write("%" + "=" * 50 + "%")
                    outfile.write("\n" * 2)
                    print(f"Contents in {nested_file} written to {output_file}.\n")
            else:
                outfile.write(line)

# Open the output file and process the main input file
with open(output_file, 'w') as outfile:
    process_file(input_file, outfile)

print(f"Combined preamble written to {output_file}")
