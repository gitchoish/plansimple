import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://solvesteps.pages.dev',
  integrations: [tailwind()],
  output: 'static',
});
