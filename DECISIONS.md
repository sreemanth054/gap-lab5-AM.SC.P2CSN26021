# Decisions

## 2026-09-21 - Handle extra text around JSON

I noticed that the model does not always have to return the JSON exactly by itself. The stub also has cases where the JSON is inside Markdown fences or has some text before it.

I added an `extract_json` function that first removes the common code-fence formatting and then looks for the JSON in the response.

I could have just rejected anything that was not raw JSON, but then the `fenced` and `preamble` cases would fail even though the actual JSON is valid.

## 2026-09-21 - Add a separate refusal check

I found that a refusal is not necessarily returned with a special flag that I can check. It can just come back as normal text, which would otherwise look like invalid JSON.

I added a small check for common refusal phrases before trying to extract the JSON.

I considered treating every non-JSON response as `invalid_output`, but then I would not be able to return the separate `refused` result required by the lab.

## 2026-09-21 - Validate the response with Pydantic

While writing the validation, I realised that successfully parsing JSON is not enough. The JSON can still have the wrong number of questions or options, or an `answer_index` that does not point to an option.

I used Pydantic `Field` constraints for the basic limits and a `model_validator` for checks involving the options and answer index.

I could have checked these conditions manually with `if` statements, but using the Pydantic model keeps the validation in one place and makes the expected structure clearer.

## 2026-09-21 - Test all the different model responses

After getting a successful response from Gemini, I still needed to make sure the program handled responses that were not successful.

I tested all eight stub modes, including malformed JSON, wrong-shaped JSON, an empty response, a refusal, and a model error. They produced the expected status and exit codes.

I could have stopped after confirming that Gemini generated the questions correctly, but that would not have tested the failure handling in the program.s