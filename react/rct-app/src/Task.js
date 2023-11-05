import React from "react";
import "./Task.css";
export function TaskCard({ ready }) {
  // const cardStyles = { background: "#202020", color: "#fff", padding: "20px" };

  return (
    // <div style={cardStyles}>
    <div className="card">
      <h1>Mi primera tarea</h1>
      <span className={ready ? "bg-green" : "bg-red"}>
        {ready ? "tarea lista" : "tarea pendiente"}
      </span>
    </div>
  );
}
