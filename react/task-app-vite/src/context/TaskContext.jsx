import React from "react";

function TaskContext(props) {
  return (
    <>
      <h1>Componente context</h1>
      {props.children}
    </>
  );
}

export default TaskContext;
