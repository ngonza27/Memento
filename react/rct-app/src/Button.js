import React from "react";
import PropTypes from "prop-types";

export function Button(props) {
  let { text, name } = props;
  return (
    <button>
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
