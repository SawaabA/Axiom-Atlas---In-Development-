import {
  GraphEdge,
  GraphNode,
  Recommendation,
  SearchResult,
  getNeighborhood as getFixtureNeighborhood,
  getNode,
  getNodesByType,
  seedDataset
} from "@axiom-atlas/shared-types";

const DEFAULT_API_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

async function tryFetch<T>(path: string): Promise<T | null> {
  try {
    const response = await fetch(`${DEFAULT_API_URL}${path}`, { cache: "no-store" });
    if (!response.ok) {
      return null;
    }
    return (await response.json()) as T;
  } catch {
    return null;
  }
}

export async function getSummary() {
  const result = await tryFetch<{ counts: Record<string, number>; generated_at: string }>(
    "/v1/summary"
  );
  if (result) {
    return result;
  }
  const counts = seedDataset.nodes.reduce<Record<string, number>>((accumulator, node) => {
    accumulator[node.type] = (accumulator[node.type] ?? 0) + 1;
    return accumulator;
  }, {});
  return { counts, generated_at: seedDataset.generated_at };
}

export async function search(query: string): Promise<SearchResult[]> {
  const result = await tryFetch<{ results: SearchResult[] }>(
    `/v1/search?q=${encodeURIComponent(query)}`
  );
  if (result) {
    return result.results;
  }
  return seedDataset.nodes
    .filter((node) => `${node.title} ${node.summary} ${node.tags.join(" ")}`.toLowerCase().includes(query.toLowerCase()))
    .map((node) => ({ node, score: 1, reasons: ["Fixture fallback"] }));
}

export async function getNeighborhood(
  id: string
): Promise<{ center?: GraphNode; nodes: GraphNode[]; edges: GraphEdge[] }> {
  const result = await tryFetch<{ center: GraphNode; nodes: GraphNode[]; edges: GraphEdge[] }>(
    `/v1/graph/neighborhood/${encodeURIComponent(id)}`
  );
  return result ?? getFixtureNeighborhood(id);
}

export async function getSoftware(): Promise<GraphNode[]> {
  const result = await tryFetch<{ items: GraphNode[] }>("/v1/software");
  return result?.items ?? getNodesByType("software");
}

export async function getSoftwareById(id: string): Promise<GraphNode | undefined> {
  const result = await tryFetch<GraphNode>(`/v1/software/${encodeURIComponent(id)}`);
  return result ?? getNode(id);
}

export async function getCommunities(): Promise<GraphNode[]> {
  const result = await tryFetch<{ items: GraphNode[] }>("/v1/communities");
  return result?.items ?? getNodesByType("community");
}

export async function getCommunityById(id: string): Promise<GraphNode | undefined> {
  const result = await tryFetch<GraphNode>(`/v1/communities/${encodeURIComponent(id)}`);
  return result ?? getNode(id);
}

export async function getRecommendations(id: string): Promise<Recommendation[]> {
  const result = await tryFetch<{ results: Recommendation[] }>(
    `/v1/software/${encodeURIComponent(id)}/recommendations`
  );
  return result?.results ?? [];
}

export async function getIngestionJobs(): Promise<
  Array<{
    id: string;
    source_name: string;
    status: string;
    records_fetched: number;
    records_normalized: number;
    records_failed: number;
    started_at: string;
    finished_at: string | null;
  }>
> {
  const result = await tryFetch<{
    items: Array<{
      id: string;
      source_name: string;
      status: string;
      records_fetched: number;
      records_normalized: number;
      records_failed: number;
      started_at: string;
      finished_at: string | null;
    }>;
  }>("/v1/admin/ingestion/jobs");
  return result?.items ?? [];
}
