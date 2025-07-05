import axios from "axios";

const apiClient = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: false,
    headers: {
        Accept: "application/json",
        "Content-Type": 'application/json'
    }
});

export default {
    simplifyPDF(pdf: File) {
        const formData = new FormData();

        formData.append('file', pdf);

        return apiClient.post('/privacy-policy/simplify', formData);
    }
}