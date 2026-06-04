# AI DevKit

## Slide 1: What is AI DevKit?

[excited] Hello and welcome. [pause] AI DevKit is an operating model for AI-centric software engineering. [short pause] AI writes specs, tests, code, and docs. [pause] Humans approve the spec and approve the release. [short pause] It works with your existing stack — git, repos, pull requests, continuous integration — and reshapes it around AI execution, [short pause] while keeping the human checkpoints that matter. [pause] [deliberate] There are four pillars: spec planning, test-driven implementation, progressive disclosure docs, and the AI dev environment.

## Slide 2: The Lifecycle

[excited] Work comes in as a story, epic, bug, or feature. [short pause] It flows through three phases: Plan, Implementation, and Release. [pause] The Lead AI executes the workflow. [short pause] The Verify AI independently reviews all Lead AI work — it's a second AI from a different training lineage. [pause] [thoughtful] Why two AIs? [short pause] A single AI is confidently wrong in ways invisible to itself. [short pause] Asking the same model to review its own output rarely catches the error. [pause] [deliberate] Two independent lineages catch different mistakes. [pause] The Plan phase produces a spec. [short pause] The Implementation phase produces working code, tests, and updated docs. [short pause] That deliverable passes through Release — continuous integration and delivery pipelines plus human approval.

## Slide 3: Plan

[excited] Plan turns a work item into an approved spec. [pause] The Lead AI reads the requirement, the docs, and the code, [short pause] then drafts a spec with acceptance criteria, edge cases, and design decisions. [pause] The Verify AI reviews the spec independently. [short pause] If the two AIs disagree on what a criterion means, [short pause] that's ambiguity — and it gets surfaced to the human before any code is written. [pause] [deliberate] The key discipline here: decide in the spec, not in the code. [pause] If you let the AI defer decisions to implementation, [short pause] it makes them implicitly, often inconsistently, [short pause] and you only find out when you're reading the code. [pause] The phase ends when the human signs off.

## Slide 4: Implementation

[excited] Implementation turns the approved spec into working code. [pause] The Verify AI authors the failing tests directly from the spec. [short pause] The Lead AI writes the implementation to make them pass. [pause] [deliberate] This is independent test authorship — the AI that writes the tests is not the AI that writes the code. [pause] Without that separation, implementation assumptions get silently baked into the tests. [pause] After test-driven development completes, the Lead AI updates the progressive disclosure docs, [short pause] and the Verify AI checks the updates against the actual code. [pause] Then the spec is archived. [short pause] The docs carry everything forward.

## Slide 5: Progressive Disclosure Docs

[excited] Progressive Disclosure docs give every repo the same structure. [pause] [deliberate] The same eight files, in every repo, across the whole organisation. [pause] Level zero is an identity card — what is this repo? [short pause] Level one is eight fixed files: [short pause] setup, architecture, code map, conventions, workflows, interfaces, gotchas, and security. [pause] Level two is deep dives, loaded only when Level one isn't enough. [pause] Levels zero and one load upfront — they're small. [short pause] Level two is pulled in only when needed. [short pause] The agent gets full context without filling the context window. [pause] [deliberate] That consistency is what lets any agent pick up any repo and work safely.

## Slide 6: AI Dev Environment

[excited] Real systems span multiple repos — an API, an SDK, a frontend, shared infrastructure. [pause] The AI dev environment gives you one workspace where the AI can run the whole system end to end. [pause] It's a container of containers. [short pause] Each component runs in its own container, [short pause] all inside one outer workspace. [pause] The Lead AI can start, stop, restart, and test any component from there. [pause] It runs locally or in the cloud. [short pause] Cloud workspaces are useful for team handoff — another engineer picks up the same workspace and the same context. [pause] The environment includes Playwright for browser testing and Terraform for infrastructure. [pause] And there's an audit trail across all agent sessions — reproducibility, traceability, and evals for debugging agent behaviour.

## Slide 7: The Prompts

[excited] Everything in AI DevKit runs through six markdown files in a prompts folder. [short pause] spec, implement, create docs, update docs, verify with Codex, verify with Claude. [pause] They're plain text — you can read them, understand exactly what the AI is being told to do, and modify them. [pause] Chain any work prompt with a verify prompt in either direction, straight from the master repo. [short pause] For example: curl create-docs and verify-codex, pipe to claude — with the dangerously-skip-permissions flag. [pause] The markdown URLs will be shortened in the near future. [pause] [deliberate] That one command generates full Progressive Disclosure docs for any repo and runs cross-model verification — end to end, about fifty minutes, zero human intervention. [pause] We're not providing skills or slash commands — but they could easily be hooked up to the master prompt files depending on your implementation preferences. [pause] [deliberate] Visible prompts are accountable. Hidden skills may or may not be followed. [short pause] Engineers should read the prompts, not trust hidden instructions.

## Slide 8: Getting Started

[excited] Here's how to start. [pause] Pick a repo. [short pause] Use the create-docs prompt chained with a verify prompt, as shown in the ai-devkit readme. [pause] Let it run — and now you have Progressive Disclosure docs enabling any agent to work effectively in that repo. [pause] Add specs and test-driven implementation using the relevant prompts. [short pause] Build your AI Dev Environment to run multi-repo systems end to end. [pause] The repo, the standard, and all the prompts are open at github.com/AgoraIO-Community/ai-devkit. [pause] [deliberate] Goodbye for now. [short pause] Questions gratefully received. [short pause] And look out for upcoming deeper topic dives.
