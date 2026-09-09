import clsx from "clsx";
import type { PropsWithChildren, ReactNode } from "react";

export function cn(...values: Array<string | undefined | false>) {
  return clsx(values);
}

export function Section({
  title,
  eyebrow,
  action,
  children
}: PropsWithChildren<{ title: string; eyebrow?: string; action?: ReactNode }>) {
  return (
    <section className="rounded-[28px] border border-white/10 bg-white/5 p-6 shadow-[0_24px_80px_rgba(4,8,18,0.32)]">
      <div className="mb-5 flex items-start justify-between gap-4">
        <div>
          {eyebrow ? <p className="text-xs uppercase tracking-[0.28em] text-cyan-200/80">{eyebrow}</p> : null}
          <h2 className="mt-2 text-2xl font-semibold text-slate-50">{title}</h2>
        </div>
        {action}
      </div>
      {children}
    </section>
  );
}

export function Tag({ children, tone = "default" }: PropsWithChildren<{ tone?: "default" | "accent" | "warm" }>) {
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-full border px-3 py-1 text-xs font-medium",
        tone === "default" && "border-white/10 bg-white/5 text-slate-200",
        tone === "accent" && "border-cyan-400/30 bg-cyan-400/10 text-cyan-100",
        tone === "warm" && "border-amber-400/30 bg-amber-400/10 text-amber-100"
      )}
    >
      {children}
    </span>
  );
}

export function MetricCard({ label, value, detail }: { label: string; value: string; detail: string }) {
  return (
    <div className="rounded-3xl border border-white/10 bg-slate-950/40 p-5">
      <p className="text-sm text-slate-400">{label}</p>
      <p className="mt-3 text-3xl font-semibold text-slate-50">{value}</p>
      <p className="mt-2 text-sm text-slate-300">{detail}</p>
    </div>
  );
}

export function EntityCard({
  title,
  summary,
  metadata,
  href
}: {
  title: string;
  summary: string;
  metadata: ReactNode;
  href?: string;
}) {
  const content = (
    <div className="group rounded-[24px] border border-white/10 bg-slate-950/40 p-5 transition hover:border-cyan-400/40 hover:bg-slate-900/70">
      <h3 className="text-lg font-semibold text-slate-50">{title}</h3>
      <p className="mt-3 text-sm leading-6 text-slate-300">{summary}</p>
      <div className="mt-4 flex flex-wrap gap-2">{metadata}</div>
    </div>
  );

  if (!href) {
    return content;
  }

  return <a href={href}>{content}</a>;
}
