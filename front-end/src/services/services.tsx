const baseUrl = 'http://localhost:8000';

const DatabaseService = {
    createStudyGuide: async (myFormData: any) => {
        return await fetch (`${baseUrl}/studyGuides/`,
            {
                method: 'POST',
                body: myFormData
            }
        ).catch((e) => {
            console.log(e);
        })
    },
    getExams: async () => {
        return await fetch(`${baseUrl}/exams/`, 
            {
                method: 'GET',
                mode: 'cors'
            }
        ).then((response) => response.json()) 
        .then((data: [])=> {
            return data;
        });
    },
    getStudyGuides: async () => {
        return await fetch(`${baseUrl}/studyGuides/`, 
            {
                method: 'GET',
                mode: 'cors'
            }
        ).then((response) => response.json())
        .then((data: []) => {
            return data;
        });
    }
}

export default DatabaseService;