import React from "react";
import ReactDOM from "react-dom/client";
import { Greeting, User } from "./Greeting";
import Product, { Navbar } from "./Product";
const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <>
    <Greeting></Greeting>
    <User />
    <Product />
    <Navbar />
  </>
);
