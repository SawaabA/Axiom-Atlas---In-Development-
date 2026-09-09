import Link from "next/link";

import { getCommunities, getSoftware, getSummary } from "@axiom-atlas/api-client";
import { seedDataset } from "@axiom-atlas/shared-types";
import { EntityCard, MetricCard, Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../components/app-shell";
import { AtlasPreviewShell } from "../components/atlas-preview-shell";

const exampleQueries = [
  "Python software for symbolic algebra",
  "Finite element tools with reproducible workflows",
  "Packages implementing Groebner basis algorithms"
];

export default async function HomePage() {
  const [summary, software, communities] = await Promise.all([
    getSummary(),
    getSoftware(),
    getCommunities()
  ]);

  return (
    <AppShell>
      <div className="space-y-8">
        <section className="grid gap-8 xl:grid-cols-[1.2fr_0.8fr]">
          <div className="rounded-[36px] border border-white/10 bg-white/5 p-8">
            <p className="text-xs uppercase tracking-[0.36em] text-cyan-200/80">Navigate the software, algorithms, and ideas behind mathematics</p>
            <h2 className="mt-5 max-w-3xl text-5xl font-semibold leading-tight text-slate-50">
              Discover how mathematical research becomes software through an explainable scholarly atlas.
            </h2>
            <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-300">
              Axiom Atlas connects papers, software packages, repositories, algorithms, and research communities with visible provenance and recommendation paths.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Link className="rounded-full bg-cyan-400 px-5 py-3 text-sm font-semibold text-slate-950" href="/discover">
                Start discovering
              </Link>
              <Link className="rounded-full border border-white/10 px-5 py-3 text-sm font-semibold text-slate-100" href="/atlas">
                Open the atlas
              </Link>
            </div>
            <div className="mt-8 flex flex-wrap gap-2">
              {exampleQueries.map((query) => (
                <Tag key={query} tone="accent">
                  {query}
                </Tag>
              ))}
            </div>
          </div>
          <AtlasPreviewShell autoRotate edges={seedDataset.edges} nodes={seedDataset.nodes.slice(0, 10)} />
        </section>

        <section className="grid gap-4 md:grid-cols-2 xl:grid-cols-4">
          <MetricCard label="Software entities" value={String(summary.counts.software ?? 0)} detail="Seeded mathematical software profiles with graph links." />
          <MetricCard label="Paper entities" value={String(summary.counts.paper ?? 0)} detail="Research papers connected to the tools they use." />
          <MetricCard label="Communities" value={String(summary.counts.community ?? 0)} detail="Machine-readable research communities ready for labeling." />
          <MetricCard label="Relationships" value={String(seedDataset.edges.length)} detail="Explainable paths across software, papers, and repositories." />
        </section>

        <Section eyebrow="Featured software" title="Recently explored packages">
          <div className="grid gap-4 xl:grid-cols-3">
            {software.slice(0, 3).map((node) => (
              <EntityCard
                href={`/software/${encodeURIComponent(node.id)}`}
                key={node.id}
                metadata={
                  <>
                    {((node.metadata.languages as string[] | undefined) ?? []).slice(0, 2).map((language) => (
                      <Tag key={language}>{language}</Tag>
                    ))}
                    <Tag tone="warm">{String(node.metadata.license ?? "Unknown licence")}</Tag>
                  </>
                }
                summary={node.summary}
                title={node.title}
              />
            ))}
          </div>
        </Section>

        <Section eyebrow="Communities" title="Research clusters">
          <div className="grid gap-4 xl:grid-cols-3">
            {communities.map((community) => (
              <EntityCard
                href={`/communities/${encodeURIComponent(community.id)}`}
                key={community.id}
                metadata={
                  <>
                    {((community.metadata.dominant_msc_codes as string[] | undefined) ?? []).slice(0, 3).map((code) => (
                      <Tag key={code}>{code}</Tag>
                    ))}
                  </>
                }
                summary={community.summary}
                title={community.title}
              />
            ))}
          </div>
        </Section>
      </div>
    </AppShell>
  );
}
