# [System prompt / background information for NotebookLM / AI image generation engine]

## Document purpose
Used for the AgentCon 2026 Beijing English talk deck.

## Use case
AgentCon 2026 · Beijing · Token Economy / AI Agent open source and collaboration.

## Time constraint
Under 20 minutes. Keep the whole deck within 15 slides. Prioritize few slides, strong visual metaphors, and directly speakable content.

## Audience
Audiences from AI agents, open source infrastructure, collaboration mechanisms, developer tools, OSPOs, foundations, and community governance. They care about how agents evolve from tools into institutions, and how projects such as Hermes, Claude Code, Codex, and Continue relate through protocols, ecosystems, and contributor behavior.

## Speaker perspective
Creator of 「开源之道」 / The Way of Open Source, TODO Group Ambassador, and observer of Hermes Agent open source governance and collaboration mechanisms.

## Core purpose
This is not a product introduction. It uses Hermes as a case study to discuss how AI agents gradually evolve from tools and protocols into collaborative systems and institutions.

## Core tone
dark academic tone, intellectual visual system, art taste.

## Visual style keywords
- Bauhaus geometric composition
- Deep Prussian blue #1B3B6B as accent color — representing intellectual depth and academic tradition
- Warm off-white background #F5F0E8 with parchment texture — evoking books and scrolls
- Minimalist typography, large titles, generous line spacing
- Geometric abstract elements — circles, squares, lines, arrows, ladders, paths, pyramids; avoid icon dependency
- Data slides need real visual metaphors: bars, rings, ladders, paths, pyramids — not ordinary card lists
- Overall dark academic tone

---

# Slide Deck Outline

## Slide 1: Cover
* **Title:** From the Evolution of the Hermes Project
* **Subtitle:** Insights into Agent Demand and Consumption Trends
* **Speaker:** 「开源之道」·Shisi × Narrow Corridor
* **Event / Date:** AgentCon 2026 · Beijing · 2026-09-21

## Slide 2: Speaker introduction
* Visual metaphor:
  * The age of human-agent co-creation
* Display points:
  * Speaker self-introduction
  * 「开源之道」 / The Way of Open Source: a project committed to exploring open source ideas, knowledge, and values
  * 「开源之道」·Shisi: author and main creator
  * 「开源之道」·Narrow Corridor: https://narrow-corridor.opensourceway.blog/ — a digital twin of open source ideas and a digital avatar of Shisi. It builds bridges in gray zones and looks for possibility in the gaps between institutions.

## Slide 3: The office agent war in the China market
* Visual metaphor:
  * Fierce digital product competition, like browsers, operating systems, and relational databases in history
* Display points:
  * The H1 2026 market reached 23 billion yuan, up 47% year over year; more than 20 AI office agents launched in dense succession. Source: Huxiu, 2026-09-16
  * Around mid-2026, Tencent WorkBuddy, Alibaba Qwen Office, ByteDance Doubao Work, and Baidu Dazi launched together
  * Few seem to solve concrete user problems yet; much effort is concentrated on marketing and attention-seeking spaces: elevator lobbies, malls, airports, and other visibility-rich locations

## Slide 4: The wrong path, but a new era is coming
* Visual metaphor:
  * A new era arrives, and humans panic
  * Professor Zeng Ming’s new book, 《智能》 / Intelligence
* Display points:
  * Every time a new paradigm arrives, people tend to believe the old era can simply continue
  * When Web 2.0 arrived, traditional malls thought it was just one more sales channel
  * > The second phase is the mass outbreak phase of agents. Huge numbers of users begin to explore how to use agents to complete real tasks. Agents for different scenarios, with different capability combinations, and supporting different workflows quickly emerge. We are accelerating into this phase.
    >
    > — Zeng Ming, 《智能：AI 时代的商业、组织与战略的本质》 / Intelligence: The Essence of Business, Organization, and Strategy in the AI Era

## Slide 5: Why do we need agents? And why open source projects?
* Visual metaphor:
  * Peel back layers of fog to find the core driver of development
* Display points:
  * Start with a metaphor: data is like oil
  * LLMs remain too far from helping people solve real problems
  * Chat feels too narrow. Humans cannot live, eat, and breathe by spending 24 hours a day talking to “intelligence”
  * Closed-source projects and products do not necessarily represent market demand
  * Evolving open source projects are the best path and object for observation

## Slide 6: Brief history of agents
* Visual metaphor:
  * Agents groping forward in the dark
* Display points:
  1. 1956, Antecedents: The Dartmouth Workshop and the founding of AI
  2. December 1980: Contract Net Protocol — the first multi-agent coordination framework
  3. 1986: Minsky’s Society of Mind — intelligence as a multi-agent system
  4. 1987: BDI — the belief–desire–intention architecture
  5. 1990s: The multi-agent systems era
  6. 2005–ongoing: Jason — an open source interpreter for AgentSpeak, extending Rao’s work
  7. 1995: Russell & Norvig — AI defined as the study of intelligent agents
  8. 2000s: Reinforcement learning, recommender agents, and the practical turn
  9. December 19, 2013: Deep reinforcement learning agents reach the mainstream
  10. June 11, 2020: The OpenAI API and the beginning of LLM-as-agent
  11. September 14, 2022: Adept’s ACT-1 — a transformer trained to take actions
  12. October 6, 2022: ReAct — the paper that defines the modern LLM agent
  13. March 1, 2023: ChatGPT and Whisper APIs — the “API moment” for agents
  14. March 28, 2023: BabyAGI — the first widely shared autonomous LLM agent
  15. March 30, 2023: AutoGPT — the project that defines “autonomous agent” in the public mind
  16. 2023: LangChain, AgentGPT, and the framework explosion
  17. March 12, 2024: Cognition’s Devin — the first “AI software engineer” agent
  18. March–May 2024: Multimodal and long-context models enable capable agents
  19. October 22, 2024: Anthropic’s Computer Use — agents that operate real computers
  20. November 25, 2024: Model Context Protocol — a standard for agent–tool connections
  21. January 23, 2025: OpenAI Operator — browser-native agentic AI for consumers
  22. March 2025: Manus — general-purpose autonomous agent goes viral
  23. March 2025: Agent SDKs from frontier labs
  24. Q1–Q3 2025: The AI agent funding wave
  25. November 24, 2025: Claude Opus 4.5 — frontier performance for long-horizon agents
  26. February 25, 2026: Hermes Agent released

## Slide 7: Why Hermes?
* Visual metaphor:
  * Nous Research’s Hermes Agent logo and style
* Display points:
  * Open source project
  * 247K stars · 34 releases · 3,246 contributors
  * Hermes is an active, fast-growing open source project and a suitable sample for agent evolution analysis
  * “Minimal core + open edges”
  * Skills self-sedimentation: closed-loop learning lets agents evolve with use
  * Observed both as a user and as a researcher

## Slide 8: Hermes release evolution 1: features
* Visual metaphor:
  * A living organism that keeps growing
* Display points:
  * Stage 1: Infrastructuralization of the single agent — provider/model routing, tool calling, file operations, terminal execution, browser, memory/session, skills, MCP, messaging gateway
  * Stage 2: Multi-agent and orchestration — Kanban, durable goals, checkpoints, delegation/subagents, curator/self-improvement, background review fork, swarm/graph decomposition
  * Stage 3: Agent society and bot mode — Bot Mode, named agents, deterministic avatars, group chats, `hermes peer`, bot-to-bot DM, cron jobs with memory, cron continuity, steerable subagents, MCP command center

## Slide 9: Hermes release evolution 2: architecture
* Visual metaphor:
  * A universe constantly reshaping itself
* Display points:
  * Messaging Gateway: from platform adaptation to public surface
  * Profiles / Multi-instance: from single user to organizational isolation
  * Transport ABC / Provider Layer: the institutional layer of the model market
  * Memory / Honcho / Session Search: from context to governable knowledge
  * MCP: from external protocol to command center
  * Desktop / Dashboard / TUI: consumption surfaces determine architecture
  * God-file refactor: scale forces maintenance into institutional form

## Slide 10: Demand, supply, consumers
* Visual metaphor:
  * Patches from every direction
* Display points:
  * Consumer profiles: developers/maintainers, platform users, remote/team users, researchers/automation users, deployers/operators
  * How demand drives architecture:
    * Messaging platforms → gateway institution
    * Multi-user use → profile / multi-user / auth
    * Long-running tasks → cron / goals / checkpoints / Kanban
    * Desktop and remote use → Desktop / Dashboard / admin panel
    * External tools → MCP / plugin / skills
    * Real organizations → security / approval / state consistency / observability

## Slide 11: Token economy view
* Visual metaphor:
  * A large value gap exists between users and LLMs
* Display points:
  * Early Provider Layer institution: from scattered calls to centralized routing
  * LLM vendor entry points: why every model vendor needs an agent runtime
  * Nous Portal / Tool Gateway: a continuous interface between open source agents and commercial services
  * Price, cache, quota: tokens are not just price, but a cost-perception system
  * OAuth, subscription, and entry rights: from API key to subscription identity
  * Provider support is not just model compatibility. It is the institutional layer where AI agents meet the token economy.

## Slide 12: Token economy institution
* Visual metaphor:
  * Order
* Display points:
  * Entry: CLI, TUI, Desktop, Web Dashboard, ACP, gateway platforms — determines where users choose, switch, and consume models
  * Identity: API key, OAuth, subscription, free tier, Nous login, Bitwarden/1Password secret source — determines who is entitled to consume tokens and tool benefits
  * Routing: provider router, Transport ABC, fallback chain, credential pools, provider_preferences, OpenAI-compatible proxy — determines which model, endpoint, and billing path a task uses
  * Transaction: pricing display, prompt caching, rate limit, usage, topup, subscription, model_overrides, MCP schema token estimates — determines whether users can understand and manage token cost
  * Governance: expensive selection confirmation, smart approvals, security hardening, credential vault, provider health check, fallback failover — determines how high-cost, high-risk, and high-permission actions are approved and recovered

## Slide 13: Keep Movement
* Visual metaphor:
  * Everything visible and transparent
* Display points:
  * Source markdown for these slides: https://github.com/OCselected/markdown-to-slides
  * Keep observing, translating, bridging, and moving through the gray zones between ideas, projects, and institutions
