export default function handler(req, res) {
  const beat = {
    heartbeat: "💓",
    status: "vivo",
    timestamp: new Date().toISOString(),
    node: "vaelir-core",
    uptime: `${process.uptime().toFixed(2)}s`
  };

  res.status(200).json(beat);
}
