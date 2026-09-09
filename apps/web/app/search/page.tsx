import Link from "next/link";

import { search } from "@axiom-atlas/api-client";
import { Section, Tag } from "@axiom-atlas/ui";

import { AppShell } from "../../components/app-shell";

const entityHref = (type: string, id: string) => {
  if (type === "software") {
    return `/software/${encodeURIComponent(id)}`;
  }
  if (type === "community") {
    return `/communities/${encodeURIComponent(id)}`;
  }
  return "#";
};

export default async function SearchPage({
  searchParams
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const params = await searchParams;
  const query = params.q?.trim() ?? "";
  const results = query.length >= 2 ? await search(query) : [];

  return (
    <AppShell>
      <div className="space-y-8">
        <header>
          <p className="text-xs uppercase tracking-[0.32em] text-cyan-200/80">Search</p>
          <h2 className="mt-4 text-4xl font-semibold">Hybrid-ready entity search</h2>
          <p className="mt-4 max-w-3xl text-lg leading-8 text-slate-300">
            This page uses the API first. In fixture mode it falls back locally, and once Zenodo-backed indexing is populated it will read from OpenSearch through the backend repository.
          </p>
        </header>

        <Section eyebrow="Results" title={query ? `Search results for "${query}"` : "Enter a query"}>
          {query.length < 2 ? (
            <p className="text-sm leading-6 text-slate-300">
              Try queries like <span className="font-medium text-slate-100">symbolic algebra</span>, <span className="font-medium text-slate-100">python software</span>, or <span className="font-medium text-slate-100">computational algebra</span>.
            </p>
          ) : results.length === 0 ? (
            <p className="text-sm leading-6 text-slate-300">
              No exact matches were found. Try broadening the wording or removing a domain constraint.
            </p>
          ) : (
            <div className="space-y-4">
              {results.map((result) => (
                <Link
                  className="block rounded-[24px] border border-white/10 bg-slate-950/40 p-5 transition hover:border-cyan-400/40"
                  href={entityHref(result.node.type, result.node.id)}
                  key={result.node.id}
                >
                  <div className="flex flex-wrap items-center gap-2">
                    <Tag tone="accent">{result.node.type}</Tag>
                    {result.reasons.map((reason) => (
                      <Tag key={reason}>{reason}</Tag>
                    ))}
                  </div>
                  <h3 className="mt-4 text-xl font-semibold">{result.node.title}</h3>
                  <p className="mt-3 text-sm leading-6 text-slate-300">{result.node.summary}</p>
                </Link>
              ))}
            </div>
          )}
        </Section>
      </div>
    </AppShell>
  );
}
