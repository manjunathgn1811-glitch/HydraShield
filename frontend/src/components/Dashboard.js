import React, { useEffect, useState } from "react";
import api from "../services/api";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function Dashboard() {

  const [stats, setStats] = useState({
    blocked_ips: 0,
    honeypot_hits: 0,
    anomalies: 0,
    threat_feed_matches: 0
  });

  const [health, setHealth] = useState({});

  const [incidents, setIncidents] = useState([]);

  useEffect(() => {

    loadDashboard();

  }, []);

  const loadDashboard = () => {

    api.get("/dashboard/stats")
      .then((res) => {
        setStats(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

    api.get("/dashboard/health")
      .then((res) => {
        setHealth(res.data);
      })
      .catch((err) => {
        console.log(err);
      });

    api.get("/dashboard/incidents")
      .then((res) => {
        setIncidents(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const chartData = {
    labels: [
      "Blocked IPs",
      "Honeypot Hits",
      "AI Anomalies",
      "Threat Feed Matches"
    ],
    datasets: [
      {
        label: "HydraShield Security Metrics",
        data: [
          stats.blocked_ips,
          stats.honeypot_hits,
          stats.anomalies,
          stats.threat_feed_matches
        ]
      }
    ]
  };

  return (
    <div
      style={{
        padding: "20px",
        backgroundColor: "#f4f6f9",
        minHeight: "100vh"
      }}
    >
      <h1>🛡 HydraShield Security Dashboard</h1>

      {/* STAT CARDS */}

      <div
        style={{
          display: "flex",
          gap: "20px",
          flexWrap: "wrap",
          marginTop: "20px"
        }}
      >
        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "10px",
            minWidth: "220px"
          }}
        >
          <h3>Blocked IPs</h3>
          <h2>{stats.blocked_ips}</h2>
        </div>

        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "10px",
            minWidth: "220px"
          }}
        >
          <h3>Honeypot Hits</h3>
          <h2>{stats.honeypot_hits}</h2>
        </div>

        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "10px",
            minWidth: "220px"
          }}
        >
          <h3>AI Anomalies</h3>
          <h2>{stats.anomalies}</h2>
        </div>

        <div
          style={{
            background: "white",
            padding: "20px",
            borderRadius: "10px",
            minWidth: "220px"
          }}
        >
          <h3>Threat Feed Matches</h3>
          <h2>{stats.threat_feed_matches}</h2>
        </div>
      </div>

      {/* CHART */}

      <div
        style={{
          background: "white",
          marginTop: "30px",
          padding: "20px",
          borderRadius: "10px"
        }}
      >
        <h2>Security Analytics</h2>

        <Bar data={chartData} />
      </div>

      {/* SYSTEM HEALTH */}

      <div
        style={{
          background: "white",
          marginTop: "30px",
          padding: "20px",
          borderRadius: "10px"
        }}
      >
        <h2>System Health</h2>

        <p>
          <strong>Status:</strong> {health.status}
        </p>

        <p>
          <strong>Database:</strong> {health.database}
        </p>

        <p>
          <strong>Threat Feed:</strong> {health.threat_feed}
        </p>

        <p>
          <strong>Server:</strong> {health.server}
        </p>
      </div>

      {/* AI ALERTS */}

      <div
        style={{
          background: "#fff3cd",
          marginTop: "30px",
          padding: "20px",
          borderRadius: "10px"
        }}
      >
        <h2>🚨 AI Security Alerts</h2>

        <ul>
          <li>Monitor unusual traffic spikes</li>
          <li>Review threat feed matches</li>
          <li>Investigate honeypot triggers</li>
          <li>Analyze anomaly detection results</li>
        </ul>
      </div>

      {/* INCIDENT TABLE */}

      <div
        style={{
          background: "white",
          marginTop: "30px",
          padding: "20px",
          borderRadius: "10px"
        }}
      >
        <h2>Recent Security Incidents</h2>

        <table
          border="1"
          cellPadding="10"
          width="100%"
        >
          <thead>
            <tr>
              <th>ID</th>
              <th>Event</th>
              <th>Severity</th>
              <th>IP Address</th>
              <th>Timestamp</th>
            </tr>
          </thead>

          <tbody>
            {incidents.length > 0 ? (
              incidents.map((item, index) => (
                <tr key={index}>
                  <td>{item.id}</td>
                  <td>{item.event}</td>
                  <td>{item.severity}</td>
                  <td>{item.source_ip}</td>
                  <td>{item.timestamp}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5">
                  No incidents recorded
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Dashboard;