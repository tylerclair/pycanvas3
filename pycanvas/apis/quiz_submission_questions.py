"""QuizSubmissionQuestions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from base import BaseCanvasAPI
from base import BaseModel


class QuizSubmissionQuestionsAPI(BaseCanvasAPI):
    """QuizSubmissionQuestions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for QuizSubmissionQuestionsAPI."""
        super(QuizSubmissionQuestionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("pycanvas.QuizSubmissionQuestionsAPI")

    def get_all_quiz_submission_questions(self, quiz_submission_id, include=None):
        """
        Get all quiz submission questions.

        Get a list of all the question records for this quiz submission.
        
        <b>200 OK</b> response code is returned if the request was successful.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - quiz_submission_id - ID
        path["quiz_submission_id"] = quiz_submission_id
        # OPTIONAL - include - Associations to include with the quiz submission question.
        if include is not None:
            self._validate_enum(include, ["quiz_question"])
        if include is not None:
            payload["include"] = include

        self.logger.debug("GET /api/v1/quiz_submissions/{quiz_submission_id}/questions with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("GET", "/api/v1/quiz_submissions/{quiz_submission_id}/questions".format(**path), params=payload, no_data=True)

    def get_single_quiz_submission_question(self, id, quiz_submission_id, include=None):
        """
        Get a single quiz submission question.

        Get a single question record.
        
        <b>200 OK</b> response code is returned if the request was successful.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - quiz_submission_id - ID
        path["quiz_submission_id"] = quiz_submission_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # OPTIONAL - include - Associations to include with the quiz submission question.
        if include is not None:
            self._validate_enum(include, ["quiz_question"])
        if include is not None:
            payload["include"] = include

        self.logger.debug("GET /api/v1/quiz_submissions/{quiz_submission_id}/questions/{id} with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("GET", "/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}".format(**path), params=payload, no_data=True)

    def answering_questions(self, attempt, validation_token, quiz_submission_id, access_code=None, quiz_questions=None):
        """
        Answering questions.

        Provide or update an answer to one or more QuizQuestions.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - quiz_submission_id - ID
        path["quiz_submission_id"] = quiz_submission_id
        # REQUIRED - attempt - The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified.
        payload["attempt"] = attempt
        # REQUIRED - validation_token - The unique validation token you received when the Quiz Submission was created.
        payload["validation_token"] = validation_token
        # OPTIONAL - access_code - Access code for the Quiz, if any.
        if access_code is not None:
            payload["access_code"] = access_code
        # OPTIONAL - quiz_questions - Set of question IDs and the answer value. See {Appendix: Question Answer Formats} for the accepted answer formats for each question type.
        if quiz_questions is not None:
            payload["quiz_questions"] = quiz_questions

        self.logger.debug("POST /api/v1/quiz_submissions/{quiz_submission_id}/questions with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("POST", "/api/v1/quiz_submissions/{quiz_submission_id}/questions".format(**path), data=payload, all_pages=True)

    def flagging_question(self, id, attempt, validation_token, quiz_submission_id, access_code=None):
        """
        Flagging a question.

        Set a flag on a quiz question to indicate that you want to return to it
        later.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - quiz_submission_id - ID
        path["quiz_submission_id"] = quiz_submission_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - attempt - The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified.
        payload["attempt"] = attempt
        # REQUIRED - validation_token - The unique validation token you received when the Quiz Submission was created.
        payload["validation_token"] = validation_token
        # OPTIONAL - access_code - Access code for the Quiz, if any.
        if access_code is not None:
            payload["access_code"] = access_code

        self.logger.debug("PUT /api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("PUT", "/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag".format(**path), data=payload, no_data=True)

    def unflagging_question(self, id, attempt, validation_token, quiz_submission_id, access_code=None):
        """
        Unflagging a question.

        Remove the flag that you previously set on a quiz question after you've
        returned to it.
        """
        path = {}
        payload = {}

        # REQUIRED - PATH - quiz_submission_id - ID
        path["quiz_submission_id"] = quiz_submission_id
        # REQUIRED - PATH - id - ID
        path["id"] = id
        # REQUIRED - attempt - The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified.
        payload["attempt"] = attempt
        # REQUIRED - validation_token - The unique validation token you received when the Quiz Submission was created.
        payload["validation_token"] = validation_token
        # OPTIONAL - access_code - Access code for the Quiz, if any.
        if access_code is not None:
            payload["access_code"] = access_code

        self.logger.debug("PUT /api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag with payload: {payload}".format(payload=payload, **path))
        return self.generic_request("PUT", "/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag".format(**path), data=payload, no_data=True)


class Quizsubmissionquestion(BaseModel):
    """Quizsubmissionquestion Model."""

    def __init__(self, id, answer=None, flagged=None):
        """Init method for Quizsubmissionquestion class."""
        self._answer = answer
        self._id = id
        self._flagged = flagged

        self.logger = logging.getLogger('pycanvas.Quizsubmissionquestion')

    @property
    def answer(self):
        """The provided answer (if any) for this question. The format of this parameter depends on the type of the question, see the Appendix for more information."""
        return self._answer

    @answer.setter
    def answer(self, value):
        """Setter for answer property."""
        self.logger.warn("Setting values on answer will NOT update the remote Canvas instance.")
        self._answer = value

    @property
    def id(self):
        """The ID of the QuizQuestion this answer is for."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def flagged(self):
        """Whether this question is flagged."""
        return self._flagged

    @flagged.setter
    def flagged(self, value):
        """Setter for flagged property."""
        self.logger.warn("Setting values on flagged will NOT update the remote Canvas instance.")
        self._flagged = value

