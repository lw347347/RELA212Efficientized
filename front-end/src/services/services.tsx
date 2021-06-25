const baseUrl = 'http://localhost:8000';

const DatabaseService = {
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
    }
}

export default DatabaseService;