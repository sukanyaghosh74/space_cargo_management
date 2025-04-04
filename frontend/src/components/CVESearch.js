import React, { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

const CVESearch = () => {
  const [cveID, setCveID] = useState("");
  const [cveData, setCveData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    if (!cveID) return;
    setLoading(true);
    setError(null);
    setCveData(null);

    try {
      const response = await axios.get(`http://127.0.0.1:5000/cve/${cveID}`);
      setCveData(response.data);
    } catch (err) {
      setError("CVE not found or API error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">CVE Search</h2>
      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Enter CVE ID (e.g., CVE-2023-1234)"
          value={cveID}
          onChange={(e) => setCveID(e.target.value)}
        />
        <button className="btn btn-primary" onClick={handleSearch}>
          Search
        </button>
      </div>

      {loading && <p>Loading...</p>}
      {error && <p className="text-danger">{error}</p>}
      {cveData && (
        <div className="card p-3">
          <h4>{cveData.id}</h4>
          <p><strong>Description:</strong> {cveData.description}</p>
          <p><strong>Severity:</strong> {cveData.severity}</p>
          <p><strong>Published Date:</strong> {cveData.published}</p>
          <p><strong>Last Modified:</strong> {cveData.last_modified}</p>
          <a href={cveData.references[0]} target="_blank" rel="noopener noreferrer">
            View CVE Details
          </a>
        </div>
      )}
    </div>
  );
};

export default CVESearch;
