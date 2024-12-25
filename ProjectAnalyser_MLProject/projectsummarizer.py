import os
import re
import json
from transformers import pipeline

# Initialize summarization model
summarizer = pipeline(summarization, model=facebookbart-large-cnn)

def analyze_file(file_path)
    with open(file_path, 'r') as file
        content = file.read()

    # Extract class name
    class_name = re.search(r'classs+(w+)', content)
    class_name = class_name.group(1) if class_name else UnknownClass

    # Extract main imports (dependencies)
    imports = re.findall(r'imports+([w.]+);', content)
    
    # Extract method signatures
    methods = re.findall(r'publics+[^{]+{', content)
    method_signatures = [method.split('{')[0].strip() for method in methods]

    # Generate summary using NLP model
    try
        summary = summarizer(content, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    except Exception as e
        summary = fSummarization failed {str(e)}

    # Structure analysis data
    analysis = {
        file_name os.path.basename(file_path),
        class_name class_name,
        imports imports,
        methods method_signatures,
        summary summary
    }
    
    return analysis

def analyze_directory(directory_path)
    # Traverse directory and analyze each Java file
    analysis_report = []
    for root, _, files in os.walk(directory_path)
        for file in files
            if file.endswith(.java)
                file_path = os.path.join(root, file)
                analysis = analyze_file(file_path)
                analysis_report.append(analysis)

    # Save report as JSON
    with open(project_analysis.json, w) as report_file
        json.dump(analysis_report, report_file, indent=4)
    print(Analysis report generated project_analysis.json)

# Run analysis on the project directory
project_directory = pathtoyourproject  # Update this to your project's root directory
analyze_directory(project_directory)
