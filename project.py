#!/usr/bin/env python3

# Sequence Trimming and Exclusion Script
# Processes a FASTA file to:
# - Remove sequences from an exclude list
# - Trim sequences at specific spans
# - Remove trailing/leading Ns
# - Output 3 versions of cleaned FASTA files

THRESHOLD = 200

# File paths
fasta_file_path = "Scaffolds.fasta"
exclude_file_path = "exclude_list.tab"
trim_file_path = "trim_list.tab"

output1_path = "output1.fasta"  # Only excludes removed
output2_path = "output2.fasta"  # Excludes removed + cleaned (not 'mitochondrion-not_cleaned')
output3_path = "output3.fasta"  # Excludes removed + all trimmed

# Step 1: Load Exclude List
exclude_list = []
with open(exclude_file_path, 'r') as file:
    for line in file:
        exclude_list.append(line.strip().split('\t')[0])

# Step 2: Load Trim Info
trim_dict = {}
with open(trim_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 4:
            name = parts[0]
            length = int(parts[1])
            spans = parts[2].split(',') if parts[2] else []
            source = parts[3]
            trim_dict[name] = {'length': length, 'span': spans, 'source': source}

# Step 3: Load FASTA Sequences
sequences = {}
with open(fasta_file_path, 'r') as file:
    current_id = None
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:].split()[0]
            sequences[current_id] = ''
        else:
            sequences[current_id] += line.upper()

# Step 4: Remove Excluded Sequences
filtered_sequences = {}
for name, seq in sequences.items():
    if name not in exclude_list:
        filtered_sequences[name] = seq

# Step 5: Output 1 (Exclude Only)
with open(output1_path, 'w') as out1:
    for name, seq in filtered_sequences.items():
        if len(seq) >= THRESHOLD:
            out1.write(f'>{name}\n{seq}\n')

# Step 6: Output 2 & 3 (Trimming)
output2 = {}
output3 = {}

for name, seq in filtered_sequences.items():
    trim_info = trim_dict.get(name)

    # Output 2: Trim only if not 'mitochondrion-not_cleaned'
    if trim_info and trim_info['span'] and trim_info['span'][0] != 'mitochondrion-not_cleaned':
        spans = sorted([tuple(map(int, s.split('..'))) for s in trim_info['span']])
        last_end = 0
        frag_count = 1
        for start, end in spans:
            start -= 1
            if last_end < start:
                fragment = seq[last_end:start].lstrip('N').rstrip('N')
                if len(fragment) >= THRESHOLD:
                    output2[f"{name}_{frag_count}"] = fragment
                    frag_count += 1
            last_end = end
        if last_end < len(seq):
            fragment = seq[last_end:].lstrip('N').rstrip('N')
            if len(fragment) >= THRESHOLD:
                output2[f"{name}_{frag_count}"] = fragment
    else:
        cleaned = seq.lstrip('N').rstrip('N')
        output2[name] = cleaned

    # Output 3: Always trim if spans exist
    if trim_info and trim_info['span']:
        spans = sorted([tuple(map(int, s.split('..'))) for s in trim_info['span']])
        last_end = 0
        frag_count = 1
        for start, end in spans:
            start -= 1
            if last_end < start:
                fragment = seq[last_end:start].lstrip('N').rstrip('N')
                if len(fragment) >= THRESHOLD:
                    output3[f"{name}_{frag_count}"] = fragment
                    frag_count += 1
            last_end = end
        if last_end < len(seq):
            fragment = seq[last_end:].lstrip('N').rstrip('N')
            if len(fragment) >= THRESHOLD:
                output3[f"{name}_{frag_count}"] = fragment
    else:
        cleaned = seq.lstrip('N').rstrip('N')
        output3[name] = cleaned

# Step 7: Write Output 2
with open(output2_path, 'w') as out2:
    for name, seq in output2.items():
        out2.write(f'>{name}\n{seq}\n')

# Step 8: Write Output 3
with open(output3_path, 'w') as out3:
    for name, seq in output3.items():
        out3.write(f'>{name}\n{seq}\n')
