import { useState } from "react";
import API from "../api";

export default function ReviewForm() {
  const [form, setForm] = useState({
    judge_id: "",
    submission_id: "",
    comments: "",
    ratings: {
      Innovation: 0,
      Feasibility: 0,
      Impact: 0,
      Presentation: 0,
    }
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await API.post("/review", form);
    alert("Review submitted!");
  };

  const updateRating = (key, value) => {
    setForm({ ...form, ratings: { ...form.ratings, [key]: value } });
  };

  return (
    <form onSubmit={handleSubmit} className="p-4">
      {["judge_id", "submission_id", "comments"].map((f) => (
        <input
          key={f}
          placeholder={f}
          value={form[f]}
          onChange={(e) => setForm({ ...form, [f]: e.target.value })}
          className="m-2 p-2 border"
        />
      ))}
      {Object.keys(form.ratings).map((c) => (
        <input
          key={c}
          type="number"
          placeholder={c}
          value={form.ratings[c]}
          onChange={(e) => updateRating(c, Number(e.target.value))}
          className="m-2 p-2 border"
        />
      ))}
      <button className="bg-yellow-500 text-white px-4 py-2">Submit Review</button>
    </form>
  );
}
