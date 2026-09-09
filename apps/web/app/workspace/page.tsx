import { Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../../components/app-shell";

export default function WorkspacePage() {
  return (
    <AppShell>
      <div className="space-y-8">
        <header className="rounded-[32px] border border-white/10 bg-white/5 p-8">
          <p className="text-xs uppercase tracking-[0.32em] text-cyan-200/80">Workspace</p>
          <h2 className="mt-4 text-4xl font-semibold">Saved research map foundation</h2>
          <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">
            Collections, notes, exports, and graph-state persistence are part of the next product slice. This page already establishes the information architecture and shared experience-mode state.
          </p>
        </header>

        <Section eyebrow="Planned capabilities" title="Workspace roadmap">
          <div className="flex flex-wrap gap-2">
            <Tag>Collections</Tag>
            <Tag>Saved graph views</Tag>
            <Tag>Notes</Tag>
            <Tag>Exports</Tag>
            <Tag>Recommendation feedback</Tag>
          </div>
        </Section>
      </div>
    </AppShell>
  );
}
