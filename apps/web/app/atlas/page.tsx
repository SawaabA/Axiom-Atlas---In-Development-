import { seedDataset } from "@axiom-atlas/shared-types";
import { Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../../components/app-shell";
import { AtlasPreviewShell } from "../../components/atlas-preview-shell";

export default function AtlasPage() {
  return (
    <AppShell>
      <div className="space-y-8">
        <header className="grid gap-6 xl:grid-cols-[1.1fr_0.9fr]">
          <div>
            <p className="text-xs uppercase tracking-[0.32em] text-cyan-200/80">3D atlas</p>
            <h2 className="mt-4 text-4xl font-semibold">Focused neighborhoods instead of an unreadable global graph</h2>
            <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">
              The current atlas renders a bounded graph neighborhood from the shared fixture. The service boundary is already prepared for server-side neighborhood loading so the browser never needs the full knowledge graph.
            </p>
          </div>
          <div className="rounded-[32px] border border-white/10 bg-white/5 p-6">
            <p className="text-sm font-medium text-slate-200">Accessible equivalents</p>
            <ul className="mt-4 space-y-3 text-sm leading-6 text-slate-300">
              <li>2D and table views remain planned for the next graph phase.</li>
              <li>Current pages expose graph paths as structured text in recommendations.</li>
              <li>Node type and relationship meaning are never encoded by color alone in the data model.</li>
            </ul>
          </div>
        </header>

        <AtlasPreviewShell edges={seedDataset.edges} nodes={seedDataset.nodes.slice(0, 12)} />

        <Section eyebrow="Node encoding" title="Current atlas schema">
          <div className="flex flex-wrap gap-3">
            <Tag>Software: cyan solid</Tag>
            <Tag tone="warm">Paper: amber solid</Tag>
            <Tag>Repository: neutral support node</Tag>
            <Tag>Community: violet region seed</Tag>
            <Tag>Algorithm: typed bridge entity</Tag>
          </div>
        </Section>
      </div>
    </AppShell>
  );
}
