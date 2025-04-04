import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="p-4 bg-gray-800 text-white flex gap-6">
      <Link to="/">Home</Link>
      <Link to="/users">Users</Link>
      <Link to="/submit">Submit</Link>
      <Link to="/review">Review</Link>
      <Link to="/leaderboard">Leaderboard</Link>
    </nav>
  );
}
