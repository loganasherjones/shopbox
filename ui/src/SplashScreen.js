import React from "react";
import PropTypes from "prop-types";
import classNames from "classnames";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import { withStyles } from "@material-ui/core/styles";
import ProjectCard from "./components/ProjectCard";
import Hero from "./components/Hero";

const styles = theme => ({
  layout: {
    width: "auto",
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    [theme.breakpoints.up(1100 + theme.spacing.unit * 3 * 2)]: {
      width: 1100,
      marginLeft: "auto",
      marginRight: "auto",
    },
  },
  cardGrid: {
    padding: `${theme.spacing.unit * 8}px 0`,
  },
});

const projects = [
  {
    name: "project1",
    displayName: "Project 1",
    shortDescription:
      "This is a project. Here, you would put your project tagline or short description.",
  },
  {
    name: "project2",
    displayName: "Project 2",
    shortDescription:
      "This is a project. Here, you would put your project tagline or short description.",
  },
  {
    name: "project3",
    displayName: "Project 3",
    shortDescription:
      "This is a project. Here, you would put your project tagline or short description.",
  },
  {
    name: "project4",
    displayName: "Project 4",
    shortDescription:
      "This is a project. Here, you would put your project tagline or short description.",
  },
];

function SplashScreen(props) {
  const { classes } = props;

  return (
    <>
      <Hero />
      <div className={classNames(classes.layout, classes.cardGrid)}>
        <Grid container spacing={32}>
          <Grid item xs={12}>
            <Typography variant="h4">Recently Published Software</Typography>
          </Grid>
          {projects.map(project => (
            <Grid item key={project.name} sm={6} md={4} lg={3}>
              <ProjectCard project={project} />
            </Grid>
          ))}
        </Grid>
      </div>
    </>
  );
}

SplashScreen.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SplashScreen);
