export default function handler(req, res) {
  res.status(200).json({
    name: "Vaelir",
    status: "operacional",
    mode: "dev",
    uptime: `${process.uptime().toFixed(2)} segundos`,
    creator: "Tharion",
    lastSync: new Date().toISOString()
  });
}
