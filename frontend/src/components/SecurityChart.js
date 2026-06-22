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

function SecurityChart() {

  const data = {
    labels: [
      "Blocked IPs",
      "Honeypot Hits",
      "Anomalies",
      "Threat Matches"
    ],
    datasets: [
      {
        label: "Security Metrics",
        data: [12, 5, 2, 1]
      }
    ]
  };

  return (
    <div style={{ width: "700px" }}>
      <Bar data={data} />
    </div>
  );
}

export default SecurityChart;