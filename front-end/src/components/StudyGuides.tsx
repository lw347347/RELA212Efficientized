import { useEffect, useState } from "react";
import DatabaseService from "../services/services";
import { Button, ListGroup } from 'react-bootstrap';
import { Link } from "react-router-dom";

export default function StudyGuides(props: any) {
    const [studyGuides, setStudyGuides] = useState<any>([]);

    useEffect(() => {
        DatabaseService.getStudyGuides().then((response: any) => {
            setStudyGuides(response);
        })
    }, []);

    return(
        <div className="mainContent">
            <div></div>
            <ListGroup>
                {studyGuides.map((item: any, index: number) => {
                    return(                    
                        <ListGroup.Item>
                            <ListGroup horizontal>
                                <ListGroup.Item>
                                    {item.name}
                                </ListGroup.Item>
                                <ListGroup.Item>
                                    <Link to={`/studyGuides/${item.studyGuideId}`}>View</Link>
                                </ListGroup.Item>
                            </ListGroup>
                        </ListGroup.Item>
                    )
                })}
            </ListGroup>
            <div></div>
        </div>
    )
}