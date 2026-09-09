FROM node:22-slim

WORKDIR /app

COPY package.json pnpm-workspace.yaml turbo.json tsconfig.base.json ./
COPY apps/web ./apps/web
COPY packages ./packages
COPY data ./data
COPY scripts ./scripts

RUN corepack enable && pnpm install --no-frozen-lockfile
RUN pnpm --filter @axiom-atlas/web build

WORKDIR /app/apps/web

CMD ["pnpm", "start"]
