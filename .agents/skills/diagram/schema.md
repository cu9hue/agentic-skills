# diagram model schema

One system → one `model.json`. The renderer (`render.mjs`) injects it into `template.html`.
Everything is optional except `meta`, `layers`, `nodes`, `edges`. Tabs auto-hide when their data is empty.

Edge keys everywhere use the literal arrow `→` (U+2192): `"from→to"`.

```jsonc
{
  "meta": {
    "system": "indexer",              // REQUIRED. short id, used for the output filenames
    "title": "Event Indexer",         // header title
    "subtitle": "raw events → normalized.* on Kafka",
    "icon": "🧭",                     // one emoji, becomes favicon + header prefix
    "repo": "your-org/your-repo",     // STRICTLY owner/name — file:line citations become GitHub deep links
    "branch": "main",                 // optional; git ref for those links (default main)
    "source": "branch feat/streaming"  // optional free-text provenance (which checkout this scan
                                      // ran against). Display-only — NEVER stuff provenance into
                                      // "repo"; it breaks the deep links.
  },

  // Horizontal bands, top → bottom. Node.layer must reference one of these ids.
  "layers": [
    { "id": "source",  "label": "Source" },
    { "id": "ingest",  "label": "Ingest" },
    { "id": "control", "label": "Control plane" }
  ],

  // Edge/wire kinds. color drives node accent + edge stroke + legend. dash = SVG dasharray ("" = solid).
  "connectionTypes": {
    "kafka":        { "color": "#ef4444", "dash": "",    "label": "Kafka topic" },
    "redis-pubsub": { "color": "#f59e0b", "dash": "7 4", "label": "Redis pub/sub" },
    "inmem":        { "color": "#10b981", "dash": "",    "label": "in-process" },
    "control":      { "color": "#64748b", "dash": "5 5", "label": "control plane" }
  },
  // If omitted, a sensible default palette is used (kafka, redis-pubsub, redis-cache,
  // ws, http, grpc, inmem, db, control).

  // Components. KEY = stable node id (referenced by edges and edgeMessages).
  // Position is AUTO-COMPUTED from layer + col. Do NOT set x/y unless overriding.
  "nodes": {
    "indexer": {
      "layer": "ingest",             // REQUIRED, must match a layers[].id
      "region": "main",              // "main" (default) or "side" (control plane etc → right column)
      "col": 0,                      // ordering hint within a (layer,region) row, left→right
      "label": "Indexer",            // REQUIRED
      "sub": "services/indexer",     // small mono subtitle under the label
      "desc": "The sole producer of normalized.* topics. Turns raw events into ...",
      "files": ["services/indexer/src/sink.rs:167"],   // cite file:line
      "io": [["in", "raw events"], ["out", "normalized.* on Kafka"]],
      "msgs": ["IndexedEventEnvelope", "wire frame"],            // shown as pills
      "gotchas": [["Idempotent producer; a replay can double-publish if acks aren't all."]],
      "note": "optional free extra note shown in the detail pane",
      "color": "#ef4444",            // optional accent override (else derived from edges)
      "only": "somescenario",        // optional: node exists only in this scenario (proposals)
      "links": [["Runbook", "https://…"], ["Dashboard", "https://…"]]  // optional external links
      // "x": 175, "y": 104, "w": 200, "h": 46   // optional hard override of auto-layout
    }
  },

  // Directed wires. type must match a connectionTypes key.
  "edges": [
    { "from": "indexer", "to": "kafka", "type": "kafka",
      "label": "normalized.* (protobuf)",
      "scenarios": ["full", "market"],  // which flow presets light this edge
      "lpos": 0.5 }                      // optional 0..1 label position along the curve
  ],

  // Field-level payloads per wire, keyed "from→to". Powers the edge detail pane.
  "edgeMessages": {
    "indexer→kafka": {
      "what": "One protobuf record per normalized event, in a length-prefixed frame.",
      "payloads": [
        ["IndexedEventEnvelope (proto)", "source/partition/cursor + one of ~13 *Fact payloads"],
        ["wire frame", "16-byte header: magic, version, message_type, payload_len"]
      ]
    }
  },

  // Flow presets (left sidebar). "full" is auto-added. A scenario dims everything
  // except its path. Give EITHER path (ordered edge keys, also drives the ▶ animation)
  // OR nodes (ids to keep lit); omit both to derive from edge.scenarios tags.
  "scenarios": [
    { "id": "market", "name": "Market-data tick", "desc": "One update, source → browser.",
      "path": ["source→indexer", "indexer→kafka", "kafka→consumer"] }
  ],

  // State machines. Diagram is auto-laid-out from transitions (BFS columns from start).
  "stateMachines": [
    { "id": "conn", "name": "Client connection", "path": "services/live/src/ws.rs:66",
      "states": ["idle", "active", "closed"], "start": "idle",
      "terminal": ["closed"], "extra": ["rejected"],   // extra = off-happy-path states
      "transitions": [
        ["idle", "active", "upgrade accepted; register_connection"],
        ["active", "closed", "client close / read error"]
      ] }
  ],

  // "Pipeline" tab: numbered end-to-end stages.
  "pipeline": {
    "title": "The five-hop pipeline", "lede": "One update travels N concrete stages ...",
    "stages": [
      { "name": "Indexer produce", "actor": "indexer (KafkaSink)", "type": "kafka",
        "desc": "Route each envelope to its topic, key by shard, PUBLISH." }
    ]
  },

  // "Messages" tab: cards. Each group is pills | fields | table.
  "messages": {
    "title": "Message catalog", "lede": "Two wire protocols ...",
    "groups": [
      { "title": "Public methods", "layout": "pills", "items": ["auth", "subscribe"] },
      { "title": "LiveClientMessage", "layout": "fields",
        "fields": [["Subscribe", "pool/shard/channel"], ["Ping", "keepalive"]] },
      { "title": "Kafka topics", "layout": "table",
        "columns": ["topic", "carries", "consumed by"],
        "rows": [["normalized.market_executions", "public trade tape", "market-execution"]] }
    ]
  },

  // "Facts & rationale" tab.
  "facts": ["Headline fact 1 ...", "Headline fact 2 ..."],
  "rationale": [["Why a separate consumer tier", "The live stream must be ..."]],
  "gotchas": [["Shard-count skew silently drops deltas", "If publisher and subscriber ..."]],

  // Optional extra custom tabs (freeform HTML), e.g. a "v2 proposal" tab.
  "extras": [
    { "id": "v2", "name": "News v2 ✦", "html": "<h2>...</h2><div class='grid'>...</div>" }
  ]
}
```

## Rules of thumb for a good model
- 12–24 nodes. More than ~28 and the map gets noisy; split into sub-systems or use `region:"side"`.
- Every `desc` is concrete and cites at least one `file:line`. No hand-waving.
- `gotchas` are the real sharp edges (races, silent drops, footguns), not generic caveats.
- Order layers so the dominant data flow runs top → bottom; put control/infra planes in `region:"side"`.
- Keep node ids short and descriptive — `edges` and `edgeMessages` key off them.

