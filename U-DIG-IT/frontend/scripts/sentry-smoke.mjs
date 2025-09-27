import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import * as Sentry from '@sentry/node';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const candidateEnvPaths = [
  path.resolve(__dirname, '..', '.env'),
  path.resolve(__dirname, '..', '..', '.env'),
  path.resolve(__dirname, '..', '..', '..', '.env'),
];

for (const envPath of candidateEnvPaths) {
  if (!fs.existsSync(envPath)) continue;
  const { parse } = await import('dotenv');
  const parsed = parse(fs.readFileSync(envPath, 'utf8'));
  for (const [key, value] of Object.entries(parsed)) {
    if (!process.env[key]) {
      process.env[key] = value;
    }
  }
}

const dsn = process.env.VITE_FRONTEND_SENTRY_DSN;
if (!dsn) {
  console.error('Missing VITE_FRONTEND_SENTRY_DSN');
  process.exitCode = 1;
  process.exit();
}

const environment = process.env.VITE_FRONTEND_ENVIRONMENT ?? 'development';
const sampleRate = Number(process.env.VITE_FRONTEND_TRACES_SAMPLE_RATE ?? '1');

Sentry.init({
  dsn,
  environment,
  tracesSampleRate: Number.isFinite(sampleRate) ? sampleRate : 1,
});

const eventId = Sentry.captureMessage('U-DIG-IT frontend Sentry smoke test');

const flushed = await Sentry.flush(5000);
if (!flushed) {
  console.error('Failed to flush Sentry event');
  process.exitCode = 1;
} else {
  console.log(JSON.stringify({ eventId, environment }));
}

await Sentry.close(2000);

