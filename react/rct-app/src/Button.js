import React from "react";
import PropTypes from "prop-types";

export function Button(props) {
  let { text, name } = props;
  return (
    <button
      onClick={function () {
        console.log("Hola mundo");
      }}
    >
      {text} - {name}
    </button>
  );
}

Button.propTypes = {
  text: PropTypes.string.isRequired,
};

Button.defaultProps = {
  name: "some_name",
};
