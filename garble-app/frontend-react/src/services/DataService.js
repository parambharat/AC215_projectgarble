import { BASE_API_URL } from "./Common";

const axios = require('axios');

const DataService = {
    Init: function () {
        // Any application initialization logic comes here
    },
    Transcribe: async function (formData) {
      console.log(formData);
        return await axios.post(BASE_API_URL + "transcribe", formData, {
            headers: {
                'Content-Type': 'multipart/form-data', 
            }
        });
    },
    Summarize: async function (transcript) {
      console.log({transcript});
        return await axios.post(BASE_API_URL + "summarize", {transcript: transcript}, {
            headers: {
                'Content-Type': 'application/json', 
            }
        });
    },
}

export default DataService;