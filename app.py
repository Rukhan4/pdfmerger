from flask import Flask, render_template, request, send_file
import PyPDF2
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/merge', methods=['POST'])
def merge_pdfs():
    pdf1 = request.files['file1']
    pdf2 = request.files['file2']

    pdf_merger = PyPDF2.PdfMerger()
    pdf_merger.append(pdf1)
    pdf_merger.append(pdf2)

    output_pdf = io.BytesIO()
    pdf_merger.write(output_pdf)
    output_pdf.seek(0)

    return send_file(
        output_pdf,
        as_attachment=True,
        download_name='merged.pdf',
        mimetype='application/pdf'
    )


if __name__ == '__main__':
    app.run(debug=True)
