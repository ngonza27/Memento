import React from "react";
import ReactDOM from "react-dom/client";
import { Greeting, UserCard } from "./Greeting";
import Product, { Navbar } from "./Product";
const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <>
    <Greeting title="Dove" a="Go" />
    <UserCard
      name="name"
      amount={300}
      married={true}
      points={[1, 2, 3]}
      address={{ street: "123 main street", city: "london" }}
      greet={function () {
        alert("Hello");
      }}
    />
  </>
);
