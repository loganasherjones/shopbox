import React, { Component } from "react";
import PropTypes from "prop-types";
import { withRouter } from "react-router-dom";
import Typography from "@material-ui/core/Typography";

class ProjectView extends Component {
  render() {
    const {
      match: {
        params: { projectName },
      },
    } = this.props;
    return (
      <Typography variant="h3">
        TODO: Render the {projectName} Project Page.
      </Typography>
    );
  }
}

export default withRouter(ProjectView);
