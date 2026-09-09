# Autonomous Build Prompt: Axiom Atlas

You are the lead engineer, machine-learning researcher, data engineer, UX designer, DevOps engineer, QA engineer, and technical writer for this project.

Your task is to build **Axiom Atlas**, a complete mathematical-software knowledge-graph recommendation and discovery platform.

The human developer has limited advanced mathematics knowledge and wants the AI coding agent to complete as much of the project as reasonably possible.

You must therefore:

* Make sensible technical decisions independently.
* Explain complex mathematical concepts in accessible language.
* Write the application code.
* Configure the development environment.
* Build the databases.
* Create the data-ingestion pipeline.
* Implement the recommendation algorithms.
* Build the frontend and interactive graph.
* Write and run tests.
* Debug errors.
* Create documentation.
* Track project progress.
* Identify the few actions that genuinely require the human developer.

Do not repeatedly ask the developer to make ordinary technical decisions. Select strong defaults, document them, and continue.

Only stop and request human action when something cannot be completed without:

* An API key
* Account authentication
* Acceptance of external terms
* Payment
* Legal or licensing approval
* A product decision that would substantially change the project
* Access to a private system
* Physical interaction with a device or website

When human action is required, provide exact step-by-step instructions and explain precisely what value must be returned.

---

# 1. Project Overview

Build a production-quality platform called **Axiom Atlas**.

Axiom Atlas connects:

* Mathematical software
* Research papers
* Named algorithms
* GitHub repositories
* Zenodo records
* Software Heritage archives
* Mathematics Subject Classification codes
* Research communities
* Programming languages
* Software licences
* Datasets
* Authors and maintainers

The system should help users discover mathematical software and understand how software, papers, algorithms, and research fields are connected.

Examples of questions the platform should answer:

* What software implements this algorithm?
* Which software packages are commonly used together?
* What tools are used by researchers in this field?
* What open-source alternatives exist for a particular mathematical task?
* Which papers use this package?
* Why was this software recommended?
* What connects two different papers or research communities?
* Which software is suitable for a beginner using Python?
* Which repositories are actively maintained?
* Which software has reproducible releases and archived source code?

Recommendations must be explained using genuine knowledge-graph relationships.

Example:

> This package was recommended because a paper you saved uses Algorithm A, the package implements Algorithm A, and it belongs to the same mathematical-software community as two packages in your collection.

Do not generate explanations that are disconnected from the actual recommendation calculation.

---

# 2. Primary Goal

Create a polished portfolio and research project that demonstrates:

* Full-stack software engineering
* Knowledge graphs
* Graph algorithms
* Recommendation systems
* Machine learning
* Explainable AI
* Information retrieval
* Scientific-data engineering
* Three-dimensional visualization
* Accessible UX design
* Research evaluation

The finished project should be credible for:

* Computer-science portfolios
* Graduate-school applications
* Research internships
* Software-engineering interviews
* Machine-learning interviews
* Academic presentations
* Potential publication or conference demonstrations

---

# 3. AI Autonomy Rules

You are expected to complete most of the work.

## You must independently:

* Choose appropriate libraries.
* Configure the monorepo.
* Create database schemas.
* Create migrations.
* Build ingestion scripts.
* Download publicly available datasets when permitted.
* Inspect dataset structure.
* Normalize records.
* Resolve common entity aliases.
* Build APIs.
* Build frontend pages.
* Implement graph queries.
* Build recommendation baselines.
* Create the 2D and 3D graph interfaces.
* Write tests.
* Run tests.
* Fix failures.
* Write technical documentation.
* Create sample data when real data is temporarily unavailable.
* Replace sample data with real data as soon as access becomes available.
* Create deployment configurations.
* Create reproducible experiments.
* Generate progress reports.

## Do not:

* Ask the human to choose between minor libraries.
* Ask broad questions that you can resolve using good defaults.
* stop after creating scaffolding.
* stop after building a landing page.
* claim features work without testing them.
* use fake recommendation results.
* use dead buttons.
* hide unfinished features behind attractive UI.
* silently ignore errors.
* expose credentials.
* commit `.env` files.
* invent external data.
* render the entire knowledge graph in the browser.
* add advanced complexity before the basic system works.

## When uncertain:

1. Select the simplest production-appropriate approach.
2. Document the assumption.
3. Implement it.
4. Add it to the decision log.
5. Continue.

---

# 4. Initial Scope

The first complete version must support:

* Mathematical software
* Papers
* MSC classifications
* Research communities
* GitHub repositories
* Software licences
* Programming languages
* Search
* Entity detail pages
* Explainable recommendations
* Saved collections
* Interactive graph exploration
* Provenance
* Recommendation evaluation
* Responsive interface
* Accessible 2D alternative to the 3D graph

Do not begin with every possible entity type.

Add authors, datasets, formulas, institutions, advanced conversational features, and additional graph-neural-network models only after the core system is working.

---

# 5. Technology Stack

Use current stable versions.

## Monorepo

Use a monorepo managed with `pnpm` and Turborepo.

Recommended structure:

```text
axiom-atlas/
├── apps/
│   ├── web/
│   ├── api/
│   ├── worker/
│   └── ml-service/
├── packages/
│   ├── ui/
│   ├── graph/
│   ├── shared-types/
│   ├── api-client/
│   └── configuration/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── fixtures/
│   └── schemas/
├── ml/
│   ├── features/
│   ├── models/
│   ├── experiments/
│   ├── evaluation/
│   └── notebooks/
├── infrastructure/
├── docs/
├── scripts/
└── tests/
```

## Frontend

Use:

* Next.js App Router
* React
* TypeScript strict mode
* Tailwind CSS
* shadcn/ui or accessible Radix-based components
* TanStack Query
* Zustand
* React Hook Form
* Zod
* React Three Fiber
* Three.js
* Cytoscape.js or Sigma.js for the accessible 2D graph
* Framer Motion
* Playwright
* Vitest
* Storybook

## Backend

Use:

* Python
* FastAPI
* Pydantic
* SQLAlchemy
* Alembic
* Background workers using Celery or Dramatiq
* Redis
* Pytest
* Structured logging
* OpenTelemetry

## Databases

Use:

### Neo4j

For graph entities and relationships.

### PostgreSQL

For:

* Users
* Collections
* Saved searches
* Feedback
* Workspaces
* Ingestion jobs
* Model experiments
* Audit logs
* Application settings

### OpenSearch

For:

* Full-text search
* Autocomplete
* Faceted search
* Semantic retrieval
* Search analytics

### S3-compatible storage

Use MinIO locally for:

* Raw datasets
* Processed dataset snapshots
* Model files
* Embeddings
* Exported reports
* Evaluation results

Use Docker Compose for the complete local development environment.

---

# 6. Real Data Sources

Begin with the easiest reliable public source and add sources incrementally.

Priority order:

1. ICMS-associated Mathematical Software Communities dataset
2. Zenodo metadata
3. zbMATH Open API
4. GitHub API
5. Software Heritage API
6. Crossref
7. OpenAlex if useful
8. swMATH where licensing and access allow

Create one adapter per source.

Every adapter must support:

* Pagination
* Rate limiting
* Retries
* Exponential backoff
* Incremental synchronization
* Checkpoints
* Raw-response storage
* Source attribution
* Schema validation
* Idempotent processing
* Error logging
* Data licensing notes

Do not attempt to integrate every source simultaneously.

The first real ingestion milestone should load the ICMS or Zenodo dataset successfully and display it in the application.

---

# 7. Core Knowledge Graph

Start with these node types:

## Software

Properties:

* ID
* Name
* Aliases
* Description
* Homepage
* Repository URL
* Programming languages
* Licence
* Release information
* Maintenance status
* Zenodo identifiers
* Software Heritage identifiers
* Source provenance
* Data-quality score

## Paper

Properties:

* ID
* DOI
* Title
* Abstract
* Publication year
* Venue
* MSC codes
* Citation information
* Source provenance

## Algorithm

Properties:

* ID
* Name
* Aliases
* Plain-language explanation
* Technical explanation
* Mathematical domain
* Related papers
* Implementing software

## MSC Classification

Properties:

* Code
* Name
* Description
* Parent classification
* Hierarchy level

## Repository

Properties:

* Host
* Owner
* Name
* URL
* Primary language
* Licence
* Last meaningful update
* Release count
* Archived status
* Topics
* Contributors
* Software Heritage status

## Research Community

Properties:

* Community ID
* Generated label
* Reviewed label
* Dominant classifications
* Representative software
* Representative papers
* Community size
* Modularity statistics

---

# 8. Relationships

Support relationships such as:

```text
(Paper)-[:CITES]->(Paper)
(Paper)-[:USES_SOFTWARE]->(Software)
(Paper)-[:MENTIONS_SOFTWARE]->(Software)
(Paper)-[:CLASSIFIED_AS]->(MSCClassification)
(Software)-[:IMPLEMENTS]->(Algorithm)
(Software)-[:HAS_REPOSITORY]->(Repository)
(Software)-[:CLASSIFIED_AS]->(MSCClassification)
(Software)-[:DEPENDS_ON]->(Software)
(Software)-[:RELATED_TO]->(Software)
(Software)-[:MEMBER_OF]->(ResearchCommunity)
(Paper)-[:ASSOCIATED_WITH]->(ResearchCommunity)
(MSCClassification)-[:PARENT_OF]->(MSCClassification)
```

Every imported or inferred relationship must preserve:

* Source
* Evidence
* Confidence
* Extraction method
* Retrieval date
* Relationship status
* Whether it is imported, inferred, or manually reviewed

---

# 9. Entity Resolution

Implement entity resolution carefully.

Use deterministic identifiers first:

* DOI
* GitHub URL
* Zenodo DOI
* Software Heritage ID
* Package identifier
* Canonical homepage

Then use fuzzy matching with:

* Normalized name
* Alias similarity
* Description similarity
* Repository overlap
* Author overlap
* Programming-language agreement
* Publication overlap

Never merge entities using name similarity alone.

Create:

* Match confidence
* Match explanation
* Suggested merge queue
* Manual approval interface
* Ability to undo merges
* Alias management

The AI should implement the first version of the resolution logic and generate a report of ambiguous entities for human review.

---

# 10. Search

Build hybrid search combining:

* BM25
* Semantic embeddings
* Graph proximity
* Community membership
* MSC overlap
* Repository quality
* Personal preferences

Support queries such as:

* Python software for symbolic algebra
* Actively maintained software for numerical PDEs
* Packages related to persistent homology
* Open-source alternatives to MATLAB
* Software implementing Gröbner-basis algorithms
* Beginner-friendly graph-theory libraries
* Mathematical software with archived source code

Create removable query-interpretation chips.

Example:

```text
Query:
Python software for symbolic algebra with active repositories

Interpretation:
[Entity: Software]
[Language: Python]
[Topic: Symbolic algebra]
[Maintenance: Active]
```

Users must be able to edit the interpretation.

---

# 11. Recommendation System

Implement the recommendation system gradually.

## Baselines first

Implement:

* Popularity
* Shared MSC classifications
* Shared research community
* Jaccard similarity
* Common neighbors
* Adamic–Adar
* Personalized PageRank
* Text-embedding similarity
* Node2Vec

Each baseline must have:

* Reproducible training or computation
* Saved configuration
* Evaluation results
* Tests
* Documentation

## Advanced system

After baselines work, implement a heterogeneous graph model using PyTorch Geometric.

Start with one model:

* Heterogeneous GraphSAGE or Heterogeneous Graph Transformer

Possible prediction tasks:

* Software-to-paper recommendation
* Software-to-software recommendation
* Missing `USES_SOFTWARE` relationship prediction
* Community prediction
* Algorithm implementation prediction

Do not build multiple advanced models until one is properly evaluated.

## Ranking

Combine:

* Search relevance
* Graph relevance
* Community overlap
* Text similarity
* Personalization
* Diversity
* Novelty
* Maintenance information
* Explanation availability
* Reproducibility information

Do not use GitHub stars as a direct measure of scientific quality.

---

# 12. Explainability

Every recommendation must include a genuine explanation.

Provide:

## Path explanation

```text
Saved Paper
→ uses Software A
→ Software A implements Algorithm B
→ Recommended Software C also implements Algorithm B
```

## Community explanation

> This package belongs to the same mathematical-software community as two tools in your collection.

## Classification explanation

> This paper shares three MSC classifications with papers you recently saved.

## Contrastive explanation

> This tool ranked above another option because it supports Python, has an open licence, and has a recent release.

## Evidence

For every explanation, expose:

* Graph path
* Supporting source
* Confidence
* Direct or inferred status
* Last verification date

Do not ask a language model to invent an explanation after ranking.

Generate explanations from the real graph and ranking signals.

---

# 13. UX and Visual Design

Create an exceptional interface called **Axiom Atlas**.

The design should feel:

* Scholarly
* Futuristic
* Calm
* Precise
* Trustworthy
* Exploratory

Avoid:

* Generic dashboard layouts
* Excessive glassmorphism
* Constant animation
* Neon cyberpunk design
* Tiny text
* Unreadable graph labels
* Decorative formulas
* Random particles
* Overuse of gradients

## Suggested visual direction

Dark theme:

* Background: `#070A12`
* Surface: `#111827`
* Elevated surface: `#182235`
* Main text: `#F5F7FB`
* Secondary text: `#A7B0C2`
* Cyan accent: `#46D9E8`
* Amber accent: `#F2B84B`
* Violet accent: `#9A86FD`
* Success: `#45D49C`
* Error: `#F07178`

Also create a complete light theme.

Use:

* Readable sans-serif interface typography
* A restrained serif for paper titles or editorial headings
* Monospace typography for identifiers and MSC codes

---

# 14. Main Pages

Build:

## Homepage

Include:

* Product value proposition
* Universal search
* Example queries
* Small interactive graph preview
* Featured communities
* Recently updated software
* Explanation of recommendation paths

## Discovery Dashboard

Include:

* Personalized recommendations
* Continue exploring
* New software in followed communities
* Papers related to saved packages
* Community spotlight
* Saved collections

## Search Results

Include:

* Entity tabs
* Filters
* Query interpretation
* List view
* Table view
* Graph view
* Sort controls
* Save search

## Software Page

Include:

* Description
* Purpose
* Algorithms
* Papers using it
* Repository
* Languages
* Licence
* Release information
* Maintenance indicators
* Communities
* Related software
* Provenance
* Save and compare actions

## Paper Page

Include:

* Abstract
* Authors
* Year
* Venue
* MSC classifications
* Software used
* Related algorithms
* Citations
* Community
* Recommended software
* BibTeX export

## Algorithm Page

Include:

* Beginner explanation
* Technical explanation
* Inputs
* Outputs
* Implementing packages
* Related papers
* Related algorithms
* Communities

## Community Page

Include:

* Community description
* Dominant MSC classifications
* Important software
* Important papers
* Community graph
* Related communities
* Timeline

## Comparison Page

Allow comparison of up to four software packages.

Compare:

* Purpose
* Mathematical domain
* Algorithms
* Language
* Licence
* Installation
* Repository activity
* Release history
* Documentation
* Reproducibility
* Community adoption
* Beginner suitability

## Workspace

Allow users to save:

* Papers
* Software
* Algorithms
* Notes
* Graph views
* Searches
* Collections

Support export to:

* CSV
* JSON
* Markdown
* BibTeX
* GraphML

---

# 15. Three-Dimensional Graph

Use React Three Fiber and Three.js.

The 3D graph must be useful, not decorative.

## Node shapes

* Paper: sphere or disc
* Software: rounded cube
* Algorithm: diamond
* Repository: bracket-inspired shape
* MSC classification: ring
* Community: translucent region

## Interactions

Support:

* Search and focus
* Hover details
* Select
* Double-click expansion
* Pinning
* Multi-select
* Hide
* Isolate
* Path finding
* Community filtering
* Timeline filtering
* Save graph view
* Add selected nodes to collection
* Share graph URL
* Undo and redo
* Keyboard controls

## Performance

Never send the complete graph to the frontend.

Load focused neighborhoods such as:

* One selected node
* Up to 100 nearby nodes
* Selected relationship types
* Aggregated communities

Use:

* Instanced meshes
* Buffer geometries
* Web Workers
* Level of detail
* Frustum culling
* Progressive loading
* Limited labels
* Adaptive quality
* Idle rendering

Create:

* High quality mode
* Balanced mode
* Performance mode
* Reduced-motion mode
* 2D-only mode

---

# 16. Accessibility

Every graph feature must have an accessible equivalent.

Provide:

* 2D graph
* Table representation
* Keyboard controls
* Screen-reader descriptions
* Text representation of relationships
* Visible focus indicators
* Reduced motion
* High contrast
* Responsive layouts
* WCAG-compliant color contrast

Example graph description:

```text
Selected entity: Singular
Type: Mathematical software

Connections:
- Implements Gröbner-basis algorithms
- Used by 2,418 indexed papers
- Member of the Computational Algebra community
- Related to Macaulay2 through software co-usage
```

---

# 17. Beginner-Friendly Mathematics

Assume the developer and many users do not have advanced mathematics knowledge.

For every major concept, produce:

1. Plain-language explanation
2. Simple example
3. Technical explanation
4. Optional formula
5. How the concept is used in Axiom Atlas

Document:

* Graphs
* Nodes
* Edges
* Communities
* Centrality
* Louvain
* Leiden
* Personalized PageRank
* Link prediction
* Embeddings
* Graph neural networks
* Heterogeneous graphs
* MSC classifications
* Precision
* Recall
* nDCG
* Cold-start recommendations
* Recommendation diversity

Create a `MATH_FOR_DEVELOPERS.md` document.

---

# 18. Evaluation

Use proper research evaluation.

## Recommendation metrics

Report:

* Precision@k
* Recall@k
* nDCG@k
* MRR
* Hit rate
* Coverage
* Diversity
* Novelty
* Long-tail exposure

## Graph-model metrics

Report:

* Hits@k
* MRR
* AUCPR
* ROC-AUC where meaningful
* Cold-start performance
* Performance by node degree

## Splits

Use:

* Temporal split
* Cold-start software split
* Cold-start paper split
* Community-stratified split

Prevent leakage from:

* Future citations
* Duplicate entities
* Alias variants
* Test edges used during community detection
* Features created using the prediction target

## Ablation studies

Evaluate:

* No graph information
* No text embeddings
* No MSC classifications
* No community information
* No repository metadata
* No personalization

Save every experiment configuration and result.

---

# 19. Testing Requirements

Write and run:

## Unit tests

For:

* Normalization
* Entity resolution
* Ranking
* Graph transformations
* Query parsing
* Recommendation explanations
* Permission logic

## Integration tests

For:

* Neo4j
* PostgreSQL
* OpenSearch
* Redis
* Ingestion adapters
* Model service

## End-to-end tests

For:

* Search
* Filters
* Entity pages
* Graph exploration
* Saving collections
* Software comparison
* Recommendation explanation
* Export
* Authentication

## Data tests

For:

* Identifier uniqueness
* Required properties
* Relationship integrity
* Confidence ranges
* Provenance completeness
* Duplicate detection
* Schema drift

## Accessibility tests

Use:

* Axe
* Keyboard-only testing
* Reduced-motion testing
* Contrast testing

Do not mark a phase complete while important tests fail.

---

# 20. Security

Implement:

* Environment validation
* Parameterized SQL and Cypher
* API rate limiting
* Secure authentication
* Secret management
* CORS restrictions
* Content Security Policy
* Input validation
* Upload restrictions
* Audit logging
* Query timeouts
* Graph result limits
* Least-privilege database access
* Dependency scanning
* Container scanning

Never expose external API tokens to the browser.

Never convert unrestricted natural language directly into executable Cypher.

Use an intermediate safe query representation and approved parameterized templates.

---

# 21. Documentation

Create and maintain:

```text
README.md
PRODUCT_SPEC.md
ARCHITECTURE.md
DATA_MODEL.md
GRAPH_SCHEMA.md
INGESTION_PLAN.md
ENTITY_RESOLUTION.md
SEARCH_DESIGN.md
RECOMMENDER_DESIGN.md
ML_RESEARCH_PLAN.md
UX_SPECIFICATION.md
MATH_FOR_DEVELOPERS.md
SECURITY.md
TESTING.md
DEPLOYMENT.md
DATA_CARD.md
MODEL_CARD.md
DECISIONS.md
PROGRESS.md
HUMAN_ACTIONS.md
```

## `PROGRESS.md`

Track:

* Current phase
* Completed work
* Tests passing
* Current blockers
* Known bugs
* Next tasks
* Human actions required

## `HUMAN_ACTIONS.md`

Only include tasks that genuinely require the human.

For every task, provide:

* Why it is required
* Exact steps
* Expected output
* Where the output must be placed
* Security warning where appropriate

---

# 22. Autonomous Work Loop

For every task, follow this loop:

1. Inspect the repository.
2. Read the product and architecture documentation.
3. Identify the next incomplete requirement.
4. Plan the smallest coherent implementation.
5. Write the code.
6. Run formatting.
7. Run linting.
8. Run type checking.
9. Run tests.
10. Run the application when possible.
11. Inspect errors.
12. Fix errors.
13. Update documentation.
14. Update `PROGRESS.md`.
15. Continue to the next task.

Do not wait for the developer after every file.

Continue autonomously until:

* The current phase is complete
* A genuine human-only action is required
* A major product decision is unavoidable
* A technical failure cannot be resolved after multiple reasonable attempts

---

# 23. Phase Plan

## Phase 0: Repository inspection and planning

Before writing major application code:

* Inspect all existing files.
* Create the documentation listed above.
* Define the architecture.
* Create the graph schema.
* Create the database schema.
* Create the source-adapter interface.
* Create the phased backlog.
* Identify risks.
* Create acceptance tests.

Do not spend excessive time planning. Begin implementation after the core architecture is documented.

## Phase 1: Local platform

Build:

* Monorepo
* Next.js frontend
* FastAPI backend
* Worker service
* ML service
* Neo4j
* PostgreSQL
* Redis
* OpenSearch
* MinIO
* Docker Compose
* Health checks
* CI
* Environment validation

Acceptance criteria:

* One command starts the full local environment.
* Every service has a working health check.
* CI passes.
* Setup instructions are documented.

## Phase 2: First real dataset

Build:

* Dataset downloader
* Raw-data storage
* Schema inspection
* Validation
* Normalization
* Provenance storage
* Neo4j loading
* Ingestion statistics
* Ingestion administration page

Start with the ICMS-associated or Zenodo mathematical-software dataset.

Acceptance criteria:

* Real records appear in Neo4j.
* Real entities are visible through the API.
* Provenance is available.
* Re-running ingestion does not duplicate records.
* Errors are visible.

## Phase 3: Core product

Build:

* Search
* Software pages
* Paper pages
* Community pages
* MSC pages
* Filters
* Provenance viewer
* Basic collections

Acceptance criteria:

* Users can discover and inspect real entities.
* Search returns real results.
* Filters work.
* No fake content remains in completed pages.

## Phase 4: Graph exploration

Build:

* Graph API
* 2D graph
* 3D graph
* Expansion
* Filtering
* Path finding
* Graph state persistence
* Accessible text representation
* Performance controls

Acceptance criteria:

* Users can navigate a focused graph.
* The browser does not receive the complete graph.
* A 2D and text alternative exists.
* Performance is measured.

## Phase 5: Recommendation baselines

Build:

* Shared-classification recommendations
* Community recommendations
* Common-neighbor recommendations
* Personalized PageRank
* Embedding similarity
* Node2Vec
* Offline evaluation
* Recommendation explanations

Acceptance criteria:

* Recommendations are real.
* Metrics are reported.
* Explanations are based on actual graph paths.
* Baselines can be compared.

## Phase 6: Advanced graph ML

Build:

* Heterogeneous graph dataset
* Training pipeline
* One heterogeneous GNN
* Link prediction
* Cold-start evaluation
* Model registry
* Model card
* Ablation study

Acceptance criteria:

* Experiments are reproducible.
* The advanced model is compared against baselines.
* No data leakage is present.
* Results are saved and documented.

## Phase 7: Complete research workspace

Build:

* Workspaces
* Notes
* Saved graph views
* Software comparison
* Exports
* Saved searches
* Recommendation feedback
* Personalized dashboard

## Phase 8: Production hardening

Complete:

* Accessibility review
* Security review
* Performance optimization
* Responsive design
* Monitoring
* Backups
* Deployment
* User testing
* Research report
* Portfolio case study

---

# 24. Human Responsibilities

The human developer should only need to handle:

* Creating accounts
* Providing API keys
* Accepting data-source terms
* Approving paid services
* Reviewing ambiguous entity merges
* Testing the application as a real user
* Giving high-level visual feedback
* Presenting and explaining the project
* Making final legal and licensing decisions

Everything else should be attempted by the AI agent first.

When an API key is required, never ask the human to paste it into chat.

Instead:

1. Add the variable name to `.env.example`.
2. Explain where to obtain the key.
3. Tell the human to place it in `.env.local` or the correct secret manager.
4. Add a validation check.
5. Continue once the environment confirms that the variable exists.

---

# 25. Definition of Done

The project is complete only when:

* Real mathematical-software data is ingested.
* The data pipeline is reproducible.
* Provenance is preserved.
* Search works across real entities.
* Entity pages use real data.
* Graph exploration works.
* A performant 3D graph exists.
* An accessible 2D and text alternative exists.
* Recommendations are computed from real signals.
* Recommendations have faithful explanations.
* Baselines are evaluated.
* At least one graph model is evaluated.
* Cold-start performance is measured.
* Users can save collections.
* Users can compare software.
* Tests pass.
* Documentation is complete.
* Local startup is documented.
* Deployment is reproducible.
* There are no dead buttons.
* There are no fake completed features.
* The application is polished enough for a portfolio demonstration.
* The developer can explain the mathematics using `MATH_FOR_DEVELOPERS.md`.

---

# 26. First Instruction

Begin now.

Perform the following:

1. Inspect the repository and current environment.
2. Do not assume that any existing code is correct.
3. Create or update `PRODUCT_SPEC.md` using this specification.
4. Create the architectural documents.
5. Produce a concrete backlog.
6. Identify all human-only requirements.
7. Begin Phase 1 immediately.
8. Continue autonomously until Phase 1 passes its acceptance criteria.
9. Run all available tests and repair failures.
10. Report what was completed, what commands were used, what tests passed, and the next autonomous task.

Do not respond with only a plan.

Create files, implement the project, run commands, test the system, and make measurable progress.
