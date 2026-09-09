import { describe, expect, it } from "vitest";

import { getNode, getNodesByType } from "./index";

describe("shared fixture access", () => {
  it("loads software nodes", () => {
    expect(getNodesByType("software").length).toBeGreaterThan(0);
  });

  it("finds a known node", () => {
    expect(getNode("software:sagemath")?.title).toBe("SageMath");
  });
});
