import { useState } from "react";
import API from "../api";

export default function UserForm() {
  const [form, setForm] = useState({ id: "", name: "", role: "", email: "" });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await API.post("/users", form);
    alert("User added!");
  };

  return (
    <form onSubmit={handleSubmit} className="p-4">
      {["id", "name", "email"].map((f) => (
        <input
          key={f}
          placeholder={f}
          value={form[f]}
          onChange={(e) => setForm({ ...form, [f]: e.target.value })}
          className="m-2 p-2 border"
        />
      ))}
      <select
        value={form.role}
        onChange={(e) => setForm({ ...form, role: e.target.value })}
        className="m-2 p-2 border"
      >
        <option value="">Role</option>
        <option value="participant">Participant</option>
        <option value="judge">Judge</option>
      </select>
      <button className="bg-blue-500 text-white px-4 py-2">Submit</button>
    </form>
  );
}
