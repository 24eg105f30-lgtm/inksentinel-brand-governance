// Vercel serverless function: AI tone review via any OpenAI-compatible provider (OpenRouter, Groq, Cerebras...).
// Default provider: Google Gemini via its OpenAI-compatible endpoint. Only AI_API_KEY (your Gemini key) is required.
// Optional: AI_BASE_URL and AI_MODEL to switch provider.
const SYSTEM = `You are a brand-voice reviewer for Inkloom AI. Brand tone: authoritative yet approachable, concise, technically rigorous, empathetic. Forbidden tones: hyperbolic/salesy, overly casual/slang, sarcastic, pessimistic.
Review the marketing copy. Reply ONLY with JSON: {"score":0-100,"verdict":"on-brand"|"needs-work"|"off-brand","summary":"one sentence","issues":[{"quote":"short exact excerpt","problem":"why it breaks the tone","rewrite":"suggested rewrite"}]}
Max 5 issues. Do not invent product facts, prices or certifications.`;

module.exports = async (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  if (req.method !== 'POST') return res.status(405).json({ error: 'POST only' });
  const key = process.env.AI_API_KEY || process.env.GEMINI_API_KEY;
  if (!key) return res.status(503).json({ error: 'AI_API_KEY is not set on the server.' });
  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  const text = String((body && body.text) || '').slice(0, 4000);
  if (!text.trim()) return res.status(400).json({ error: 'text is required' });
  const base = (process.env.AI_BASE_URL || 'https://generativelanguage.googleapis.com/v1beta/openai').replace(/\/$/, '');
  const model = process.env.AI_MODEL || 'gemini-2.5-flash';
  try {
    const r = await fetch(base + '/chat/completions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key },
      body: JSON.stringify({
        model,
        temperature: 0.2,
        messages: [{ role: 'system', content: SYSTEM }, { role: 'user', content: text }]
      })
    });
    const data = await r.json();
    if (!r.ok) { const e = Array.isArray(data) ? data[0] : data; return res.status(502).json({ error: 'Provider ' + r.status + ': ' + (((e && e.error && e.error.message) || JSON.stringify(data)) + '').slice(0, 300) }); }
    const raw = data.choices[0].message.content;
    const m = raw.match(/\{[\s\S]*\}/);
    return res.status(200).json(JSON.parse(m ? m[0] : raw));
  } catch (e) {
    return res.status(500).json({ error: 'AI review failed: ' + e.message });
  }
};
