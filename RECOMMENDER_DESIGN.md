# Recommender Design

## Baseline in Repository

The current baseline recommends software by:

- shared algorithm coverage
- shared MSC overlap
- shared research community

Each recommendation returns:

- score
- plain-language explanation
- path summary
- ranking signals

## Planned Baselines

- popularity
- Jaccard similarity
- common neighbors
- Adamic-Adar
- Personalized PageRank
- Node2Vec
- text similarity

## Constraint

Explanations must be computed from actual ranking signals, never added after scoring as fabricated prose.
