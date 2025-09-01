#!/usr/bin/env python3

import os
import argparse
import csv
import re
from collections import defaultdict

def generate_samplesheet(fastq_dirs, output_file):
    """
    Parses one or more directories of paired-end FASTQ files to create a single samplesheet.

    Args:
        fastq_dirs (list of str): List of paths to directories containing .fastq.gz files.
        output_file (str): Name of the output CSV file.
    """
    sample_pattern = re.compile(r'(.+)_R1_001\.fastq\.gz')
    samples = defaultdict(list)

    # Iterate over all input directories
    for fastq_dir in fastq_dirs:
        if not os.path.isdir(fastq_dir):
            print(f"Warning: '{fastq_dir}' is not a valid directory. Skipping.")
            continue

        for filename in sorted(os.listdir(fastq_dir)):
            if '_R1_001.fastq.gz' in filename:
                match = sample_pattern.match(filename)
                if match:
                    sample_name = match.group(1)
                    r1_path = os.path.join(fastq_dir, filename)
                    r2_filename = filename.replace('_R1_001.fastq.gz', '_R2_001.fastq.gz')
                    r2_path = os.path.join(fastq_dir, r2_filename)
                    if os.path.exists(r2_path):
                        samples[sample_name].append((r1_path, r2_path))
                    else:
                        print(f"Warning: R2 file not found for {filename}. Skipping this pair.")

    if not samples:
        print("Error: No FASTQ pairs found in the provided directories.")
        return

    # Write to CSV
    try:
        with open(output_file, 'w', newline='') as f_out:
            writer = csv.writer(f_out)
            writer.writerow(['sample', 'fastq_1', 'fastq_2', 'strandedness'])
            for sample_name, pairs in samples.items():
                for r1_path, r2_path in pairs:
                    writer.writerow([sample_name, r1_path, r2_path, 'auto'])

        print(f"✅ Samplesheet successfully created at: {output_file}")

    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate a samplesheet CSV from one or more directories of FASTQ files."
    )
    parser.add_argument(
        '-i', '--input_dirs',
        nargs='+',
        required=True,
        help="Paths to one or more directories containing FASTQ files (supports multiple directories)."
    )
    parser.add_argument(
        '-o', '--output_file',
        default='samplesheet.csv',
        help="Name for the output CSV file (default: samplesheet.csv)."
    )

    args = parser.parse_args()
    generate_samplesheet(args.input_dirs, args.output_file)


if __name__ == '__main__':
    main()

