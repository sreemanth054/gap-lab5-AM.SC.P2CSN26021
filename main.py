import json
import re
import sys

from pydantic import BaseModel, Field, ValidationError, model_validator

from client import get_client, get_model


class Question(BaseModel):
    question: str = Field(min_length=5, max_length=500)
    options: list[str] = Field(min_length=4, max_length=4)
    answer_index: int = Field(ge=0, le=3)

    @model_validator(mode="after")
    def validate_answer(self):
        if self.answer_index >= len(self.options):
            raise ValueError("answer_index must point to an existing option")

        if len(set(option.strip() for option in self.options)) != len(self.options):
            raise ValueError("options must be unique")

        return self


class QuestionPaper(BaseModel):
    questions: list[Question] = Field(min_length=5, max_length=5)


def extract_json(text: str):
    """Extract the first valid JSON value from model output."""
    text = text.strip()

    # Remove markdown code fences if they are present.
    text = re.sub(r"^\s*```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```\s*$", "", text)

    # Try to decode JSON starting from each possible object/array.
    decoder = json.JSONDecoder()

    for index, char in enumerate(text):
        if char not in "{[":
            continue

        try:
            value, _ = decoder.raw_decode(text[index:])
            return value
        except json.JSONDecodeError:
            continue

    raise json.JSONDecodeError("No valid JSON found", text, 0)


def looks_like_refusal(text: str) -> bool:
    """Detect common refusal-style replies before JSON parsing."""
    refusal_patterns = [
        r"\bi can't\b",
        r"\bi cannot\b",
        r"\bi’m unable\b",
        r"\bi'm unable\b",
        r"\bi am unable\b",
        r"\bi won't\b",
        r"\bi will not\b",
        r"\bcan't help with\b",
        r"\bcannot help with\b",
        r"\bnot able to\b",
        r"\bunable to comply\b",
    ]

    lower_text = text.lower()

    return any(re.search(pattern, lower_text) for pattern in refusal_patterns)


def generate_questions(topic: str):
    client = get_client()
    model = get_model()

    prompt = f"""
Generate exactly five multiple-choice questions about: {topic}

Return ONLY a JSON object in this exact structure:

{{
  "questions": [
    {{
      "question": "question text",
      "options": [
        "option 1",
        "option 2",
        "option 3",
        "option 4"
      ],
      "answer_index": 0
    }}
  ]
}}

Rules:
- There must be exactly five questions.
- Each question must have exactly four options.
- answer_index must be 0, 1, 2, or 3.
- answer_index identifies the correct option in the options list.
- Do not use Markdown code fences.
- Do not add explanations or text before or after the JSON.
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content or ""


def main():
    # Input gate: reject invalid topics before making a model call.
    if len(sys.argv) != 2:
        print("error")
        sys.exit(2)

    topic = sys.argv[1]

    if not topic.strip() or len(topic) < 3 or len(topic) > 200:
        print("error")
        sys.exit(2)

    try:
        raw_response = generate_questions(topic)

        if not raw_response.strip():
            print("invalid_output")
            sys.exit(1)

        if looks_like_refusal(raw_response):
            print("refused")
            sys.exit(1)

        data = extract_json(raw_response)
        result = QuestionPaper.model_validate(data)

        print(json.dumps(result.model_dump(), indent=2))
        print("ok")
        sys.exit(0)

    except ValidationError:
        print("invalid_output")
        sys.exit(1)

    except json.JSONDecodeError:
        print("invalid_output")
        sys.exit(1)

    except Exception:
        print("error")
        sys.exit(1)


if __name__ == "__main__":
    main()