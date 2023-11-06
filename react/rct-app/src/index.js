import React from "react";
import ReactDOM from "react-dom/client";
import { Posts } from "./Posts";
const root = ReactDOM.createRoot(document.getElementById("root"));

const users = [
  { id: 1, name: "Alberto", image: "https://robohash.org/user1" },
  { id: 2, name: "Carlos", image: "https://robohash.org/user2" },
];

root.render(
  <>
    <Posts />
    {users.map((obj, i) => {
      return (
        <div key={i}>
          <h1>{obj.name}</h1>
          <img src={obj.image} />
        </div>
      );
    })}
  </>
);
