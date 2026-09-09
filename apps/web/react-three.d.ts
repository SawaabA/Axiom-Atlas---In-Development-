declare global {
  namespace JSX {
    interface IntrinsicElements {
      ambientLight: Record<string, unknown>;
      bufferAttribute: Record<string, unknown>;
      bufferGeometry: Record<string, unknown>;
      icosahedronGeometry: Record<string, unknown>;
      line: Record<string, unknown>;
      lineBasicMaterial: Record<string, unknown>;
      mesh: Record<string, unknown>;
      meshStandardMaterial: Record<string, unknown>;
      pointLight: Record<string, unknown>;
    }
  }
}

declare namespace React {
  namespace JSX {
    interface IntrinsicElements {
      ambientLight: Record<string, unknown>;
      bufferAttribute: Record<string, unknown>;
      bufferGeometry: Record<string, unknown>;
      icosahedronGeometry: Record<string, unknown>;
      line: Record<string, unknown>;
      lineBasicMaterial: Record<string, unknown>;
      mesh: Record<string, unknown>;
      meshStandardMaterial: Record<string, unknown>;
      pointLight: Record<string, unknown>;
    }
  }
}

export {};
