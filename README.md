# DART PDF Extractor

DART PDF Extractor는 전자공시시스템(DART)의 사업보고서 PDF 파일에서 주요 섹션을 추출하는 간단한 웹 서비스입니다.

## 요구사항

- Python 3.7+
- Flask
- PyPDF2

## 설치

1. 이 리포지토리를 클론합니다:
   ```
   git clone https://github.com/your-username/dart-pdf-extractor.git
   cd dart-pdf-extractor
   ```

2. 필요한 패키지를 설치합니다:
   ```
   pip install flask PyPDF2
   ```

## 실행 방법

1. 터미널에서 다음 명령어를 실행합니다:
   ```
   python app.py
   ```

2. 브라우저에서 `http://localhost:5000`으로 접속합니다.

3. POST 요청을 `/extract` 엔드포인트로 보내 PDF 파일을 업로드하고 결과를 받습니다.

## 사용 예시

```python
import requests

url = 'http://localhost:5000/extract'
files = {'file': open('path_to_your_pdf_file.pdf', 'rb')}
response = requests.post(url, files=files)

print(response.json())
```

## 주의사항

이 프로젝트는 간단한 예시이며, 실제 사용을 위해서는 보안, 에러 처리, 성능 최적화 등의 추가 작업이 필요합니다.
