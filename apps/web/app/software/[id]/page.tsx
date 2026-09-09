import { notFound } from "next/navigation";

import { getRecommendations, getSoftwareById } from "@axiom-atlas/api-client";
import { Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../../../components/app-shell";

export default async function SoftwareDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const software = await getSoftwareById(decodeURIComponent(id));
  if (!software) {
    notFound();
  }
  const recommendations = await getRecommendations(software.id);

  return (
    <AppShell>
      <div className="space-y-8">
        <header className="rounded-[32px] border border-white/10 bg-white/5 p-8">
          <p className="text-xs uppercase tracking-[0.32em] text-cyan-200/80">Software profile</p>
          <h2 className="mt-4 text-4xl font-semibold">{software.title}</h2>
          <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">{software.summary}</p>
          <div className="mt-6 flex flex-wrap gap-2">
            {((software.metadata.languages as string[] | undefined) ?? []).map((language) => (
              <Tag key={language}>{language}</Tag>
            ))}
            <Tag tone="warm">{String(software.metadata.license ?? "Unknown licence")}</Tag>
            <Tag>{String(software.metadata.status ?? "unknown")}</Tag>
          </div>
        </header>

        <Section eyebrow="Algorithms and scope" title="Metadata">
          <div className="grid gap-4 xl:grid-cols-2">
            <div className="rounded-3xl border border-white/10 bg-slate-950/40 p-5">
              <p className="text-sm text-slate-400">MSC coverage</p>
              <div className="mt-3 flex flex-wrap gap-2">
                {((software.metadata.msc_codes as string[] | undefined) ?? []).map((code) => (
                  <Tag key={code}>{code}</Tag>
                ))}
              </div>
            </div>
            <div className="rounded-3xl border border-white/10 bg-slate-950/40 p-5">
              <p className="text-sm text-slate-400">Algorithms</p>
              <div className="mt-3 flex flex-wrap gap-2">
                {((software.metadata.algorithms as string[] | undefined) ?? []).map((algorithm) => (
                  <Tag key={algorithm}>{algorithm.replace("algorithm:", "")}</Tag>
                ))}
              </div>
            </div>
          </div>
        </Section>

        <Section eyebrow="Why this?" title="Related software recommendations">
          <div className="grid gap-4 xl:grid-cols-2">
            {recommendations.map((recommendation) => (
              <div className="rounded-[24px] border border-cyan-400/20 bg-cyan-400/5 p-5" key={recommendation.node.id}>
                <div className="flex items-center justify-between gap-4">
                  <h3 className="text-xl font-semibold text-slate-50">{recommendation.node.title}</h3>
                  <Tag tone="accent">{recommendation.score.toFixed(1)}</Tag>
                </div>
                <p className="mt-3 text-sm leading-6 text-slate-200">{recommendation.explanation.plain_language}</p>
                <div className="mt-4 flex flex-wrap gap-2">
                  {recommendation.explanation.signals.map((signal) => (
                    <Tag key={signal}>{signal}</Tag>
                  ))}
                </div>
                <ol className="mt-4 space-y-2 text-sm text-slate-300">
                  {recommendation.explanation.path.map((step) => (
                    <li key={step}>{step}</li>
                  ))}
                </ol>
              </div>
            ))}
          </div>
        </Section>

        <Section eyebrow="Provenance" title="Source evidence">
          <div className="rounded-[24px] border border-white/10 bg-slate-950/40 p-5">
            <p className="text-sm text-slate-400">Source</p>
            <p className="mt-2 text-base text-slate-100">{software.provenance.source}</p>
            <p className="mt-4 text-sm text-slate-400">Evidence</p>
            <p className="mt-2 text-sm leading-6 text-slate-300">{software.provenance.evidence}</p>
            <p className="mt-4 text-sm text-slate-400">Retrieved</p>
            <p className="mt-2 font-mono text-xs text-slate-300">{software.provenance.retrieved_at}</p>
          </div>
        </Section>
      </div>
    </AppShell>
  );
}
