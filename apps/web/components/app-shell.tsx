import Link from "next/link";
import { PropsWithChildren } from "react";

const links = [
  { href: "/discover", label: "Discover" },
  { href: "/search?q=software", label: "Search" },
  { href: "/atlas", label: "Atlas" },
  { href: "/communities/community:computational-algebra", label: "Communities" },
  { href: "/workspace", label: "Workspace" },
  { href: "/admin/ingestion", label: "Ingestion" }
];

export function AppShell({ children }: PropsWithChildren) {
  return (
    <div className="min-h-screen bg-atlas-background text-slate-50">
      <div className="mx-auto grid min-h-screen max-w-[1600px] grid-cols-1 gap-6 px-4 py-4 lg:grid-cols-[240px_minmax(0,1fr)]">
        <aside className="rounded-[32px] border border-white/10 bg-white/5 p-6 lg:sticky lg:top-4 lg:h-[calc(100vh-2rem)]">
          <div>
            <p className="text-xs uppercase tracking-[0.4em] text-cyan-200/75">Axiom Atlas</p>
            <h1 className="mt-3 text-2xl font-semibold">Scholarly constellation</h1>
            <p className="mt-3 text-sm leading-6 text-slate-300">
              Navigate mathematical software, papers, algorithms, and research communities through real graph relationships.
            </p>
          </div>
          <nav className="mt-8 space-y-2">
            {links.map((link) => (
              <Link
                className="block rounded-2xl border border-transparent px-4 py-3 text-sm text-slate-200 transition hover:border-white/10 hover:bg-white/5"
                href={link.href}
                key={link.href}
              >
                {link.label}
              </Link>
            ))}
          </nav>
          <div className="mt-10 rounded-3xl border border-cyan-400/20 bg-cyan-400/10 p-4">
            <p className="text-sm font-medium text-cyan-100">Phase 1 foundation</p>
            <p className="mt-2 text-sm leading-6 text-cyan-50/80">
              Fixture-backed graph, API search, explainable recommendation baseline, and 3D preview are active.
            </p>
          </div>
        </aside>
        <main className="rounded-[32px] border border-white/10 bg-[linear-gradient(180deg,rgba(17,24,39,0.95),rgba(7,10,18,0.98))] p-6 shadow-atlas lg:p-8">
          <form action="/search" className="mb-8 rounded-[24px] border border-white/10 bg-white/5 p-4">
            <label className="block text-xs uppercase tracking-[0.28em] text-slate-400" htmlFor="global-search">
              Universal search
            </label>
            <div className="mt-3 flex flex-col gap-3 md:flex-row">
              <input
                className="w-full rounded-2xl border border-white/10 bg-slate-950/60 px-4 py-3 text-sm text-slate-100 outline-none placeholder:text-slate-500"
                defaultValue=""
                id="global-search"
                name="q"
                placeholder="Search software, papers, algorithms, or communities"
                type="search"
              />
              <button className="rounded-2xl bg-cyan-400 px-5 py-3 text-sm font-semibold text-slate-950" type="submit">
                Search
              </button>
            </div>
          </form>
          {children}
        </main>
      </div>
    </div>
  );
}
