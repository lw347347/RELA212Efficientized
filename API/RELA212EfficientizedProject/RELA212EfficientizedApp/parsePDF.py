import re


def parsePDF(studyGuide, file, questionGroupSplitter="*", questionGroupBeginning=""):
    # if (studyGuide.typeOfStudyGuide == "scripture"):        
    #     # Find scripture book and chapter

    # elif(studyGuide.typeOfStudyGuide == "handout"):

    # # Find each question group (look for "*"")
    #     # Find each question (look for "?")         
    #         # Figure out if is note or not
    #         if (doesNotContainQuestionMark)
    #         # Find answer hints look for "(vv"
    #         # Look for specifically what does the word "" mean?
    #         # Look for specifically word word what?
        
    import PyPDF2
    from .models import QuestionGroup, Question, AnswerHint
    reader = PyPDF2.PdfFileReader(file)
    pageObject = reader.getPage(1)
    firstPageText = pageObject.extractText()
    splitStrings = firstPageText.replace("\n", "").split("*")
    print(splitStrings)

    # Loop through each page
    for pageIndex in range(1, reader.getNumPages()):
        page = reader.getPage(pageIndex)
        pageText = page.extractText()

        # Split the strings based on the asterisk
        splitStrings = pageText.replace("\n", "").split(questionGroupSplitter)

        # Loop through each split string to find the questions
        for questionGroup in splitStrings:            
            questionsInQuestionGroup = re.split('([?]\W)', questionGroup.strip())

            # Create the question group
            newQuestionGroup = QuestionGroup.objects.create(
                studyGuideId = studyGuide,
                countOfQuestions = len(questionsInQuestionGroup)
            )
            newQuestionGroup.save()

            # Check for note
            isNote = False
            if len(questionsInQuestionGroup) == 1 or "?" not in questionGroup:
                # It's a note
                isNote = True

            for questionIndex in range(len(questionsInQuestionGroup)):
                # Check for a hint
                questionText = questionsInQuestionGroup[questionIndex].strip()               
                # Create the question
                newQuestion = Question.objects.create(
                    questionGroupId = newQuestionGroup,
                    questionText = questionsInQuestionGroup[questionIndex],
                    isNote = isNote
                )
                newQuestion.save()

                if (questionIndex < len(questionsInQuestionGroup) - 1):
                    if "(" in questionsInQuestionGroup[questionIndex + 1] and ")" in questionsInQuestionGroup[questionIndex + 1]:
                        # It has an answer hint
                        firstIndex = int(questionsInQuestionGroup[questionIndex + 1].find("("))
                        secondIndex = int(questionsInQuestionGroup[questionIndex + 1].find(")"))
                        newAnswerHint = AnswerHint.objects.create(
                            hintText = questionsInQuestionGroup[questionIndex + 1][firstIndex:secondIndex],
                            questionId = newQuestion
                        )
                        newAnswerHint.save()