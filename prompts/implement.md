Your task is to implement (or continue implementing) the spec using
test-driven development.

Read the spec profile from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/standard/spec-profile.md

If this is a continuation, check the spec's test case status column to see
where you left off.

Steps:

1. Read the spec. Read docs/ai/L1/07_gotchas.md and
   docs/ai/L1/04_conventions.md before writing any code.
2. Red: Write the failing tests, one per acceptance criterion and edge
   case. Run the test suite to confirm they fail for the right reason.
3. Green: Write the minimum code to make the tests pass. No premature
   abstraction, no scope expansion beyond what the spec requires.
4. Refactor: Improve naming, remove duplication, check against
   04_conventions.md. Tests must stay green.
5. Update the spec's test case status column as you go
   (TODO → Red → Green → Refactored).
6. Update Progressive Disclosure docs if repo behaviour changed.
7. Use normal conventional commits. Add a Spec: SPEC-NNN trailer.
