const required = [
  "NEXT_PUBLIC_API_BASE_URL",
  "NEXT_PUBLIC_APP_URL",
  "API_HOST",
  "API_PORT",
  "ML_SERVICE_HOST",
  "ML_SERVICE_PORT",
  "FIXTURE_DATA_PATH"
];

const missing = required.filter((key) => !process.env[key]);

if (missing.length > 0) {
  console.error(`Missing required environment variables: ${missing.join(", ")}`);
  process.exit(1);
}

console.log("Environment validation passed.");
