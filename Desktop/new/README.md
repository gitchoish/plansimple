# SolveSteps - Interactive Situation Solver Tools

An Astro + Tailwind CSS static site with interactive tools to help people solve real-life situations. Free, private, and AdSense-ready.

## 🚀 Features

- **3 Interactive Tools**
  - Checklist Builder: Create and track actionable steps
  - Weekly Planner: Plan focus areas and daily actions
  - Routine Builder: Design and time custom routines

- **8 Situation Pages** covering:
  - Moving to a new apartment
  - Weekly cleaning routine
  - Budget reset
  - Exam study planning
  - Managing overwhelming weeks
  - Morning routine building
  - Weekend home reset
  - Burnout-free week planning

- **Full AdSense Compliance**
  - Privacy Policy
  - Terms of Use
  - About & Disclaimer pages
  - Contact page
  - Robots.txt and ads.txt

- **100% Private & Secure**
  - All data stays on user's device (localStorage)
  - No backend, no database
  - No tracking or analytics
  - No external APIs

- **Mobile-Responsive Design**
  - Tailwind CSS styling
  - Print-friendly pages
  - Fast static site generation

## 📋 Tech Stack

- **Framework**: Astro 4.x
- **Styling**: Tailwind CSS 3.x
- **Language**: TypeScript
- **Deployment**: Cloudflare Pages
- **Build**: Static Site Generation (SSG)

## 🛠️ Local Development

### Prerequisites
- Node.js 18+ installed
- npm or pnpm

### Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Visit `http://localhost:3000` in your browser.

### Build for Production

```bash
npm run build
```

This generates a static `/dist` folder ready for deployment.

### Preview Production Build

```bash
npm run preview
```

## 🚀 Deployment on Cloudflare Pages

### Option 1: Via GitHub (Recommended)

1. Push this repository to GitHub
2. Go to [Cloudflare Pages](https://pages.cloudflare.com/)
3. Click "Create a project" → "Connect to Git"
4. Select your GitHub repo
5. Fill in these settings:
   - **Framework**: Astro
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
   - **Root directory**: `/`
6. Click "Save and Deploy"

Your site will deploy automatically on every push to the selected branch.

### Option 2: Direct Upload

1. Build locally: `npm run build`
2. Drag and drop the `/dist` folder to Cloudflare Pages
3. Your site will be live in seconds

## 💰 Adding Google AdSense

### Step 1: Update ads.txt

1. Get your AdSense Publisher ID from Google AdSense console
2. Open `/public/ads.txt`
3. Replace `pub-xxxxxxxxxxxxxxxx` with your actual Publisher ID

### Step 2: Add AdSense Code

1. Get your AdSense script code from Google AdSense
2. Open `/src/layouts/Layout.astro`
3. Add the script to the `<head>` section:

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-xxxxxxxxxxxxxxxx"
     crossorigin="anonymous"></script>
```

### Step 3: Verify in Google AdSense

- Go to your AdSense console
- Check "Ads.txt" status
- Allow 24-48 hours for full verification

## 📝 Adding New Situations

To add a new situation page:

1. Create a new file in `/src/pages/situations/`
2. Use the moving-apartment.astro as a template
3. Import the tool component you need (Checklist, Planner, or Routine)
4. Add the link to the situations index page
5. Add entry to the home page featured situations

Example:

```astro
---
import Layout from '../../layouts/Layout.astro';
import SituationChecklist from '../../components/SituationChecklist.astro';
---

<Layout title="Your Situation - SolveSteps">
  <!-- Your content -->
  <SituationChecklist 
    title="Your Situation"
    situationId="your-situation-id"
    steps={["Step 1", "Step 2", ...]}
  />
</Layout>
```

## 🎨 Customization

### Colors & Branding

Edit `/tailwind.config.mjs`:

```javascript
theme: {
  extend: {
    colors: {
      primary: '#your-color'
    }
  }
}
```

### Site Metadata

Edit `/astro.config.mjs`:

```javascript
export default defineConfig({
  site: 'https://your-domain.com',
  // ...
});
```

## 📊 Project Structure

```
src/
├── components/
│   ├── SituationChecklist.astro    # Interactive checklist tool
│   ├── WeeklyPlanner.astro         # Weekly planning tool
│   └── RoutineBuilder.astro        # Routine building tool
├── layouts/
│   └── Layout.astro                # Master layout with nav/footer
├── pages/
│   ├── index.astro                 # Home page
│   ├── about.astro                 # About page
│   ├── contact.astro               # Contact page
│   ├── privacy-policy.astro        # Privacy policy (AdSense required)
│   ├── terms.astro                 # Terms of use (AdSense required)
│   └── situations/
│       ├── index.astro             # All situations index
│       ├── moving-apartment.astro  # Example situation
│       └── [7 more situation pages...]
└── styles/
    └── global.css                  # Global Tailwind styles

public/
├── robots.txt                      # SEO robots configuration
└── ads.txt                         # Google AdSense configuration
```

## 🔒 Privacy & Data

- **No data collection**: This site uses localStorage only
- **No cookies**: No tracking cookies
- **No analytics**: No Google Analytics or similar
- **No backend**: Everything is static files
- **No third-party services**: Except Cloudflare (hosting provider)

Users own their data completely. When they clear browser storage, their plan data is deleted locally.

## 📱 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🆘 Troubleshooting

### Build fails with "port already in use"

```bash
# Kill process using port 3000
# On Windows:
taskkill /F /IM node.exe

# On Mac/Linux:
lsof -ti:3000 | xargs kill -9
```

### Cloudflare deployment fails

- Check that `npm run build` works locally
- Verify `astro.config.mjs` has correct site URL
- Check that Node.js version is 18+
- Review Cloudflare build logs for errors

### Tools not saving progress

- User has localStorage disabled (rare)
- Browser in private/incognito mode (localStorage not persisted)
- Too much data for localStorage quota (very rare, >5MB)

## 📄 License

This project is open source and free to use.

## 🤝 Contributing

Found a bug? Have a suggestion for a new situation?
Email: hello@solvesteps.io

---

**Happy solving! 🎯**

Built with Astro, powered by Cloudflare Pages, ready for AdSense approval.