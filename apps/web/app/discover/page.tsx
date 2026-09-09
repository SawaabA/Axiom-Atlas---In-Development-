import Link from "next/link";

import { getIngestionJobs, getSoftware } from "@axiom-atlas/api-client";
import { Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../../components/app-shell";

export default async function DiscoverPage() {
  const [software, jobs] = await Promise.all([getSoftware(), getIngestionJobs()]);

  return (
    <AppShell>
      <div className="space-y-8">
        <header>
          <p className="text-xs uppercase tracking-[0.32em] text-cyan-200/80">Discovery dashboard</p>
          <h2 className="mt-4 text-4xl font-semibold">Working recommendation and exploration surface</h2>
          <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">
            This Phase 1 dashboard is already wired to API search and seeded recommendation logic, so each entity card can lead into explainable graph detail pages rather than static marketing copy.
          </p>
        </header>

        <Section eyebrow="Continue exploring" title="Software collection">
          <div className="grid gap-4 xl:grid-cols-2">
            {software.map((node) => (
              <Link
                className="rounded-[24px] border border-white/10 bg-white/5 p-5 transition hover:border-cyan-400/40"
                href={`/software/${encodeURIComponent(node.id)}`}
                key={node.id}
              >
                <div className="flex flex-wrap gap-2">
                  {((node.metadata.languages as string[] | undefined) ?? []).map((language) => (
                    <Tag key={language}>{language}</Tag>
                  ))}
                  <Tag tone="warm">{String(node.metadata.status ?? "unknown")}</Tag>
                </div>
                <h3 className="mt-4 text-xl font-semibold">{node.title}</h3>
                <p className="mt-3 text-sm leading-6 text-slate-300">{node.summary}</p>
              </Link>
            ))}
          </div>
        </Section>

        <Section eyebrow="Ingestion state" title="Latest pipeline activity">
          {jobs.length === 0 ? (
            <p className="text-sm leading-6 text-slate-300">
              The repository is ready for Zenodo ingestion, but no completed backend job is recorded yet in this environment.
            </p>
          ) : (
            <div className="grid gap-4 xl:grid-cols-3">
              {jobs.slice(0, 3).map((job) => (
                <div className="rounded-[24px] border border-white/10 bg-slate-950/40 p-5" key={job.id}>
                  <div className="flex flex-wrap gap-2">
                    <Tag tone={job.status === "completed" ? "accent" : "warm"}>{job.status}</Tag>
                    <Tag>{job.source_name}</Tag>
                  </div>
                  <p className="mt-4 text-sm leading-6 text-slate-300">
                    {job.records_normalized} normalized entities from {job.records_fetched} fetched records.
                  </p>
                </div>
              ))}
            </div>
          )}
        </Section>
      </div>
    </AppShell>
  );
}
