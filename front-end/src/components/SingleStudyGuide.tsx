import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import DatabaseService from "../services/services";
import AddAnswers from "./AddAnswers";

export default function SingleStudyGuide() {
    const { studyGuideId } = useParams<{ studyGuideId: string}>();
    const [ studyGuide, setStudyGuide] = useState<{questionGroups: any[]} | undefined>();
    const [ activeQuestionGroupIndex, setActiveQuestionGroupIndex ] = useState<number>(0);

    useEffect(() => {
        // Go get the study guide
        DatabaseService.getStudyGuide(parseInt(studyGuideId)).then((response) => {            
            setStudyGuide(response);
        });
    }, []);

    function getNextQuestionGroup() {
        if (studyGuide !== undefined && studyGuide?.questionGroups?.length > activeQuestionGroupIndex - 1) {       
            setActiveQuestionGroupIndex(activeQuestionGroupIndex + 1);
        } else {
            return false;
        }
    }

    function getPreviousQuestionGroup() {
        if (activeQuestionGroupIndex !== 0) {
            setActiveQuestionGroupIndex(activeQuestionGroupIndex - 1);   
        } else {
            return false;
        }    
    }

    return (
        <div className="mainContent">
            <div></div>
            <div>

            </div>
            <AddAnswers
                getNextQuestionGroup={getNextQuestionGroup}
                getPreviousQuestionGroup={getPreviousQuestionGroup}
                questionGroup={studyGuide?.questionGroups[activeQuestionGroupIndex]}
            >
            </AddAnswers>
        </div>
    );
}