import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "../../packages/ui/src/**/*.{ts,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        atlas: {
          background: "#070A12",
          surface: "#111827",
          elevated: "#182235",
          cyan: "#46D9E8",
          amber: "#F2B84B",
          violet: "#9A86FD"
        }
      },
      boxShadow: {
        atlas: "0 30px 80px rgba(6, 10, 22, 0.45)"
      }
    }
  },
  plugins: []
};

export default config;
