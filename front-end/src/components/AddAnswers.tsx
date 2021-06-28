import { useState, useEffect } from 'react';
import { Button, ListGroup } from 'react-bootstrap';
import DatabaseService from '../services/services';
export default function AddAnswers(props: any) {
    const [questionGroup, setQuestionGroup] = useState<any>();
    const [currentItemValue, setCurrentItemValue] = useState<any>();

    useEffect(() => {
        setQuestionGroup(props.questionGroup);
    }, [props.questionGroup]);

    return (
        <div>
            <ListGroup>
                {questionGroup?.questions.map((item: any, index: number) => {
                    return(                    
                        <ListGroup.Item>
                            <ListGroup horizontal>
                                <ListGroup.Item>
                                    {item.questionText}
                                </ListGroup.Item>
                                <ListGroup.Item>                                    
                                    <input type="text" 
                                    onFocus={() => setCurrentItemValue(item.answer?.answerText)}
                                    onChange={(e) => {
                                            setCurrentItemValue(e.target.value);
                                        }
                                    }
                                    onBlur={() => {
                                        DatabaseService.setQuestionAnswer(item.questionId, currentItemValue, item?.answer?.answerId);
                                    }}
                                    value={currentItemValue}></input>
                                </ListGroup.Item>
                            </ListGroup>
                        </ListGroup.Item>
                    )
                })}
            </ListGroup>
            <Button onClick={props.getPreviousQuestionGroup}>Previous</Button>
            <Button onClick={props.getNextQuestionGroup}>Next</Button>
        </div>
    );
}