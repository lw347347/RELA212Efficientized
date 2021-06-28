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
    getStudyGuide: async (studyGuideId: number) => {
        return await fetch(`${baseUrl}/studyGuides/${studyGuideId}/`,
            {
                method: 'GET',
                mode: 'cors'
            }
        ).then((response => response.json()))
        .then((data: {questionGroups: any[]}) => {
            return data;
        })
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
    },
    setQuestionAnswer: async (questionId: number, answerText: string, answerId: number) => {
        if (answerId !== undefined) {
            return await fetch(`${baseUrl}/answers/${answerId}/`, 
                {
                    method: 'PUT',
                    mode: 'cors',
                    body: JSON.stringify({
                        questionId: questionId,
                        answerText: answerText
                    }),
                    headers: {
                        'Content-Type': 'application/json'
                    },
                }
            ).then((response) => {
                console.log(response);
                return response.json();
            })
            .then((data): any => {
                return data;
            })
        }
        return await fetch(`${baseUrl}/answers/`, 
            {
                method: 'POST',
                mode: 'cors',
                body: JSON.stringify({
                    questionId: questionId,
                    answerText: answerText
                }),
                headers: {
                    'Content-Type': 'application/json'
                },
            }
        ).then((response) => {
            response.json()
        })
        .then((data: any) => {
            return data;
        })
    }
}

export default DatabaseService;