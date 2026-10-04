# What it does

The program takes a topic entered by the user and uses AI model to generate five mcqs on the given topic. Each question contains four answer options and one correct answer. The program checks and validates the model's response before accepting it. Only responses that follows the required structure and constraints are accepted.


# Inputs

The topic will be given as a string through the command line. It should be at least 3 characters long and should not exceed 200 characters. Topics containing spaces are allowed, as long as they are entered within quotes. If the topic is missing, empty, contains only spaces, or does not meet the length requirements, the program will reject it without sending anything to the AI model.

# Outputs

The program should generate exactly five questions for a valid topic. Each question will have the question itself, four answer options, and an answer_index that shows which option is correct. The generated response will be checked against these requirements before it is accepted.
The last non-empty line printed by the program will always show what happened. It will be one of ok, invalid_output, refused, or error. A valid response will return ok with exit code 0. If the model response is invalid, refused, or an error occurs during the model call, the program will return the corresponding status with exit code 1. If the topic is rejected before contacting the model, the program will exit with code 2.

# Failure cases

If the user does not provide a topic, or if the topic is empty, only contains spaces, or is outside the allowed length, the program will reject it without contacting the AI model and exit with code 2.
If the model gives a response that is not valid JSON, the program will reject it and return invalid_output with exit code 1.
If the response is valid JSON but does not follow the required format, such as having the wrong number of questions or options, it will also be rejected as invalid_output with exit code 1.
If the model returns nothing, the program will treat it as invalid_output and exit with code 1.
If the model refuses to generate the questions, the program will return refused with exit code 1.
If there is an error while communicating with the model or something goes wrong during the model call, the program will return error with exit code 1.
If the model puts the JSON inside Markdown code blocks or adds some text before the JSON, the program will try to extract the JSON and then validate it.

# Acceptance checks

A successful generation should produce five valid questions and end with `ok`.

The stub modes are also tested individually:

`stub:ok` → `ok`, exit code 0
`stub:fenced` → `ok`, exit code 0
`stub:preamble` → `ok`, exit code 0
`stub:malformed` → `invalid_output`, exit code 1
`stub:badshape` → `invalid_output`, exit code 1
`stub:empty` → `invalid_output`, exit code 1
`stub:refused` → `refused`, exit code 1
`stub:error` → `error`, exit code 1

`python check.py .`

The checker should complete successfully without reporting failed checks.

# Out of scope

This program will focus only on generating multiple-choice questions through the command line. it will not provide a graphical or web interface or support other types of questions such as short-answer or true/false questions.Features such as user accounts, authentication, databases, storing previous questions, and editing questions manually are also outside the scope of this project.
