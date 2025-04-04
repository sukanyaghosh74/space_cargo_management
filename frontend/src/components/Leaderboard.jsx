import { useEffect, useState } from "react";
import API from "../api";

export default function Leaderboard() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("/leaderboard").then((res) => setData(res.data));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">Leaderboard</h2>
      <ul>
        {data.map((entry, i) => (
          <li key={i} className="mb-1">
            {entry.name} – Score: {entry.total_score.toFixed(2)}
          </li>
        ))}
      </ul>
    </div>
  );
}
