#!/usr/bin/env python3
"""
Analyze PRIDE dataset PXD013649 to identify lung tumor samples
"""
import json
import re
from pridepy.project.project import Project

def main():
    # Initialize the Project class
    project = Project()

    # Dataset accession
    import sys
    accession = sys.argv[1] if len(sys.argv) > 1 else "PXD013649"

    print(f"Analyzing PRIDE dataset: {accession}")
    print("=" * 80)

    # 1. Get project metadata
    print("\n1. Fetching project metadata...")
    try:
        metadata = project.get_by_accession(accession)

        # Display key metadata
        print(f"\nTitle: {metadata.get('title', 'N/A')}")
        print(f"\nDescription:\n{metadata.get('projectDescription', 'N/A')}")
        print(f"\nSample Processing Protocol:\n{metadata.get('sampleProcessingProtocol', 'N/A')}")
        print(f"\nData Processing Protocol:\n{metadata.get('dataProcessingProtocol', 'N/A')}")

        # Check for references/publications
        references = metadata.get('references', [])
        if references:
            print(f"\nReferences:")
            for ref in references:
                print(f"  - DOI: {ref.get('doi', 'N/A')}")
                print(f"    PubMed ID: {ref.get('pubmedId', 'N/A')}")
                print(f"    Reference: {ref.get('referenceLine', 'N/A')}")

        # Get publication DOI for later
        pub_doi = None
        if references and len(references) > 0:
            pub_doi = references[0].get('doi')

    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return

    # 2. Get all files
    print("\n" + "=" * 80)
    print("\n2. Fetching all files...")
    try:
        files = project.get_files_by_accession(accession)

        if not files:
            print("No files found!")
            return

        print(f"\nTotal files: {len(files)}")

    except Exception as e:
        print(f"Error fetching files: {e}")
        return

    # 3. Filter for .raw files
    print("\n" + "=" * 80)
    print("\n3. Filtering for .raw files...")
    raw_files = [f for f in files if f.get('fileName', '').lower().endswith('.raw')]
    print(f"\nFound {len(raw_files)} .raw files")

    # 4. Analyze filenames for patterns
    print("\n" + "=" * 80)
    print("\n4. Analyzing filenames for patterns...")

    # Keywords to search for
    keywords = {
        'tumor': ['tumor', 'tumour', 'cancer', 'malignant'],
        'normal': ['normal', 'healthy', 'control', 'benign'],
        'lung': ['lung', 'pulmonary', 'bronch'],
        'tissue': ['tissue', 'biopsy', 'sample']
    }

    # Categorize files
    categorized_files = {
        'lung_tumor': [],
        'lung_normal': [],
        'other_tumor': [],
        'other_normal': [],
        'uncategorized': []
    }

    for file_info in raw_files:
        filename = file_info.get('fileName', '')
        filename_lower = filename.lower()

        # Check for keywords
        is_tumor = any(kw in filename_lower for kw in keywords['tumor'])
        is_normal = any(kw in filename_lower for kw in keywords['normal'])
        is_lung = any(kw in filename_lower for kw in keywords['lung'])

        # Categorize
        if is_lung and is_tumor:
            categorized_files['lung_tumor'].append(file_info)
        elif is_lung and is_normal:
            categorized_files['lung_normal'].append(file_info)
        elif is_tumor:
            categorized_files['other_tumor'].append(file_info)
        elif is_normal:
            categorized_files['other_normal'].append(file_info)
        else:
            categorized_files['uncategorized'].append(file_info)

    # Display results
    print("\n" + "-" * 80)
    print("\nCATEGORIZATION RESULTS:")
    print("-" * 80)

    print(f"\nLung Tumor Samples: {len(categorized_files['lung_tumor'])}")
    for file_info in categorized_files['lung_tumor']:
        print(f"  - {file_info.get('fileName')}")
        print(f"    Size: {file_info.get('fileSizeBytes', 0) / (1024**3):.2f} GB")

    print(f"\nLung Normal/Control Samples: {len(categorized_files['lung_normal'])}")
    for file_info in categorized_files['lung_normal']:
        print(f"  - {file_info.get('fileName')}")
        print(f"    Size: {file_info.get('fileSizeBytes', 0) / (1024**3):.2f} GB")

    print(f"\nOther Tumor Samples: {len(categorized_files['other_tumor'])}")
    for file_info in categorized_files['other_tumor']:
        print(f"  - {file_info.get('fileName')}")

    print(f"\nOther Normal/Control Samples: {len(categorized_files['other_normal'])}")
    for file_info in categorized_files['other_normal']:
        print(f"  - {file_info.get('fileName')}")

    print(f"\nUncategorized Files: {len(categorized_files['uncategorized'])}")
    if categorized_files['uncategorized']:
        print("\nShowing first 20 uncategorized files for pattern analysis:")
        for file_info in categorized_files['uncategorized'][:20]:
            print(f"  - {file_info.get('fileName')}")

    # 5. Publication DOI information
    print("\n" + "=" * 80)
    print("\n5. Publication Information:")
    if pub_doi:
        print(f"\nPublication DOI: {pub_doi}")
        print(f"You can access the publication at: https://doi.org/{pub_doi}")
        print("\nTo fetch the abstract, you can use a service like:")
        print(f"  - PubMed: Search for DOI {pub_doi}")
        print(f"  - CrossRef API: https://api.crossref.org/works/{pub_doi}")
    else:
        print("\nNo publication DOI found in metadata")

    # Save detailed results to JSON
    output_file = f"{accession}_analysis.json"
    with open(output_file, 'w') as f:
        json.dump({
            'accession': accession,
            'metadata': metadata,
            'categorized_files': {
                category: [f.get('fileName') for f in files_list]
                for category, files_list in categorized_files.items()
            },
            'summary': {
                'total_files': len(files),
                'total_raw_files': len(raw_files),
                'lung_tumor_files': len(categorized_files['lung_tumor']),
                'lung_normal_files': len(categorized_files['lung_normal']),
                'other_tumor_files': len(categorized_files['other_tumor']),
                'other_normal_files': len(categorized_files['other_normal']),
                'uncategorized_files': len(categorized_files['uncategorized'])
            }
        }, f, indent=2)

    print(f"\n\nDetailed analysis saved to: {output_file}")

if __name__ == "__main__":
    main()
