import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import React, { useEffect, useState } from 'react';
import DatabaseService from '../services/services';

export default function StudyGuideImporter(props: {}) {
    const [examList, setExamList] = useState<any>([]);

    useEffect(() => {
        // go get the exam lists
        DatabaseService.getExams().then((response: any) => {            
            setExamList(response);
        });
    }, []);

    let handleSubmit = (e: any) => {
        e.preventDefault();
        let myFormData = new FormData(document.getElementById("myForm") as HTMLFormElement);

        DatabaseService.createStudyGuide(myFormData);
    }   
    
    return(
        <div>
            <Form id="myForm" onSubmit={handleSubmit}>
                <Form.Group>
                    <Form.Label>Study Guide Name</Form.Label>
                    <Form.Control type="text" name="name" id="name" placeholder="Enter study guide name" />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Study Guide Type</Form.Label>
                    <Form.Control as="select" name="typeOfStudyGuide" id="typeOfStudyGuide">
                        <option value="handout">Handout</option>
                        <option value="lecture">Lecture</option>
                        <option value="scripture">Scripture</option>
                    </Form.Control>
                </Form.Group>
                <Form.Group>
                    <Form.Label>Date of Assignment</Form.Label>
                    <Form.Control type="date" name="dateOfAssignment" id="dateOfAssignment" />
                </Form.Group>
                <Form.Group>
                    <Form.Label>Exam</Form.Label>
                    <Form.Control as="select" name="examId" id="examId">
                        {
                            examList.map((item: any, index: number) => {
                                return <option>{ item.examNumber }</option>;
                            })
                        }
                    </Form.Control>
                </Form.Group>
                <Form.Group>
                    <Form.File 
                        id="file"
                        name="file"
                        label="Study guide file"
                        custom
                    />
                </Form.Group>
                <Button type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    )
}