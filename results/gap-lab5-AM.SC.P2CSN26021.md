# Lab 5: gap-lab5-AM.SC.P2CSN26021

**Harness: 5.0 / 5.0**

| | Check | Marks | Result | Note |
|---|---|--:|:-:|---|
| A | Required files present | 0.3 | PASS |  |
| A | client.py unmodified | 0.2 | PASS |  |
| A | .env and run_log.jsonl ignored, neither ever committed | 0.3 | PASS |  |
| A | SPEC.md has its six headings, REPORT.md its three | 0.2 | PASS |  |
| A | Git: >=5 commits and the lab-5-submission tag | 0.2 | PASS |  |
| B | stub:ok -> ok (exit 0) | 0.125 | PASS |  |
| B | stub:fenced -> ok (exit 0) | 0.125 | PASS |  |
| B | stub:preamble -> ok (exit 0) | 0.125 | PASS |  |
| B | stub:malformed -> invalid_output (exit 1) | 0.125 | PASS |  |
| B | stub:badshape -> invalid_output (exit 1) | 0.125 | PASS |  |
| B | stub:empty -> invalid_output (exit 1) | 0.125 | PASS |  |
| B | stub:refused -> refused (exit 1) | 0.125 | PASS |  |
| B | stub:error -> error (exit 1) | 0.125 | PASS |  |
| C | run_log.jsonl written, one parseable JSON object per line | 0.3 | PASS |  |
| C | Every line carries the nine fields, correctly typed | 0.4 | PASS |  |
| C | The last line's status matches the word printed | 0.3 | PASS |  |
| C | One run_id per run of main.py | 0.3 | PASS |  |
| D | stub:flaky -> retried, ended ok, every attempt logged | 0.4 | PASS |  |
| D | stub:ratelimit -> capped at 2-3 attempts, each logged, ends error | 0.3 | PASS |  |
| D | stub:malformed -> exactly one repair retry, both lines invalid_output | 0.3 | PASS |  |
| E | empty topic -> exit 2, no model call, no log line | 0.3 | PASS |  |
| F | samples/run_log_sample.jsonl: >=20 good lines, nothing secret | 0.2 | PASS |  |