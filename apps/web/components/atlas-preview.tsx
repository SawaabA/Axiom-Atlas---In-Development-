"use client";

import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { GraphEdge, GraphNode } from "@axiom-atlas/shared-types";
import { createElement } from "react";

function edgeVertices(source: GraphNode, target: GraphNode): [number, number, number, number, number, number] {
  const sourceIndex = Math.abs(source.id.split("").reduce((total, char) => total + char.charCodeAt(0), 0)) % 7;
  const targetIndex = Math.abs(target.id.split("").reduce((total, char) => total + char.charCodeAt(0), 0)) % 7;
  return [
    Math.sin(sourceIndex) * 2.4,
    Math.cos(sourceIndex) * 1.5,
    (sourceIndex - 3) * 0.28,
    Math.sin(targetIndex) * 2.4,
    Math.cos(targetIndex) * 1.5,
    (targetIndex - 3) * 0.28
  ];
}

function NodeMesh({ node }: { node: GraphNode }) {
  const index = Math.abs(node.id.split("").reduce((total, char) => total + char.charCodeAt(0), 0)) % 12;
  const position: [number, number, number] = [
    Math.sin(index * 0.9) * 2.7,
    Math.cos(index * 0.5) * 1.8,
    (index - 6) * 0.18
  ];
  const color =
    node.type === "software"
      ? "#46D9E8"
      : node.type === "community"
        ? "#9A86FD"
        : node.type === "paper"
          ? "#F2B84B"
          : "#A7B0C2";

  return (
    createElement(
      "mesh",
      { position },
      createElement("icosahedronGeometry", {
        args: [node.type === "community" ? 0.28 : 0.18, 0]
      }),
      createElement("meshStandardMaterial", {
        color,
        emissive: color,
        emissiveIntensity: 0.15
      })
    )
  );
}

function EdgeLine({ edge, nodesById }: { edge: GraphEdge; nodesById: Map<string, GraphNode> }) {
  const source = nodesById.get(edge.source);
  const target = nodesById.get(edge.target);
  if (!source || !target) {
    return null;
  }

  const points = edgeVertices(source, target);
  return (
    createElement(
      "line",
      null,
      createElement(
        "bufferGeometry",
        null,
        createElement("bufferAttribute", {
          attach: "attributes-position",
          args: [new Float32Array(points), 3],
          count: 2,
          itemSize: 3
        })
      ),
      createElement("lineBasicMaterial", {
        color: "#7DD3FC",
        opacity: 0.4,
        transparent: true
      })
    )
  );
}

export function AtlasPreview({
  nodes,
  edges,
  autoRotate = false
}: {
  nodes: GraphNode[];
  edges: GraphEdge[];
  autoRotate?: boolean;
}) {
  const nodesById = new Map(nodes.map((node) => [node.id, node]));

  return (
    <div className="h-[360px] overflow-hidden rounded-[32px] border border-white/10 bg-[radial-gradient(circle_at_top,_rgba(70,217,232,0.18),_transparent_36%),linear-gradient(180deg,_rgba(17,24,39,0.95),_rgba(7,10,18,0.98))]">
      <Canvas camera={{ position: [0, 0, 6], fov: 52 }}>
        {createElement("ambientLight", { intensity: 0.75 })}
        {createElement("pointLight", { position: [4, 5, 6], intensity: 40, color: "#46D9E8" })}
        {createElement("pointLight", { position: [-4, -3, 4], intensity: 25, color: "#F2B84B" })}
        {edges.slice(0, 14).map((edge) => (
          <EdgeLine edge={edge} key={edge.id} nodesById={nodesById} />
        ))}
        {nodes.map((node) => (
          <NodeMesh key={node.id} node={node} />
        ))}
        <OrbitControls enablePan={false} autoRotate={autoRotate} autoRotateSpeed={0.5} />
      </Canvas>
    </div>
  );
}
