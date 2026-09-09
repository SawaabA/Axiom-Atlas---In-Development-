import dataset from "../../../data/fixtures/seed_graph.json";

export type EntityType = "software" | "paper" | "algorithm" | "community" | "repository";

export interface Provenance {
  source: string;
  evidence: string;
  confidence: number;
  retrievedAt: string;
}

export interface GraphNode {
  id: string;
  type: EntityType;
  title: string;
  summary: string;
  url: string;
  tags: string[];
  metadata: Record<string, unknown>;
  provenance: {
    source: string;
    evidence: string;
    confidence: number;
    retrieved_at: string;
  };
}

export interface GraphEdge {
  id: string;
  source: string;
  target: string;
  type: string;
  evidence: string;
  confidence: number;
}

export interface GraphDataset {
  generated_at: string;
  dataset_name: string;
  dataset_version: string;
  nodes: GraphNode[];
  edges: GraphEdge[];
}

export interface SearchResult {
  node: GraphNode;
  score: number;
  reasons: string[];
}

export interface RecommendationExplanation {
  plain_language: string;
  path: string[];
  evidence: string[];
  signals: string[];
}

export interface Recommendation {
  node: GraphNode;
  score: number;
  explanation: RecommendationExplanation;
}

export const seedDataset = dataset as GraphDataset;

export function getNode(id: string): GraphNode | undefined {
  return seedDataset.nodes.find((node) => node.id === id);
}

export function getNodesByType(type: EntityType): GraphNode[] {
  return seedDataset.nodes.filter((node) => node.type === type);
}

export function getNeighborhood(id: string): { center?: GraphNode; nodes: GraphNode[]; edges: GraphEdge[] } {
  const center = getNode(id);
  const edges = seedDataset.edges.filter((edge) => edge.source === id || edge.target === id);
  const ids = new Set<string>([id]);
  for (const edge of edges) {
    ids.add(edge.source);
    ids.add(edge.target);
  }
  const nodes = seedDataset.nodes.filter((node) => ids.has(node.id));
  return { center, nodes, edges };
}
