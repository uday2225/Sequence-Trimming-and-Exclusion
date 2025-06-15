# 🧬 Sequence Trimming and Exclusion

This project automates the preprocessing of raw DNA sequence data for submission to genomic databases. It handles large-scale FASTA files, removes unwanted sequences, trims defined spans, and outputs only high-quality sequence fragments suitable for downstream analysis.

Developed as part of a bioinformatics coursework assignment, this script demonstrates real-world skills in sequence curation, data parsing, and algorithmic filtering.

---

## 📌 Project Highlights

- ✅ Removes excluded sequences based on metadata
- ✂️ Trims sequence spans (1-based inclusive indexing)
- 🧹 Cleans `N`s from the *ends* of trimmed fragments only
- 🔄 Splits trimmed sequences into separate contigs
- 🧪 Applies a minimum length threshold (default 200 bp)
- 📂 Works with realistic input files (18,000+ bp per sequence)
- 🧠 No external libraries required

---

## 📁 Repository Structure

| File | Description |
|------|-------------|
| `project.py` | Main Python script (beginner-friendly, procedural style) |
| `Scaffolds_demo.fasta` | ✅ **Demo FASTA file** (trimmed down version of the original due to size limits) |
| `exclude_list.tab` | List of sequences to exclude |
| `trim_list.tab` | Span definitions for trimming |
| `output1.fasta` | Output after excluding sequences only |
| `output2.fasta` | Trimmed output excluding `"mitochondrion-not_cleaned"` |
| `output3.fasta` | Trimmed output including all trimming spans |
| `README.md` | You're reading it! |

---

## 📥 Original Input File Notice

Due to file size restrictions and licensing, the full `Scaffolds.fasta` file (approx. 600MB) used in the original assignment is not uploaded to this repository.  
Instead, this repository includes `Scaffolds_demo.fasta`, a representative subset of the original data (~24MB), designed to preserve the real structure and complexity for demonstration purposes.

---

## 👨‍💻 Author

**Uday Kiran Gogineni** – Clustering & Modeling Lead  
_M.S. in Bioinformatics_  
[LinkedIn](https://www.linkedin.com/in/udaykiran01)

---

## 📄 License

This project is licensed under the MIT License.

## 🚀 How to Run

```bash
# Run in Python 3
python project.py



