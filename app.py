from flask import Flask, request, jsonify
import PyPDF2
import re

app = Flask(__name__)

def extract_sections(pdf_content):
    main_sections = [
        "회사의 개요",
        "사업의 내용",
        "재무에 관한 사항",
        "감사인의 감사의견 등",
        "이사회 등 회사의 기관에 관한 사항",
        "주주에 관한 사항"
    ]
    extracted_content = {}

    for section in main_sections:
        pattern = f"{section}(.*?)(?={main_sections[0]}|{main_sections[-1]}|$)"
        match = re.search(pattern, pdf_content, re.DOTALL)
        if match:
            extracted_content[section] = match.group(1).strip()
        else:
            extracted_content[section] = "내용을 찾을 수 없습니다."

    return extracted_content

@app.route('/extract', methods=['POST'])
def extract_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file and file.filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_content = ""
        for page in pdf_reader.pages:
            pdf_content += page.extract_text()
        
        extracted_sections = extract_sections(pdf_content)
        return jsonify(extracted_sections)
    else:
        return jsonify({"error": "Invalid file format. Please upload a PDF."}), 400

if __name__ == '__main__':
    app.run(debug=True)
