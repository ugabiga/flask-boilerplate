from flask import jsonify

from app.core.use_case_outputs import UseCaseFailureOutput


def build_failure_response(use_case_output: UseCaseFailureOutput):
    return (
        jsonify(error=use_case_output.type, error_description=use_case_output.message),
        use_case_output.code,
    )
