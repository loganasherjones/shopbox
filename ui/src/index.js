import React from "react";
import { render } from "react-dom";
import { Provider } from "react-redux";
import "typeface-roboto";
import { BrowserRouter as Router } from "react-router-dom";
import CssBaseline from "@material-ui/core/CssBaseline";
import configureStore from "./store/configureStore";
import App from "./App";

const store = configureStore();

render(
  <Provider store={store}>
    <Router>
      <>
        <CssBaseline />
        <App />
      </>
    </Router>
  </Provider>,
  document.getElementById("root"),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
