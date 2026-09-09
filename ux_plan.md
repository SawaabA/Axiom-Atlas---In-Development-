# Design Axiom Atlas: An Outstanding Mathematical Knowledge-Graph Experience

Act as a world-class product designer, UX researcher, information architect, data-visualization specialist, and React Three Fiber creative developer.

Design the complete visual and interaction system for **Axiom Atlas**, a mathematical software discovery platform connecting papers, software, algorithms, repositories, datasets, authors, classifications, and research communities.

This is not a generic analytics dashboard. It should feel like an interactive scientific observatory built for serious research.

The design must be visually memorable enough for a portfolio showcase while remaining practical, accessible, and comfortable during long research sessions.

---

# Experience Goal

Users should feel that they are navigating a living map of mathematical knowledge.

The interface should communicate:

* Scale
* Structure
* Intellectual relationships
* Trust
* Discovery
* Precision
* Calm exploration

The experience must never feel like:

* A cryptocurrency dashboard
* A cyberpunk video game
* A generic admin template
* A collection of floating glass cards
* A decorative particle animation
* A graph with unreadable labels and no research workflow

---

# Primary Visual Concept

Use the metaphor of a **scholarly constellation**.

* Papers form clusters around research questions.
* Software packages act as tools or instruments.
* Algorithms form structural bridges.
* MSC classifications form larger organizing regions.
* Research communities appear as soft spatial territories.
* Citations and implementation relationships form visible paths.
* User collections form private named constellations.

The 3D visualization must support real navigation and decision-making.

---

# Brand Direction

Working name: **Axiom Atlas**

Possible tagline:

> Navigate the software, algorithms, and ideas behind mathematics.

Alternative tagline:

> Explore how mathematical research becomes software.

Brand personality:

* Intelligent
* Curious
* Rigorous
* Modern
* Human
* Dependable
* Exploratory

Avoid using infinity symbols, generic brain icons, random mathematical equations, or glowing network logos unless the visual has direct meaning.

---

# Color System

Create both dark and light themes.

## Dark Theme

* Main background: `#070A12`
* Secondary background: `#0D1321`
* Elevated surface: `#131B2D`
* Primary text: `#F5F7FB`
* Secondary text: `#A7B0C2`
* Border: `#26324A`
* Cyan accent: `#46D9E8`
* Amber accent: `#F2B84B`
* Violet accent: `#9A86FD`
* Emerald success: `#45D49C`
* Coral error: `#F07178`

## Light Theme

Use a warm, slightly blue-white background rather than pure white.

* Main background: `#F6F8FC`
* Elevated surface: `#FFFFFF`
* Primary text: `#101727`
* Secondary text: `#58647A`
* Border: `#DCE2ED`

Maintain WCAG-compliant contrast.

Colors must have semantic meaning and must not be the only means of communicating node types.

---

# Typography

Use:

* A clean sans-serif for the interface
* A restrained editorial serif for selected headings and paper titles
* A monospaced face for DOI values, repository IDs, MSC codes, formulas, and command examples

Typography should remain readable at normal browser zoom.

Avoid extremely small metadata text.

Use a clear hierarchy:

* Display title
* Page heading
* Section heading
* Card heading
* Body
* Metadata
* Code or identifier
* Annotation

---

# Layout

Use a desktop application shell with:

## Left Navigation Rail

Include:

* Discover
* Atlas
* Communities
* Workspace
* Collections
* Compare
* Saved Searches
* Assistant

Collapse the rail when the graph requires additional space.

## Top Command Bar

Include:

* Universal search
* Command palette
* Current workspace
* Notifications
* Theme
* User menu

## Context Panel

Use a right-side panel for:

* Selected node details
* Recommendation explanation
* Graph filters
* Path information
* Provenance
* Notes

The context panel should not fully replace the graph unless opened as a dedicated detail page.

---

# Homepage

The homepage should load quickly and provide immediate access to search.

Structure:

1. Compact navigation
2. Hero statement
3. Large universal search field
4. Example queries
5. Subtle interactive constellation
6. Featured communities
7. Recently updated mathematical software
8. Explanation of graph-based recommendations
9. Researcher and student use cases
10. Data provenance statement

The graph preview should use no more than a limited curated set of nodes.

Avoid a 100vh animation that blocks users from reaching content.

---

# Onboarding

Create a short, optional onboarding flow.

Ask:

* What areas are you exploring?
* What programming languages do you use?
* What is your experience level?
* What matters most: ease of use, performance, rigor, active maintenance, or reproducibility?
* Do you prefer open-source software only?

Use visual topic cards and searchable selections.

After onboarding, animate the selected topics joining into a personal constellation.

Keep the animation under two seconds and respect reduced-motion settings.

---

# Discovery Dashboard

Design a modular dashboard with:

* Recommended for you
* Continue exploring
* New connections
* Community spotlight
* Software updated recently
* Papers connected to saved tools
* Reproducibility concerns
* Saved collections

Recommendation cards should show:

* Entity type
* Title
* One-sentence relevance explanation
* Key metadata
* Confidence
* “Why this?” action
* Save action
* Explore connections action

Avoid displaying unexplained percentage scores.

---

# Universal Search

Create a search experience that feels faster and more powerful than a conventional academic database.

Features:

* Search-as-you-type
* Command palette shortcut
* Query interpretation chips
* Filters
* Entity tabs
* Saved queries
* Search history
* Suggestions
* Natural-language input
* Keyboard navigation
* List, table, and graph modes

Example interpretation:

```text
Query:
Python software for symbolic algebra with active repositories

Interpreted as:
[Language: Python]
[Topic: Symbolic algebra]
[Repository status: Active]
[Entity: Software]
```

Users must be able to remove or edit each interpretation.

---

# Three-Dimensional Atlas

Build the graph using React Three Fiber and Three.js.

## Scene Composition

Use:

* A deep spatial field
* Very subtle atmospheric fog
* Restrained ambient particles only when idle
* Soft community regions
* Crisp selected paths
* High legibility
* Limited labels
* Calm camera behavior

Do not make the background visually noisy.

## Node Shapes

* Paper: sphere or flat disc
* Software: rounded cube
* Algorithm: diamond
* Dataset: stacked disc
* Author: small sphere with ring
* MSC classification: outlined torus
* Repository: bracket-like geometric object
* Community: translucent boundary region

Use instanced geometry for repeated shapes.

## Node Appearance

Default nodes should be understated.

Selected nodes may use:

* Brighter outline
* Soft glow
* Increased label visibility
* Slight scale increase
* Highlighted connected edges

Do not make every node glow.

## Edges

Different relationships should be distinguishable through:

* Line width
* Line pattern
* Curvature
* Direction indicator
* Subtle animation
* Opacity

Examples:

* Citation: thin directional line
* Implements: strong solid line
* Uses software: medium line
* Inferred relation: dashed line
* Recommended path: bright emphasized path
* Dependency: stepped or slightly angular line

## Labels

Labels must be limited intelligently.

Show labels for:

* Selected nodes
* Hovered nodes
* Search results
* Important nodes
* Path nodes
* Nearby nodes at sufficient zoom

Use collision avoidance and fade labels based on zoom.

Never display thousands of overlapping labels.

## Community Regions

Represent communities with:

* Soft convex or metaball-like regions
* Restrained tint
* Community name
* Dominant MSC classifications
* Size summary

Regions should fade when users focus on individual nodes.

## Camera Controls

Provide:

* Smooth fly-to
* Fit selection
* Reset
* Perspective mode
* Orthographic mode
* Focus lock
* Minimap or orientation helper
* Keyboard controls
* Reduced-motion transitions

Do not rotate the graph automatically while users are working.

## Graph Interaction

Include:

* Hover
* Select
* Expand
* Collapse
* Pin
* Multi-select
* Lasso
* Hide
* Isolate
* Compare
* Find path
* Add to collection
* Open details
* Undo
* Redo

## Graph Modes

Include:

* Explore mode
* Path mode
* Community mode
* Timeline mode
* Compare mode
* Recommendation explanation mode
* Data-quality mode

---

# Path Explanation Experience

Design recommendation paths as a first-class interface.

When a user opens “Why this?”, show:

1. A plain-language sentence
2. The highlighted graph path
3. A step-by-step path list
4. Source evidence
5. Confidence
6. Alternative explanation paths
7. Ranking factors

Example:

```text
You saved a paper about Gröbner bases.

That paper uses Macaulay2.

Macaulay2 and Singular frequently appear in the same software community.

Singular also implements algorithms related to your saved topic.
```

Let users click each step to inspect the entity.

---

# Detail Pages

## Software Page

Hero area:

* Software name
* Brief purpose
* Primary language
* Licence
* Maintenance status
* Save and compare actions

Sections:

* Overview
* Implemented algorithms
* Papers using it
* Research communities
* Repository health
* Releases
* Dependencies
* Alternatives
* Provenance
* Recommendation reasons
* Installation information
* Reproducibility indicators

## Paper Page

Sections:

* Abstract
* Authors
* MSC codes
* Software used
* Algorithms
* Citations
* Related software
* Research community
* Recommendation explanations
* BibTeX export

## Algorithm Page

Explain:

* What problem it solves
* Inputs
* Outputs
* Simple explanation
* Technical explanation
* Implementing software
* Foundational papers
* Related algorithms
* Research communities

## Community Page

Include:

* Community map
* Human-readable description
* Dominant MSC codes
* Representative software
* Representative papers
* Community timeline
* Overlapping communities
* Emerging software

---

# Comparison Experience

Create a polished software comparison page.

Use a frozen first column and horizontally scrollable alternatives.

Compare:

* Purpose
* Algorithms
* Languages
* Licence
* Platforms
* Repository activity
* Latest release
* Documentation
* Dependencies
* Community adoption
* Reproducibility
* Beginner friendliness

Highlight differences, not merely all available metadata.

Allow users to select a priority such as:

* Best for beginners
* Best for Python
* Best maintained
* Most established
* Most reproducible
* Most flexible licence

Explain how the comparison changes under each priority.

---

# Beginner-Friendly Layer

Create a global mode switch:

* Simple
* Standard
* Technical

## Simple Mode

* Plain-language explanations
* Reduced metadata
* Common-use examples
* Expanded glossary
* Recommended starting tools

## Standard Mode

* Balanced detail
* Main metadata
* Graph explanations

## Technical Mode

* Full identifiers
* MSC hierarchy
* Confidence values
* Model information
* Graph statistics
* Provenance details

The mode should change information density, not merely font size.

---

# Motion Design

Use motion to communicate:

* Focus
* Expansion
* Relationship
* State changes
* Graph navigation

Recommended motion:

* Nodes smoothly enter during graph expansion
* New paths trace once when revealed
* Detail panels transition without covering context
* Saved entities briefly acknowledge the action
* Community isolation gently dims unrelated regions

Avoid:

* Continuous pulsing
* Excessive parallax
* Floating cards
* Long loading animations
* Dramatic camera spins
* Motion that delays work

Respect `prefers-reduced-motion`.

---

# Empty, Loading, and Error States

Create thoughtful states.

Examples:

## Empty Search

> No exact software matches were found. Try broadening the MSC classification or removing the programming-language filter.

## Empty Workspace

> Save a paper, software package, or algorithm to begin building your research map.

## Graph Loading

Use progressive node loading with a clear status such as:

> Loading 42 nearby entities and 106 relationships.

## Data Conflict

> Two sources disagree about this software licence. Review both records.

Errors should explain what happened and what the user can do next.

---

# Mobile and Tablet

Do not force the desktop 3D graph onto small screens unchanged.

On mobile:

* Search and recommendations are primary
* Use a simplified 2D graph
* Offer a limited 3D exploration mode
* Use bottom sheets for details
* Keep comparison horizontally scrollable
* Preserve saved workspaces

On tablets:

* Support split view
* Use touch-friendly graph controls
* Provide a persistent detail drawer

---

# Accessibility

The final design must support:

* Keyboard-only navigation
* Screen readers
* Visible focus
* High contrast
* Reduced motion
* Text resizing
* Color-vision deficiencies
* 2D and table alternatives
* Accessible graph-path descriptions
* Descriptive labels for all graph controls

Every graph action must have a non-pointer alternative.

Provide a generated textual representation such as:

```text
Selected node: Singular
Type: Mathematical software
Direct relationships:
- Implements Gröbner basis algorithms
- Used by 2,418 indexed papers
- Member of Computational Algebra community
- Related to Macaulay2 through 314 co-usage records
```

---

# Performance Design

Design around focused subgraphs rather than the entire database.

Use:

* Progressive loading
* Aggregated distant communities
* Limited labels
* Instancing
* Level of detail
* Idle rendering
* Adaptive graphical quality
* Web Worker layouts
* Server-side graph filtering

Provide settings:

* High quality
* Balanced
* Performance
* Reduced motion
* 2D only

Never sacrifice core usability for graphical effects.

---

# Required Design Deliverables

Produce:

1. Product sitemap
2. Core user journeys
3. Information architecture
4. Design tokens
5. Light and dark themes
6. Responsive grid
7. Complete component inventory
8. Homepage
9. Onboarding
10. Dashboard
11. Search
12. 3D Atlas
13. 2D Atlas
14. Entity pages
15. Community page
16. Comparison
17. Workspace
18. Assistant
19. Provenance explorer
20. Administration screens
21. Loading and error states
22. Accessibility annotations
23. Motion specification
24. Three.js implementation specification
25. Performance budgets
26. Developer handoff documentation

Do not return only mood boards or a few isolated screens.

---

# Final Quality Bar

The finished design should be:

* More polished than a standard university capstone
* Credible as a research infrastructure product
* Strong enough for a portfolio case study
* Visually distinctive in screenshots
* Easy to understand within one minute
* Comfortable to use for hours
* Functional without 3D
* Accessible
* Responsive
* Technically feasible
* Consistent across every screen

Prioritize usability and research trust over visual spectacle.

The final result should make users think:

> I can finally understand how mathematical papers, software, algorithms, and communities connect.
