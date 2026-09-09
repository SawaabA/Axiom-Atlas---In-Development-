Mathematical Software Knowledge Graph

Act as a combined:

Principal software architect
Senior full-stack engineer
Graph machine-learning researcher
Data engineer
UX design lead
Accessibility specialist
DevOps engineer
Technical writer

Build a complete, production-quality platform named Axiom Atlas.

This is not an MVP, hackathon mockup, landing page, or simple graph visualization. Build the full research and discovery platform described below. Develop it incrementally, but architect every component for the complete system from the beginning.

Do not replace real functionality with mock data, static cards, fake AI responses, placeholder buttons, or hard-coded recommendations. When external data cannot immediately be accessed, create a clearly documented local ingestion fixture that follows the real production schema.

1. Product Vision

Axiom Atlas is a recommendation, search, and discovery platform for mathematical research software.

It connects:

Mathematical papers
Software packages
Named algorithms
GitHub repositories
Software Heritage archives
Zenodo records
Datasets
Authors and maintainers
Mathematical concepts
Mathematics Subject Classification codes
Programming languages
Licences
Research institutions
Conferences and journals
Software dependencies
Research communities
Formula or notation entities when reliable extraction is possible

The platform must answer questions such as:

What software implements this algorithm?
What packages are commonly used together?
Which package is most relevant for my paper?
What are modern alternatives to an older mathematical package?
Which papers introduced, evaluated, extended, or used this software?
What software communities overlap with numerical analysis and machine learning?
Which repositories are actively maintained and reproducible?
Why was this paper, package, or algorithm recommended?
What path connects two apparently unrelated research areas?
Which mathematical tools should I learn for a particular research problem?
Which package is appropriate for a beginner using Python?
What software is associated with a given MSC classification?
Which research software lacks an archived version, clear licence, or reproducible release?

Recommendations must be explainable through graph paths such as:

This paper was recommended because it uses Algorithm A, Algorithm A is implemented by Package B, and Package B is commonly cited by papers in a community you follow.

The product should feel like a combination of:

A scholarly search engine
A software discovery platform
An interactive scientific atlas
A research workspace
An explainable recommender
A knowledge-graph browser
2. Target Users

Support these primary users:

Students

Students may not have a strong mathematical background. They need:

Plain-language explanations
Beginner-friendly software comparisons
Definitions of mathematical classifications
Installation and language information
Suggested learning paths
Explanations of why tools are relevant
Researchers

Researchers need:

Precise search and filtering
Citation and provenance information
Related software and papers
Reproducibility signals
Saved research collections
BibTeX and structured exports
Explainable recommendations
Research Software Engineers

They need:

Dependency relationships
Repository activity
Version and release histories
Licence information
Software Heritage identifiers
Package alternatives
Community adoption signals
Librarians and Knowledge Curators

They need:

Entity-resolution tools
Metadata provenance
Duplicate detection
Correction workflows
Classification coverage
Audit trails
Platform Administrators

They need:

Ingestion monitoring
Failed job inspection
API usage tracking
Data-quality dashboards
Model evaluation
User and access management
3. Core Product Principles
Every recommendation must be explainable.
Every imported fact must preserve provenance.
The interface must remain useful without the 3D visualization.
Mathematical expertise must not be required to begin exploring.
Advanced users must still have access to precise filters and technical metadata.
Never present inferred relationships as confirmed facts.
Display confidence and evidence for machine-generated relationships.
Accessibility and performance are product requirements, not later enhancements.
Use 3D only where it helps users understand graph structure.
Respect source licences, API terms, robots policies, rate limits, and attribution requirements.
4. Full Technology Architecture

Use current stable versions at implementation time. Pin dependencies and document version choices.

Monorepo

Use a monorepo with a structure similar to:

axiom-atlas/
├── apps/
│   ├── web/
│   ├── api/
│   ├── ingestion-worker/
│   ├── ml-service/
│   └── documentation/
├── packages/
│   ├── ui/
│   ├── graph-visualization/
│   ├── shared-types/
│   ├── api-client/
│   ├── configuration/
│   └── testing/
├── data/
│   ├── schemas/
│   ├── fixtures/
│   └── migrations/
├── ml/
│   ├── datasets/
│   ├── features/
│   ├── baselines/
│   ├── models/
│   ├── evaluation/
│   └── notebooks/
├── infrastructure/
│   ├── docker/
│   ├── terraform/
│   ├── kubernetes/
│   └── monitoring/
├── docs/
├── scripts/
└── .github/workflows/
Frontend

Use:

Next.js App Router
React
TypeScript with strict mode
React Three Fiber
Three.js
Tailwind CSS
An accessible component system such as shadcn/ui and Radix primitives
TanStack Query
Zustand or another lightweight local state solution
React Hook Form and schema validation
Framer Motion for restrained interface motion
Web Workers for graph layouts and expensive client-side calculations
Playwright for end-to-end testing
Storybook for reusable UI documentation
Backend

Use:

Python
FastAPI
Pydantic
SQLAlchemy and Alembic
Background workers using Celery, Dramatiq, or an equivalent reliable queue
Redis for caching, queues, rate limiting, and short-lived graph sessions
Structured logging
OpenTelemetry
REST endpoints with an OpenAPI contract
WebSockets or Server-Sent Events for long-running ingestion and graph-expansion jobs

Use GraphQL only when it provides a clear advantage. Do not add it merely for trendiness.

Storage

Use the correct database for each responsibility:

Neo4j

Store canonical graph entities and relationships.

PostgreSQL

Store:

Users
Accounts
Saved searches
Collections
Workspaces
Feedback
Permissions
Ingestion-job records
Source configurations
Model registry metadata
Recommendation impressions
Click and save events
Administrative audit logs
OpenSearch

Store:

Full-text paper and software indexes
BM25 fields
Facets
Autocomplete terms
Semantic vectors where appropriate
Search analytics
Object Storage

Use S3-compatible object storage or MinIO for:

Raw source responses
Dataset snapshots
Model checkpoints
Embeddings
Export files
Data-quality reports
Training artifacts

Do not store copyrighted full-text papers unless legally permitted. Prefer metadata, abstracts, permitted snippets, identifiers, and links.

5. Initial Data Sources

Implement each source through an independent adapter.

Begin with:

The ICMS-associated Mathematical Software Communities dataset on Zenodo
swMATH metadata where access and licensing permit
zbMATH Open API
GitHub REST or GraphQL APIs
Zenodo API
Software Heritage API
Crossref for DOI normalization and bibliographic enrichment
ORCID where permitted
OpenAlex as an optional enrichment source
arXiv metadata or HTML where appropriate and legally permitted

Each adapter must support:

Rate limiting
Retries with exponential backoff
Pagination
Resume checkpoints
Raw-response preservation
Source timestamps
Data licences
Incremental updates
Idempotent reprocessing
Schema versioning
Clear failure reporting

Never scrape a source when an approved API or downloadable dataset is provided.

6. Knowledge Graph Schema

Create a typed heterogeneous knowledge graph.

Primary Node Types
Paper

Properties:

Canonical ID
DOI
zbMATH identifier
arXiv identifier
Title
Abstract where available
Publication year
Venue
Authors
MSC classifications
Keywords
Citation count
Source provenance
Embeddings
Data completeness score
Software

Properties:

Canonical software ID
Official name
Aliases
Description
Homepage
Languages
Operating systems
Licence
Installation methods
Current status
First and latest known release
Repository links
Software Heritage IDs
Zenodo records
Package-manager identifiers
Maintenance indicators
Reproducibility indicators
Algorithm

Properties:

Canonical name
Aliases
Short explanation
Mathematical domain
Input/output description
Complexity information when reliable
Original or foundational references
Related algorithms
Repository

Properties:

Host
Owner
Name
URL
Primary language
Stars
Forks
Open issues
Archived state
Last meaningful commit
Release information
Licence
Topics
Contributors
Software Heritage archive status
Dataset

Properties:

DOI
Title
Description
Licence
Authors
Version
Repository
Associated papers and software
Author

Properties:

Canonical identifier
Display name
Name variants
ORCID
Affiliations
Research areas
MSCConcept

Represent both top-level and nested Mathematics Subject Classification concepts.

Properties:

Code
Label
Description
Parent code
Depth
ResearchCommunity

Properties:

Community ID
Generated label
Human-reviewed label
Top software
Top papers
Dominant MSC codes
Size
Modularity statistics
Description
Confidence
Institution
Venue
Licence
ProgrammingLanguage
MathematicalConcept
Release
FormulaExpression

Only create formula entities when the source and extraction confidence are strong enough. Preserve the original representation and evidence.

7. Relationship Types

Implement typed relationships such as:

(Paper)-[:CITES]->(Paper)
(Paper)-[:USES_SOFTWARE]->(Software)
(Paper)-[:MENTIONS_SOFTWARE]->(Software)
(Paper)-[:INTRODUCES]->(Software)
(Paper)-[:EVALUATES]->(Software)
(Paper)-[:IMPLEMENTS_ALGORITHM]->(Algorithm)
(Software)-[:IMPLEMENTS]->(Algorithm)
(Software)-[:DEPENDS_ON]->(Software)
(Software)-[:RELATED_TO]->(Software)
(Software)-[:HAS_REPOSITORY]->(Repository)
(Software)-[:HAS_RELEASE]->(Release)
(Software)-[:ARCHIVED_AS]->(SoftwareHeritageRecord)
(Software)-[:DEPOSITED_IN]->(ZenodoRecord)
(Software)-[:WRITTEN_IN]->(ProgrammingLanguage)
(Software)-[:LICENSED_UNDER]->(Licence)
(Paper)-[:CLASSIFIED_AS]->(MSCConcept)
(Software)-[:CLASSIFIED_AS]->(MSCConcept)
(Author)-[:AUTHORED]->(Paper)
(Author)-[:MAINTAINS]->(Software)
(Author)-[:AFFILIATED_WITH]->(Institution)
(Paper)-[:PUBLISHED_IN]->(Venue)
(Software)-[:MEMBER_OF]->(ResearchCommunity)
(Paper)-[:ASSOCIATED_WITH]->(ResearchCommunity)
(Algorithm)-[:RELATED_TO]->(MathematicalConcept)
(MSCConcept)-[:PARENT_OF]->(MSCConcept)

Every relationship must include, where relevant:

Source
Evidence type
Evidence excerpt or reference
Extraction method
Confidence
Creation timestamp
Last verification timestamp
Schema version
Whether it was asserted, imported, inferred, or manually curated
8. Entity Resolution

Create a serious entity-resolution pipeline.

Deterministic Matching

Use:

DOI
zbMATH IDs
GitHub repository URLs
Zenodo DOI
Software Heritage IDs
ORCID
Package registry identifiers
Canonicalized homepage URLs
Fuzzy Matching

Use:

Normalized software names
Aliases
Author overlap
Repository similarity
Description similarity
Citation overlap
Programming-language agreement
Temporal compatibility
Resolution Workflow

Each match must produce:

Match confidence
Matched features
Contradicting features
Source priority
Merge decision
Audit record

Ambiguous matches must enter a human-review queue.

Never silently merge entities solely because their names are similar.

Provide administrative screens for:

Suggested merges
Split entities
Alias management
Conflicting metadata
Source priority overrides
Reverting previous merges
9. Search System

Build hybrid search that combines:

BM25 lexical search
Semantic embedding similarity
Graph proximity
Community membership
User preferences
Software quality signals
Recency where appropriate
Reproducibility signals
Diversity controls

Support:

Natural-language queries
Exact software or paper lookup
Algorithm search
MSC browsing
Faceted filtering
Search by programming language
Search by licence
Search by operating system
Search by active maintenance
Search by archived status
Search by research community
Search by publication year
Search by reproducibility criteria

Examples:

“Python tools for symbolic integration”
“software for persistent homology with active repositories”
“papers using Julia packages for Gröbner bases”
“open-source alternatives to MATLAB for numerical PDEs”
“software connected to tropical geometry and machine learning”
“beginner-friendly graph theory libraries”
“packages implementing the F4 algorithm”

The query system should extract:

Entity mentions
Intended task
Mathematical domain
Software constraints
Programming-language preference
Time constraints
Licence preference
Experience level

Show active query interpretation as removable filter chips.

10. Recommendation Engine

Build a multi-stage recommendation system.

Candidate Generation

Generate candidates through multiple channels:

Full-text retrieval
Semantic similarity
Personalized PageRank
Community neighbors
Co-citation
Co-usage
Similar MSC classifications
Similar algorithms
Similar user collections
Graph-neural-network link prediction
Trending or emerging software within a community
Similar repository characteristics
Baselines

Implement and evaluate:

Popularity
Most-cited
BM25
Embedding nearest neighbors
Jaccard similarity
Common neighbors
Adamic–Adar
Personalized PageRank
Node2Vec
Matrix factorization where appropriate
Advanced Models

Use PyTorch Geometric to represent the graph as a heterogeneous graph.

Experiment with:

Heterogeneous Graph Transformer
R-GCN
Heterogeneous GraphSAGE
Metapath2Vec
Link-prediction decoders
Multi-task learning for community classification and link prediction

Potential node features:

Text embeddings
MSC multi-hot vectors
Programming-language vectors
Licence encoding
Repository-health features
Citation statistics
Temporal features
Community embeddings
Graph-centrality features
Software metadata-completeness features
Ranking

Use a reranker combining:

Predicted relevance
Graph relationship strength
Text relevance
User preference fit
Diversity
Novelty
Confidence
Software quality
Reproducibility
Result freshness
Explanation availability

Do not reward GitHub stars as a direct measure of scientific quality.

Cold Start

Support cold-start recommendations for:

New users
New papers
New software
Sparse research fields
Software without repositories
Papers without abstracts

Use metadata, MSC codes, text features, and community priors.

11. Explainable Recommendations

Every recommendation card must have a Why this? action.

Provide several explanation types:

Graph Path Explanation

Example:

You saved Paper A
→ Paper A uses Software B
→ Software B implements Algorithm C
→ Recommended Software D also implements Algorithm C
Community Explanation

Example:

This package belongs to the same mathematical software community as three tools in your Numerical Algebra collection.

Metadata Explanation

Example:

This paper shares MSC classifications 68W30 and 65Y05 with your recent searches.

Feature Explanation

Example:

The strongest ranking signals were shared algorithm, active Python implementation, and citation overlap.

Contrastive Explanation

Example:

This was ranked above Package X because it has a compatible licence, a recent release, and stronger adoption in your selected research community.

Confidence and Evidence

Show:

Confidence
Supporting paths
Source provenance
Whether the relationship is direct or inferred
Date last checked

Explanations must faithfully represent the actual recommendation computation. Do not generate plausible-sounding explanations after the fact.

12. Research Assistant

Include a graph-grounded research assistant.

It must answer only from retrieved graph entities and approved source metadata.

Capabilities:

Explain software and algorithms in plain language
Find implementations of algorithms
Compare software packages
Generate a research-software landscape summary
Produce a reading or learning path
Suggest related software communities
Explain graph relationships
Generate structured search filters
Create collections from a research question
Summarize why a recommendation appeared
Identify missing metadata or reproducibility concerns

Every factual answer must include clickable source entities and graph paths.

The assistant must clearly say when evidence is missing or uncertain.

Never allow unrestricted natural-language-to-Cypher execution. Use:

Query-intent parsing
A safe intermediate query representation
Approved query templates
Parameterized Cypher
Cost and result limits
Logging and abuse detection
13. Core User Experiences
Home

The homepage should immediately communicate:

Discover the papers, algorithms, and software that power modern mathematics.

Include:

Universal search
A subtle interactive graph preview
Example research queries
Popular research communities
Recently updated software
Explanation of path-based recommendations

Do not make the homepage a full-screen animation that delays access to search.

Onboarding

Ask users:

Research interests
Experience level
Preferred programming languages
Preferred software licences
Mathematics topics
Whether they prioritize ease of use, performance, rigor, reproducibility, or active maintenance

Allow skipping onboarding.

Discovery Dashboard

Include:

Personalized recommendations
Continue exploring
New software in followed communities
Papers connected to saved software
Reproducibility warnings
Community spotlight
Saved searches and collections
Universal Search

Include:

Keyboard-first command interface
Entity-type tabs
Search suggestions
Filter chips
Sort controls
List, table, and graph result modes
Search explanation panel
3D Knowledge Atlas

This is a functional research interface, not decorative artwork.

Users must be able to:

Search and fly to an entity
Expand one or more relationship types
Focus on a node
Pin nodes
Hide unrelated nodes
Change layout
Filter by node and relationship type
Filter by year
Filter by confidence
Display communities
Show shortest and strongest paths
Compare two nodes
Save a subgraph
Add selected nodes to a collection
Open details without losing graph state
Share a stable graph URL
Export a subgraph
Switch to a 2D accessible view
Switch to a table view
Entity Detail Pages

Create dedicated pages for:

Papers
Software
Algorithms
Authors
Communities
MSC classifications
Repositories
Datasets

Each detail page should include:

Overview
Key relationships
Recommendation explanations
Provenance
Timeline
Related entities
Community membership
Confidence and data quality
Citation or export tools
Software Comparison

Let users compare up to four tools using:

Mathematical purpose
Implemented algorithms
Supported languages
Installation methods
Licence
Repository activity
Release history
Documentation
Citation usage
Community adoption
Reproducibility
Dependencies
Operating-system support
Beginner suitability

Clearly separate objective metadata from inferred scores.

Research Workspace

Allow users to create workspaces containing:

Papers
Software
Algorithms
Notes
Saved graph views
Search queries
Tags
Reading status
Research questions

Include export to:

BibTeX
CSV
JSON
Markdown
GraphML
Cypher statements where appropriate
Provenance Explorer

For any field, users should be able to inspect:

Source
Original value
Normalized value
Retrieval date
Confidence
Transformation history
Conflicting values
14. Mathematics-Friendly UX

Assume many users are computer-science students without advanced mathematics training.

Include:

“Explain simply” controls
Expandable technical definitions
An MSC code explorer
Glossary tooltips
Algorithm cards showing input, output, and practical purpose
Beginner, intermediate, and expert display modes
“Why this matters” sections
Small visual examples
Links between mathematical terminology and software tasks

Do not oversimplify expert content. Let users progressively reveal depth.

Create a documentation section called:

Math Concepts You Need for Axiom Atlas

Explain in accessible language:

Graphs
Nodes and edges
Communities
Centrality
Link prediction
Embeddings
Heterogeneous graphs
Classification
Ranking
Precision and recall
Cold start
MSC classifications
Personalized PageRank
Graph neural networks
Recommendation diversity

Include optional mathematical notation after the plain-language explanation.

15. Three.js and React Three Fiber Requirements

Use Three.js through React Three Fiber for the primary graph visualization.

Visual Encoding

Use consistent visual encoding:

Paper: circular node
Software: rounded cube or hexagonal node
Algorithm: diamond or crystalline node
Author: smaller circular node
Dataset: stacked-disc node
MSC classification: ring node
Community: translucent spatial region rather than an ordinary node
Repository: code-bracket-inspired shape

Encode:

Node type through shape
Community through color
Importance through controlled size
Confidence through opacity or edge style
Selection through outline and glow
Inferred edges through dashed or animated styling

Never rely on color alone.

Interaction

Implement:

Hover tooltips
Single-click selection
Double-click expansion
Keyboard selection
Search-to-focus camera animation
Pinning
Multi-selection
Path highlighting
Community isolation
Timeline filtering
Context menus
Breadcrumb navigation
Undo and redo for graph exploration
URL-synchronized graph state
Camera

Provide:

Smooth focus transitions
Fit-selection
Reset view
Orthographic and perspective modes
Optional auto-rotation only on the passive homepage preview
No forced camera movement while the user is interacting
Performance

The graph must remain responsive.

Use:

Instanced meshes
Buffer geometries
Level of detail
Frustum culling
Progressive graph loading
Server-side graph neighborhood queries
Web Worker layouts
Spatial indexing
Limited visible labels
Texture atlases where useful
Adaptive quality
Paused rendering when the scene is idle
Performance profiling

Do not send the complete knowledge graph to the browser.

Render:

A focused subgraph
Aggregated communities
Server-generated graph neighborhoods
Progressively expanded relationships

Establish measurable performance budgets:

Initial interactive state in under 3 seconds on a typical modern laptop under normal network conditions
Smooth navigation at the target graph size
No main-thread layout calculation for large subgraphs
Graceful behavior on integrated graphics
Low-power and reduced-motion modes
Accessibility

Provide:

Complete 2D equivalent
Table equivalent
Keyboard navigation
Screen-reader descriptions
Visible focus indicators
Reduced-motion setting
High-contrast mode
Text alternatives for graph paths
No critical information available only through spatial position
16. Visual Design Direction

The visual identity should feel:

Scholarly
Futuristic
Precise
Calm
Trustworthy
Exploratory
Technically sophisticated

Avoid:

Generic SaaS gradients
Excessive glassmorphism
Neon cyberpunk overload
Tiny text
Constant particle animation
Decorative equations with no meaning
Excessive blur
Poor contrast
Giant empty hero sections
Game-like interfaces that reduce academic credibility

Use a dark-first visual system with a complete light mode.

Suggested dark palette:

Background: near-black blue
Elevated surfaces: deep navy
Primary accent: electric cyan
Secondary accent: warm amber
Tertiary accent: restrained violet
Success: emerald
Warning: amber-orange
Error: coral red
Body text: near-white
Secondary text: cool grey

Use restrained glow only for:

Active selections
Search focus
Important paths
Live ingestion state

Typography should combine:

A highly readable sans-serif for interface text
A restrained serif for selected editorial headings
A monospaced font for identifiers, formulas, and code

The interface should look impressive in screenshots while remaining practical for hours of research work.

17. Community Detection and Graph Analytics

Reproduce the conference baseline where possible.

Implement:

Louvain
Leiden
Weakly connected components
PageRank
Personalized PageRank
Betweenness centrality
Degree centrality
Similarity
Shortest paths
Weighted paths
Node embeddings
Topological link prediction

Compare Louvain and Leiden on:

Modularity
Stability
Community size distribution
Interpretability
Runtime

Create human-readable community labels using:

Dominant MSC classes
Frequent software
Frequent algorithms
Frequent paper keywords
Representative papers

Generated labels must be marked as generated until reviewed.

18. Model Evaluation

Use robust evaluation rather than a single random train/test split.

Splits

Use:

Temporal splits
Cold-start software splits
Cold-start paper splits
Community-stratified splits
Source-based robustness tests

Avoid leakage from:

Future citations
Duplicate papers
Software aliases
Relations derived from the target edge
Community labels calculated using test edges
Ranking Metrics

Report:

Precision@k
Recall@k
nDCG@k
MAP@k
MRR
Hit rate
Coverage
Diversity
Novelty
Calibration
Popularity bias
Long-tail exposure
Link Prediction

Report:

AUCPR
ROC-AUC where appropriate
Hits@k
Mean reciprocal rank
Performance by node degree
Performance on cold-start entities
Explainability

Evaluate:

Path validity
Faithfulness to ranking
Explanation stability
Human usefulness
Explanation length
User comprehension
Human Evaluation

Design a small study in which students or researchers judge:

Recommendation relevance
Explanation usefulness
Trust
Discovery of unfamiliar software
Ease of navigation
Visual overload
Whether the 3D graph improved understanding
19. Data Quality and Reproducibility Scores

Create separate, transparent indicators rather than one mysterious quality score.

Possible indicators:

Metadata completeness
Repository linked
Licence identified
Release available
Recent maintenance activity
Archived source available
Documentation present
Tests detected
Continuous integration detected
Package-manager release available
Reproducible research artifact available
Citation evidence available

Always show the components behind a score.

Do not classify inactive software as low quality automatically. Historically important and stable software may not require frequent commits.

20. Authentication and Permissions

Implement:

Email or social authentication through a secure provider
Guest exploration
Registered-user collections
Private and public workspaces
Role-based administrative access
Curator permissions
Audit logs
Account export
Account deletion
Session management
Rate limiting

Roles:

Guest
Member
Researcher
Curator
Administrator
21. Security

Implement:

Strict input validation
Parameterized database queries
Safe Cypher templates
API rate limiting
CSRF protection where relevant
Secure cookies
Secret rotation support
Dependency scanning
Container scanning
Content Security Policy
Restrictive CORS
Upload validation
Audit logging
Least-privilege database users
Protection against expensive graph-query abuse
Timeout and result limits
Personally identifiable information minimization

Do not expose GitHub or source API tokens to the client.

22. Observability

Include:

Structured logs
Request tracing
Ingestion-job traces
Model inference latency
Search latency
Graph query latency
Error rates
Recommendation impression and interaction events
WebGL performance telemetry with privacy protection
Worker queue depth
API quota usage
Data freshness
Source failure alerts

Create an administrative observability dashboard.

23. Testing

Require:

Unit Tests
Normalization
Entity matching
Ranking functions
Graph transformations
API validation
Explanation generation
Permission checks
Integration Tests
PostgreSQL
Neo4j
OpenSearch
Redis
Source adapters
Ingestion workers
Model service
End-to-End Tests
Search
Filtering
Graph exploration
Saving a collection
Comparing software
Recommendation explanation
Export
Authentication
Administration
Data Tests
Required fields
Identifier uniqueness
Referential integrity
Provenance coverage
Confidence ranges
Duplicate rates
Schema drift
Accessibility Tests
Automated axe checks
Keyboard-only workflows
Screen-reader testing
Reduced-motion behavior
Contrast
Visual and Performance Tests
Storybook snapshots
Responsive layouts
Graph frame-rate benchmarks
Large-subgraph stress tests
API load tests
24. Deployment

Provide:

Docker Compose for local development
Seed scripts
Environment validation
Production containers
Database migrations
Infrastructure-as-code
CI/CD
Preview deployments
Staging environment
Production environment
Backup and restore procedures
Disaster recovery documentation
Model rollback
Search-index rebuilds
Graph migration procedures

The local environment should start with one documented command.

Include:

.env.example
Makefile
docker-compose.yml
CONTRIBUTING.md
SECURITY.md
ARCHITECTURE.md
DATA_MODEL.md
MODEL_CARD.md
DATA_CARD.md
API.md
DEPLOYMENT.md
25. Required Administrative Tools

Build an internal administration area for:

Ingestion status
Data-source health
Failed records
Duplicate entities
Proposed merges
Metadata conflicts
Community labels
User feedback
Recommendation diagnostics
Model comparison
Search analytics
API quotas
Export jobs
Audit logs
Feature flags

Do not expect curators to edit Neo4j directly.

26. Required Research Artifacts

The repository must contain a legitimate research component.

Produce:

Reproducible data-preparation pipeline
Baseline experiments
Community-detection comparison
Heterogeneous GNN experiment
Cold-start evaluation
Recommendation evaluation
Explainability evaluation
Ablation study
Error analysis
Model card
Dataset card
Reproducible experiment configuration
Saved metrics
Research report draft

Ablations should test:

No graph features
No MSC metadata
No text embeddings
No repository-quality features
No personalization
No community features
No path-explanation requirement
Structured metadata versus text-only embeddings
27. Implementation Phases

Do not stop after the first phase.

Phase 1: Architecture and Reproducibility Foundation

Deliver:

Architecture documents
Monorepo
Local infrastructure
CI
Source schemas
Dataset download and verification
Seed ingestion
Initial Neo4j graph
Initial PostgreSQL application schema
Phase 2: Canonical Data Platform

Deliver:

Source adapters
Normalization
Entity resolution
Provenance
Incremental updates
Data-quality tests
Administration interface
Phase 3: Search and Graph Exploration

Deliver:

Hybrid search
Entity pages
Filters
2D graph
3D graph
Path finding
Graph state sharing
Performance optimization
Phase 4: Recommendation Research

Deliver:

Baselines
Offline evaluation
Community detection
Node embeddings
Heterogeneous GNN
Cold-start analysis
Model registry
Phase 5: Explainable Personalized Recommendations

Deliver:

User profiles
Recommendation feed
Multi-stage ranking
Path explanations
Feedback collection
Recommendation diagnostics
Phase 6: Research Workspace and Assistant

Deliver:

Collections
Notes
Comparison
Export
Graph-grounded assistant
Safe structured graph querying
Phase 7: Production Hardening

Deliver:

Accessibility
Security review
Load testing
Observability
Backups
Deployment
Documentation
User study
Research report
28. Acceptance Criteria

The system is not complete until all of the following are true:

A real dataset can be ingested reproducibly.
Raw and normalized metadata are traceable.
Duplicate software entities can be reviewed and merged.
Users can search across papers, software, algorithms, and communities.
Search combines text, semantic, and graph signals.
Users can explore a performant 3D graph.
Every 3D workflow has a 2D or table equivalent.
Users can save research collections.
Users can compare mathematical software.
Recommendations are generated by real models or real graph algorithms.
Recommendation explanations use actual paths and ranking signals.
Cold-start performance is evaluated.
Community-detection results are reproducible.
Model experiments are versioned.
The platform supports beginner-friendly explanations.
All imported claims expose provenance.
Inferred claims expose confidence.
The application passes accessibility checks.
The project includes unit, integration, and end-to-end tests.
Local development and production deployment are documented.
There are no dead buttons or fake features.
The complete repository can be run by another developer.
A research report can be written from saved experiments.
The UI remains usable on lower-powered devices.
The interface is visually distinctive without sacrificing readability.
29. Instructions for the Coding Agent

Before implementation:

Create ARCHITECTURE.md.
Create DATA_MODEL.md.
Create GRAPH_SCHEMA.md.
Create INGESTION_PLAN.md.
Create ML_RESEARCH_PLAN.md.
Create UX_SPECIFICATION.md.
Create SECURITY.md.
Create a dependency and infrastructure decision record.
Produce the complete phased backlog.
Identify high-risk assumptions.

Then begin implementing.

Rules:

Do not ask broad questions when a sensible technical default can be selected.
Explain important architectural decisions.
Use strict typing.
Do not use any unless technically unavoidable and documented.
Keep domain logic out of UI components.
Generate database migrations.
Validate all environment variables.
Add tests with each feature.
Keep API contracts documented.
Preserve provenance through every transformation.
Never silently discard malformed source records.
Avoid premature microservices, but preserve clean service boundaries.
Never expose secrets in source code.
Do not fabricate external data.
Do not mark a feature complete until it is functional and tested.
Do not stop at scaffolding.
Do not stop at a homepage.
Do not stop at a graph demo.
Do not call the product complete while core pages use placeholders.

At the end of every implementation phase, provide:

Completed features
Tests added
Commands to run
Known limitations
Performance measurements
Screenshots or visual test references
Next phase tasks
Updated architecture documentation