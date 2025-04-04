import { useState } from "react";
import API from "../api";

export default function SubmissionForm() {
  const [form, setForm] = useState({ user_id: "", event_id: "" });
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    data.append("user_id", form.user_id);
    data.append("event_id", form.event_id);
    data.append("file", file);
    await API.post("/submit", data);
    alert("Submission uploaded!");
  };

  return (
    <form onSubmit={handleSubmit} className="p-4">
      {["user_id", "event_id"].map((f) => (
        <input
          key={f}
          placeholder={f}
          value={form[f]}
          onChange={(e) => setForm({ ...form, [f]: e.target.value })}
          className="m-2 p-2 border"
        />
      ))}
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="m-2" />
      <button className="bg-green-500 text-white px-4 py-2">Submit Project</button>
    </form>
  );
}
