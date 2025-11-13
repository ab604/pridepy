# Analysis of PRIDE Dataset PXD013649
## Immunopeptidomics Study: Lung Tumor Sample Identification

---

## Summary

Dataset **PXD013649** is a ProteomeXchange/PRIDE immunopeptidomics dataset containing **two pairs of lung cancer samples with matched normal tissues** and seven patient-derived melanoma cell lines.

---

## Publication Information

**Title:** Integrated proteogenomic deep sequencing and analytics accurately identify non-canonical peptides in tumor immunopeptidomes

**Authors:** Chong C, Müller M, Pak H, Harnett D, Huber F, Grun D, Leleu M, Auger A, Arnaud M, Stevenson BJ, Michaux J, Bilic I, Hirsekorn A, Calviello L, Simó-Riudalbas L, Planet E, Lubiński J, Bryśkiewicz M, Wiznerowicz M, Xenarios I, Zhang L, Trono D, Harari A, Ohler U, Coukos G, Bassani-Sternberg M

**Journal:** Nature Communications
**Publication Date:** March 10, 2020
**Volume/Issue:** 11(1):1293
**DOI:** 10.1038/s41467-020-14968-9
**PubMed ID:** 32157095
**PMC ID:** PMC7064602

**Access Publication:**
- Nature Communications: https://www.nature.com/articles/s41467-020-14968-9
- PubMed Central: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7064602/
- PubMed: https://pubmed.ncbi.nlm.nih.gov/32157095/

---

## Abstract

The study addresses challenges in identifying tumor human leukocyte antigen (HLA) bound peptides that can mediate T cell-based tumor rejection. The authors note that non-canonical tumor-specific HLA peptides derived from annotated non-coding regions could elicit anti-tumor immune responses, but sensitive and accurate mass spectrometry (MS)-based proteogenomics approaches are required to robustly identify these non-canonical peptides.

The researchers present an MS-based analytical approach that characterizes the non-canonical tumor HLA peptide repertoire by incorporating:
- Whole exome sequencing
- Bulk and single-cell transcriptomics
- Ribosome profiling
- Two MS/MS search tools in combination

This approach results in the accurate identification of hundreds of shared and tumor-specific non-canonical HLA peptides, including an immunogenic peptide derived from an open reading frame downstream of the melanoma stem cell marker gene ABCB5.

---

## Sample Composition

### Lung Cancer Samples
- **2 pairs** of lung cancer samples
  - Lung tumor tissue (Patient 1)
  - Matched normal lung tissue (Patient 1)
  - Lung tumor tissue (Patient 2)
  - Matched normal lung tissue (Patient 2)

### Melanoma Samples
- **7 patient-derived melanoma cell lines**

---

## Experimental Approach

### 1. Genomic Profiling
- Whole exome sequencing to identify mutations

### 2. Transcriptomic Analysis
- Bulk transcriptome sequencing
- Single-cell RNA-Seq (scRNA-Seq)
- Whole translatome data

### 3. Ribosome Profiling
- Assessment of active translation

### 4. Mass Spectrometry
- Immunopeptidomics for HLA peptide identification
- MS-based analytical approach using NewAnce
- Combination of two MS/MS search tools
- Group-specific FDR calculations

---

## Key Findings

1. Accurate identification of hundreds of shared and tumor-specific non-canonical HLA peptides
2. Discovery of an immunogenic peptide derived from an open reading frame downstream of the melanoma stem cell marker gene ABCB5
3. Demonstrated improved sensitivity and accuracy in identifying non-canonical peptides through integrated proteogenomics
4. Validated approach for characterizing the non-canonical tumor HLA peptide repertoire

---

## Dataset Access

**ProteomeXchange ID:** PXD013649
**Repository:** PRIDE Archive
**URL:** https://www.ebi.ac.uk/pride/archive/projects/PXD013649

**Dataset Contents:**
- Raw MS data files (.raw format)
- NewAnce analytical tool (executable jar file)
- Search results and peptide identifications

---

## Lung Tumor Sample Identification

Based on the publication, the dataset contains:

### Expected File Patterns for Lung Samples:
When accessing the raw files, look for naming patterns that might include:
- Patient identifiers (e.g., PT1, PT2, Patient1, Patient2)
- Tissue type indicators:
  - Tumor: "T", "Tumor", "Cancer", "Malignant"
  - Normal: "N", "Normal", "Healthy", "Control", "Matched"
- Organ identifier: "Lung", "L", "Pulmonary"

### Sample Pairs:
Each lung cancer patient should have:
1. **Tumor sample**: Lung cancer/tumor tissue
2. **Normal sample**: Adjacent normal lung tissue (matched control)

---

## Technical Notes

### API Access Issues
During this analysis (November 2025), direct access to the PRIDE API was blocked (HTTP 403 errors). This affected:
- Direct metadata retrieval via PRIDE REST API v2 and v3
- File listing through API endpoints
- ProteomeXchange web interface access

### Alternative Approaches Used:
1. Web search to find publication information
2. Literature review to identify sample composition
3. Analysis of publication methods sections

### When API Access is Available:
The included `analyze_pxd013649.py` script can be used to:
- Retrieve full project metadata
- List all .raw files
- Automatically categorize files by keywords
- Export results to JSON format

---

## Future Analysis Steps

Once PRIDE API access is restored, you can:

1. **Download File List:**
   ```bash
   python3 analyze_pxd013649.py PXD013649
   ```

2. **Identify Specific Lung Tumor Files:**
   - Review the categorized output
   - Look for files matching lung tumor patterns
   - Download specific .raw files for analysis

3. **Data Analysis:**
   - Re-process immunopeptidomics data
   - Compare tumor vs. normal lung samples
   - Identify lung-specific neoantigens
   - Correlate with genomic/transcriptomic data

---

## Related Research

This dataset has been cited in multiple immunopeptidomics studies including:
- DIA (Data-Independent Acquisition) immunopeptidomics workflows
- Multi-HLA spectral library development
- Neoantigen discovery pipelines
- Cancer immunotherapy research

---

## Contact Information

**Corresponding Author:** Michal Bassani-Sternberg
**Institution:** University of Lausanne (UNIL) - CHUV
**Research Focus:** Immunopeptidomics, tumor antigens, mass spectrometry

---

## Software Tools

**NewAnce:** Analytical tool for non-canonical element identification
- Combines two MS/MS search tools
- Group-specific FDR calculations
- Available in PRIDE dataset PXD013649

---

## Summary for Your Analysis

**Lung Tumor Sample Count:** 2 pairs (4 samples total)
- 2 lung tumor samples
- 2 matched normal lung tissue samples

**Total Samples in Dataset:**
- 4 lung samples (2 tumor + 2 normal)
- 7 melanoma cell lines
- **Total: 11 samples**

This dataset is valuable for studying lung cancer immunopeptidomes, identifying tumor-specific antigens, and comparing tumor vs. normal tissue HLA peptide presentations in lung cancer patients.
