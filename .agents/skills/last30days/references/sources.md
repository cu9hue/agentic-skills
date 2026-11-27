# Sources: calls, date fields, fallbacks

Checked against this environment on 2026-11-26; the treg X fallback and
YouTube comments on 2026-11-27. Every call here is read-only.
Never post, react, follow or message through the `social` MCP in this skill.

Set the window once per run and reuse it:

```bash
SINCE=$(date -u -v-30d +%F 2>/dev/null || date -u -d '30 days ago' +%F)
TS=$(date -u -j -f %F "$SINCE" +%s 2>/dev/null || date -u -d "$SINCE" +%s)
OUT="$SCRATCHPAD/last30days/$(date +%s)"; mkdir -p "$OUT"
treg balance | grep Balance > "$OUT/balance-start.txt"
```

`$SCRATCHPAD` is the session scratchpad directory. Keep every raw response
in `$OUT`, one file per call, so a quote can be traced to its row.

treg prints the JSON on stdout and its charge line on stderr. Keep them
apart: `treg call ... > "$OUT/x.json" 2>> "$OUT/charges.log"`. Merging the
streams breaks the JSON.

Parse with `python3 -I` reading the saved file. Never pipe a response into
an interpreter run from inside `$OUT`.

## Date filter: every source, every row

No paid search endpoint here filters by date. TikTok, Instagram and YouTube
searches return items from 2024 and 2025 next to this week's. Drop any row
whose date is before `$SINCE`. A row with no readable date is not evidence
for a 30-day claim: drop it, or use it only as dated-unknown context and say
so.

| Source | Date field | Engagement fields |
|---|---|---|
| X (`social_search`) | `created_at` | `provider_metadata.metrics.{likes,retweets,replies,views,bookmarks}` (top-level `engagement` is null) |
| X (treg) | `createdUtc` (epoch) | `likeCount`, `retweetCount`, `replyCount`, `viewCount` |
| Reddit (treg) | `created_utc` (epoch) | `score`, `num_comments` |
| Hacker News | `created_at_i` (epoch) | `points`, `num_comments` |
| YouTube (treg) | `published_time`, relative ("2 weeks ago") | `number_of_views` |
| TikTok (treg) | `aweme_info.create_time` (epoch) | `aweme_info.statistics.{play_count,digg_count,comment_count}` |
| Instagram (treg) | `createdUtc` (epoch) | `views`, `likes`, `comments` |
| Exa / WebSearch | publish date on the page | none |

YouTube: keep "N hours/days ago" and "1–4 weeks ago". Drop "1 month ago"
and older; the relative label cannot place it inside the window.

## X — `social` MCP, free

Load with ToolSearch (`select:mcp__social__social_search,mcp__social__social_get_thread`).
Search returns newest first, so a bare query returns low-engagement noise.
Put the window and an engagement floor into the query; X operators work:

```
social_search(platforms=["x"], limit=25,
  query="<terms> since:<SINCE> min_faves:50 lang:en")
```

- One phrase per search. `OR` in the query drops the `min_faves` floor and
  returns newest-first noise.
- Floor: start at `min_faves:50`. Fewer than 5 rows → retry at 10. A big
  topic (a major company, a viral story) → 500 or 1000.
- `from:<handle>` reads the subject's own posts. A product's or person's
  own account is primary evidence for what they shipped or said.
- `social_get_thread(platform="x", post_id=<id>)` reads replies. Replies
  to a "what's the best X?" post are the strongest endorsement signal.
  The result can mix in unrelated posts: keep only rows whose
  `provider_metadata.inReplyTo.tweetId` is the root post or one of its
  replies.
- Link: `canonical_url`.

### X fallback — treg, $0.00046–0.00048 per call

Use when the `social` MCP is not connected or `social_search` fails. The
query takes the same operators: `since:`, `until:`, `min_faves:`, `lang:`
and quoted phrases all work.

```bash
treg call treg.x.search.posts --method POST \
  --header 'X-Treg-Route-Max-Cost: 0.002' \
  --data '{"q":"\"<phrase>\" since:<SINCE> min_faves:200 lang:en"}' \
  > "$OUT/x-<n>.json" 2>> "$OUT/charges.log"
```

- Keep the cost header. On a miss treg tries the next provider, and the
  third one costs $0.0148 per call.
- Rows: `output.posts[]` with `text`, `authorUsername`, `createdUtc`,
  `likeCount`, `url`, `id`. Link: `url`.
- A search returns 20 posts, weighted to the last few days. To cover the
  whole window, add a second search with `until:<a date mid-window>`.
- Replies: search `conversation_id:<root post id> min_faves:5`. Rows with
  `isReply` true are the replies; `inReplyToId` shows which post each
  answers.
- Viral posts that quote a lab engineer ("This is insane. <company>
  engineer: …") often come from engagement-farm accounts. Do not cite such a
  quote unless the person's own post or talk confirms it.

## Reddit — `social` MCP first, treg when blocked

1. `social_search(platforms=["reddit"], query=...)`. Today it returns
   `completeness: "blocked"` (patchright has no Chrome). Plain `curl` to
   reddit.com returns 403.
2. On "blocked", use treg ($0.00188 per call):

```bash
treg call scrapecreators.reddit.search.posts \
  --query query="<terms>" --query sort=relevance --query timeframe=month \
  --query trim=true > "$OUT/reddit-<n>.json" 2>> "$OUT/charges.log"
```

   Use `sort=relevance`. `sort=top` with `timeframe=month` returns
   sitewide hits that do not match the query. Rows: `posts[]` with
   `title`, `subreddit`, `score`, `num_comments`, `created_utc`, `url`.
3. Comments for the top 2–3 threads ($0.00188 per call). The top comment
   often says more than the post:

```bash
treg call scrapecreators.x.v1-reddit-post-comments \
  --query url="<thread url>" --query trim=true \
  > "$OUT/reddit-comments-<n>.json" 2>> "$OUT/charges.log"
```

   Do not use `crawl4ai.reddit.post.comments`: it returned 0 rows on every
   thread tried (its RSS route 404s).

4. One subreddit's top posts (trending sweep):
   `treg call scrapecreators.reddit.subreddit.posts --query subreddit=<name> --query sort=top`.
   Filter by `created_utc`.

A blog post or digest that summarizes a Reddit thread is web evidence, not
Reddit evidence. Fetch the thread itself when the claim matters.

## Hacker News — Algolia, free

```bash
curl -s "https://hn.algolia.com/api/v1/search?query=<urlencoded terms>&tags=story&numericFilters=created_at_i%3E$TS&hitsPerPage=20" > "$OUT/hn-<n>.json"
curl -s "https://hn.algolia.com/api/v1/items/<objectID>" > "$OUT/hn-item-<id>.json"   # comment tree
curl -s "https://hn.algolia.com/api/v1/search?tags=front_page&hitsPerPage=30" > "$OUT/hn-front.json"
```

Encode `>` as `%3E`; a raw `>` returns an empty body. Thread link:
`https://news.ycombinator.com/item?id=<objectID>`. For a window-wide top
list, add `,points%3E100` to `numericFilters`.

## YouTube — treg, $0.001 per call

```bash
treg call treg.youtube.search.videos --method POST --data '{"q":"<terms>"}' \
  > "$OUT/yt-<n>.json" 2>> "$OUT/charges.log"
```

Rows: `output.videos[]` with `video_id`, `title`, `author`, `number_of_views`,
`published_time`. Link: `https://www.youtube.com/watch?v=<video_id>`.
The free `youtube.youtube.search.videos` needs the user's own YouTube key and
returns 404 without it. Transcript of one video, only when its words carry
a finding: `treg call crawl4ai.youtube.video.captions --method POST --data '{"video":"<video_id>"}'`
($0.00165). The parameter is `video`; `url` returns HTTP 400.

Comments on a top video ($0.0009). Viewer reaction is here, not in the
title. The parameter is `video_id` (not `video`):

```bash
treg call treg.youtube.video.comments --method POST \
  --header 'X-Treg-Route-Max-Cost: 0.002' --data '{"video_id":"<video_id>"}' \
  > "$OUT/yt-comments-<n>.json" 2>> "$OUT/charges.log"
```

Rows: `output.comments[]` with `text`, `likes`, `published` (relative),
`author.handle`, `url` (links to the comment).

## TikTok — treg, $0.001 per call

```bash
treg call treg.tiktok.search.videos --method POST --data '{"q":"<terms>","limit":20}' \
  > "$OUT/tt-<n>.json" 2>> "$OUT/charges.log"
```

Rows: `output.videos[].aweme_info` with `desc`, `create_time`,
`author.unique_id`, `statistics`, `share_url`.

## Instagram reels — treg, $0.0015–0.0019 per call

```bash
treg call treg.instagram.search.reels --method POST --data '{"q":"<terms>"}' \
  > "$OUT/ig-<n>.json" 2>> "$OUT/charges.log"
```

Rows: `output.reels[]` with `caption`, `createdUtc`, `username`, `views`,
`likes`, `url`. Use for consumer, creator and brand topics; skip for
developer tools.

## Polymarket — Gamma, free

```bash
curl -s "https://gamma-api.polymarket.com/public-search?q=<urlencoded>&limit_per_type=10" > "$OUT/pm.json"
```

Keep events where `closed` is false. Each market's `outcomePrices` is a JSON
string of probabilities ("0.017" = 1.7%). Report odds as percentages, never
volume or liquidity. Use only when a market names the topic.

## Web — Exa, then WebSearch

Exa `web_search_exa` with an `objective` that says "published after
<SINCE>; exclude older pages". Check the date on each page you cite. Use
the web for facts the community sources lack: launch dates, prices,
official statements. `web_fetch_exa` reads a page Exa found.

## LinkedIn — `social` MCP, optional

`social_search(platforms=["linkedin"], ...)` uses a browser profile. It may
report "blocked" or "setup not complete". Use it for B2B and hiring topics;
name it as a gap when it fails.

## Spend

The run may spend up to $0.10 on treg without asking. A typical run spends
$0.01–0.03. Before a call would take the run past $0.10, stop and ask. At
the end, report the sum of `$OUT/charges.log` (lines `treg: charged $X`).
The balance is shared by the whole team, so its change can include other
people's calls. Report the logged sum, not the balance difference.
