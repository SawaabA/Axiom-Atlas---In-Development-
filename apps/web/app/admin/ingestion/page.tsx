import { getIngestionJobs } from "@axiom-atlas/api-client";
import { Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../../../components/app-shell";

export default async function IngestionAdminPage() {
  const jobs = await getIngestionJobs();

  return (
    <AppShell>
      <div className="space-y-8">
        <header>
          <p className="text-xs uppercase tracking-[0.32em] text-cyan-200/80">Ingestion admin</p>
          <h2 className="mt-4 text-4xl font-semibold">Phase 2 pipeline visibility</h2>
          <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">
            Job state, record counts, and checkpoints are stored in Postgres so ingestion can be audited and resumed instead of running as an opaque script.
          </p>
        </header>

        <Section eyebrow="Jobs" title="Recent ingestion runs">
          {jobs.length === 0 ? (
            <p className="text-sm leading-6 text-slate-300">
              No ingestion jobs are recorded yet. Run the Zenodo sync endpoint or the worker task to populate this view.
            </p>
          ) : (
            <div className="space-y-4">
              {jobs.map((job) => (
                <div className="rounded-[24px] border border-white/10 bg-slate-950/40 p-5" key={job.id}>
                  <div className="flex flex-wrap items-center gap-2">
                    <Tag tone={job.status === "completed" ? "accent" : "warm"}>{job.status}</Tag>
                    <Tag>{job.source_name}</Tag>
                  </div>
                  <p className="mt-3 font-mono text-xs text-slate-400">{job.id}</p>
                  <div className="mt-4 grid gap-3 md:grid-cols-3">
                    <div>
                      <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Fetched</p>
                      <p className="mt-2 text-2xl font-semibold text-slate-100">{job.records_fetched}</p>
                    </div>
                    <div>
                      <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Normalized</p>
                      <p className="mt-2 text-2xl font-semibold text-slate-100">{job.records_normalized}</p>
                    </div>
                    <div>
                      <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Failed</p>
                      <p className="mt-2 text-2xl font-semibold text-slate-100">{job.records_failed}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </Section>
      </div>
    </AppShell>
  );
}
