const fs = require('fs');
const PDFParser = require("pdf2json");
const path = require('path')
const countWords = require('./statsWords.js')

const successLoadPdf = () => {
    const words = fs.readFileSync('./test.txt', {
        encoding: 'utf-8'
    })
    console.log(words);
    fs.writeFileSync('word.js', countWords(words))

}

const pdfParser = new PDFParser(this, 1);
pdfParser.on("pdfParser_dataError", (errData) => console.error(errData.parserError));
pdfParser.on("pdfParser_dataReady", (pdfData) => {
    fs.writeFile("./test.txt", pdfParser.getRawTextContent(), { encoding: 'utf-8' }, () => { successLoadPdf() })


});

pdfParser.loadPDF("./src/test.pdf");

