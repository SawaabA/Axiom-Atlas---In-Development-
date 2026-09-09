"use client";

import dynamic from "next/dynamic";

import { GraphEdge, GraphNode } from "@axiom-atlas/shared-types";

const DynamicAtlasPreview = dynamic(
  () => import("./atlas-preview").then((module) => module.AtlasPreview),
  {
    ssr: false,
    loading: () => <div className="h-[360px] rounded-[32px] border border-white/10 bg-white/5" />
  }
);

export function AtlasPreviewShell({
  nodes,
  edges,
  autoRotate = false
}: {
  nodes: GraphNode[];
  edges: GraphEdge[];
  autoRotate?: boolean;
}) {
  return <DynamicAtlasPreview autoRotate={autoRotate} edges={edges} nodes={nodes} />;
}
