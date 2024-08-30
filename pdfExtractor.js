const mainSections = [
    "회사의 개요",
    "사업의 내용",
    "재무에 관한 사항",
    "감사인의 감사의견 등",
    "이사회 등 회사의 기관에 관한 사항",
    "주주에 관한 사항"
];

function extractSections(text) {
    let extractedContent = {};
    for (let section of mainSections) {
        let pattern = new RegExp(`${section}([\\s\\S]*?)(?=${mainSections.join('|')}|$)`, 'i');
        let match = text.match(pattern);
        extractedContent[section] = match ? match[1].trim() : "내용을 찾을 수 없습니다.";
    }
    return extractedContent;
}

async function extractFromPdf(file) {
    return new Promise((resolve, reject) => {
        let reader = new FileReader();
        reader.onload = async function(e) {
            let typedarray = new Uint8Array(e.target.result);

            try {
                let pdf = await pdfjsLib.getDocument(typedarray).promise;
                let pagesPromises = [];
                for (let i = 1; i <= pdf.numPages; i++) {
                    pagesPromises.push(pdf.getPage(i).then(page => page.getTextContent()));
                }
                let pagesContents = await Promise.all(pagesPromises);
                let fullText = pagesContents.map(content => 
                    content.items.map(item => item.str).join(' ')
                ).join('\n');

                let extractedSections = extractSections(fullText);
                resolve(extractedSections);
            } catch (error) {
                reject(error);
            }
        };
        reader.readAsArrayBuffer(file);
    });
}
