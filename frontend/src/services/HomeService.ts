import axios from "axios";
import * as pdfjsLib from 'pdfjs-dist'
import pdfjsWorker from 'pdfjs-dist/build/pdf.worker.mjs?url'

pdfjsLib.GlobalWorkerOptions.workerSrc = pdfjsWorker

const apiClient = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: false,
    headers: {
        Accept: "application/json",
    }
});

async function extractTextFromPDF(pdf: File): Promise<string> {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();

        reader.onload = async (e) => {
            try {
                const arrayBuffer = e.target?.result as ArrayBuffer;
                const pdfDoc = await pdfjsLib.getDocument(arrayBuffer).promise;
                
                let fullText = '';
                for (let i = 1; i <= pdfDoc.numPages; i++) {
                    const page = await pdfDoc.getPage(i);
                    const textContent = await page.getTextContent();
                    fullText += textContent.items.map(item => 'str' in item ? item.str : '').join(' ') + '\n';
                }
                
                resolve(fullText);

            } catch (error) {
                console.error('Failed to extract PDF text:', error);
                reject('Error: Could not read this PDF.');
            }
        };

        reader.onerror = () => {
            reject('Error: Failed to read the file.');
        };

    
        reader.readAsArrayBuffer(pdf);
    });
}
export default {
    async simplifyPDF(pdf: File) {
        const extractedText = await extractTextFromPDF(pdf)
        
        return await apiClient.post("/privacy-policy/simplify", 
            { text: extractedText }, 
            { 
                responseType: 'blob'
            }
        )
    }
}