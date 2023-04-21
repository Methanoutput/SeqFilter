# SeqFilter

## About

A python script that will filter sequences from any sequence file based on an input list given by the user. It facilitates complex and long header lines and can alphabetically order your Gene ID's.

## Usage

To use the script, run the following command with the required arguments:

```sh
python seqfilter.py -d DATABASE -l LIST -s SORT -n NAME
```

### Arguments

- `-d DATABASE`, `--database DATABASE`: Requires a file containing your sequences.
- `-l LIST`, `--list LIST`: Requires a txt. file containing the sequences you want to write in a new file.
- `-s SORT`, `--sort SORT`: Your output file will be sorted alphabetically if you set the Value to "T".
- `-n NAME`, `--name NAME`: Requires a string that represents the output file name.
