import { notFound } from "next/navigation";

import { getCommunityById, getNeighborhood } from "@axiom-atlas/api-client";
import { Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../../../components/app-shell";

export default async function CommunityPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const decodedId = decodeURIComponent(id);
  const [community, neighborhood] = await Promise.all([
    getCommunityById(decodedId),
    getNeighborhood(decodedId)
  ]);
  if (!community) {
    notFound();
  }

  return (
    <AppShell>
      <div className="space-y-8">
        <header className="rounded-[32px] border border-white/10 bg-white/5 p-8">
          <p className="text-xs uppercase tracking-[0.32em] text-violet-200/80">Community</p>
          <h2 className="mt-4 text-4xl font-semibold">{community.title}</h2>
          <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">{community.summary}</p>
        </header>

        <Section eyebrow="Dominant classifications" title="MSC profile">
          <div className="flex flex-wrap gap-2">
            {((community.metadata.dominant_msc_codes as string[] | undefined) ?? []).map((code) => (
              <Tag key={code}>{code}</Tag>
            ))}
          </div>
        </Section>

        <Section eyebrow="Connected entities" title="Neighborhood">
          <div className="space-y-3">
            {neighborhood.nodes
              .filter((node) => node.id !== community.id)
              .slice(0, 8)
              .map((node) => (
                <div className="rounded-[20px] border border-white/10 bg-slate-950/40 p-4" key={node.id}>
                  <div className="flex flex-wrap gap-2">
                    <Tag tone="accent">{node.type}</Tag>
                  </div>
                  <h3 className="mt-3 text-lg font-semibold text-slate-100">{node.title}</h3>
                  <p className="mt-2 text-sm leading-6 text-slate-300">{node.summary}</p>
                </div>
              ))}
          </div>
        </Section>
      </div>
    </AppShell>
  );
}
