import { useEffect, useState } from "react";
import DatabaseService from "../services/services";

export default function StudyGuides(props: any) {
    const [studyGuides, setStudyGuides] = useState<any>([]);

    useEffect(() => {
        DatabaseService.getStudyGuides().then((response: any) => {
            setStudyGuides(response);
        })
    }, []);

    return(
        <div>hello</div>
    )
}