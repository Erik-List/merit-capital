<!-- 512a8da5-d1f6-4b80-a8b7-31415236f76b 16fd27f9-c8e3-4faa-af81-c62814ed1f36 -->
# Multi-page refactor and navigation update

## Routes and page ownership
- Home (`/`): Hero + Leaderboard table
- Leaderboard (`/leaderboard`): Same content as Home (shared component)
- Rate (`/rate`): Use the former validation RatingSection (marketing/explainer)
- Awards (`/awards`): Awards section
- Economics (`/economics`): Economics section
- Economics Estimates (`/economics/estimates`): Move content from current `/economic-estimates`
- Supporters (`/supporters`): Supporters section
- Next Steps (`/next-steps`): Continuation section
- Investor (`/investor/[slug]`): Keep as-is

## Component relocation (before deleting /validation)
- Create `components/marketing/` and move these from `app/validation/components/sections/`:
  - `HeroSection.tsx`
  - `RatingSection.tsx`
  - `Awards.tsx`
  - `Economics.tsx`
  - `Supporters.tsx`
  - `Continuation.tsx`
- Optional: Move `CinematicIntro.tsx` to `components/marketing/` if you still want an Intro replay link.
- Do not move `InvestorSections.tsx` (explicitly delete per request).

## Pages to create/update (replace deprecated ones)
- Replace `app/page.tsx` with Home content that imports `HeroSection` + Leaderboard table (`components/leaderboard/*`).
- Keep `app/leaderboard/page.tsx` but refactor it to import the same shared `HomeContent` component to avoid duplication (e.g., `components/marketing/HomeContent.tsx`).
- Replace `app/rate/page.tsx` to render `components/marketing/RatingSection` only.
- Create new pages:
  - `app/awards/page.tsx` → render `components/marketing/Awards`.
  - `app/economics/page.tsx` → render `components/marketing/Economics`.
  - `app/economics/estimates/page.tsx` → move content from `app/economic-estimates/page.tsx`.
  - `app/supporters/page.tsx` → render `components/marketing/Supporters`.
  - `app/next-steps/page.tsx` → render `components/marketing/Continuation`.
- Add a redirect from `/economic-estimates` to `/economics/estimates`:
  - Either update `next.config.js` redirects, or turn `app/economic-estimates/page.tsx` into a tiny server component using `redirect('/economics/estimates')` from `next/navigation`.

## Navigation bar
- Place `NavBar` in `app/layout.tsx` (root layout) above `{children}` to prevent per-page height/spacing drift.
- Simplify `components/nav-bar.tsx` by removing the Sections dropdown and inlining links:
  - Intro (action or link), Home, Leaderboard, Rate, Awards, Economics, Estimates, Supporters, Next Steps
  - Mark active route via `usePathname()`; use semantic nav with proper aria-current.
  - Keep a responsive collapse (hamburger) for small screens.

## Global default content width
- Apply a narrower default width for all pages at the layout level:
  - Wrap `{children}` in `app/layout.tsx` with `div className="container mx-auto max-w-5xl px-4"`.
  - Optionally, set `container` defaults in `tailwind.config.ts` (`center: true`, `padding`, narrower `screens`) for consistency.

## Cleanup
- After all imports are updated and pages exist, delete the entire `app/validation/` directory.
- Delete `middleware.ts` so all pages are accessible.
- Remove any now-dead imports/usages (e.g., background loading hooks tied to validation).

## Notes
- Keep `/investor/[slug]` unchanged.
- If you keep Intro replay, wire `onReplayIntro` from `NavBar` to a client-side handler on Home; otherwise, drop the Intro entirely.
- Verify dark-mode styles once width/layout changes are in place.


### To-dos

- [ ] Move sections to components/marketing and update imports
- [ ] Create components/marketing/HomeContent to compose Hero + Leaderboard
- [ ] Replace app/page.tsx to render HomeContent
- [ ] Make /leaderboard render HomeContent
- [ ] Replace app/rate/page.tsx with marketing RatingSection
- [ ] Create app/awards/page.tsx rendering Awards
- [ ] Create app/economics/page.tsx rendering Economics
- [ ] Create app/economics/estimates/page.tsx (move content)
- [ ] Redirect /economic-estimates to /economics/estimates
- [ ] Create app/supporters/page.tsx rendering Supporters
- [ ] Create app/next-steps/page.tsx rendering Continuation
- [ ] Render NavBar in app/layout.tsx above children
- [ ] Inline links in NavBar; remove dropdown; active route styling
- [ ] Wrap children with container max-w-5xl in layout
- [ ] Delete app/validation after refactor and import updates
- [ ] Delete middleware.ts for open access