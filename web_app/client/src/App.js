import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import Navbar from "./components/layout/Navbar";
import Footer from "./components/layout/Footer";
import Landing from "./components/layout/Landing";
// import LandingSideBar from "./components/layout/LandingSideBar"
import Upload from "./components/layout/Upload";
import Register from "./components/auth/Register";
import Login from "./components/auth/Login";
import PreviewPDF from "./components/layout/PreviewPDF";
import ReportDownload from "./components/layout/ReportDownload";

import "./App.css";

class App extends Component {
  render() {
    return (
      <Router>
        <div className="App Site">
          <Navbar />
          <Route exact path="/" component={Landing} />
          <div className="container Site-content">
            <Route exact path="/register" component={Register} />
            <Route exact path="/login" component={Login} />
            <Route exact path="/upload" component={Upload} />
            <Route exact path="/preview" component={PreviewPDF} />
            <Route exact path="/report" component={ReportDownload} />
            {/* <Route exact path="/SideBar" component={LandingSideBar} /> */}

          </div>
          <Footer />
        </div>
      </Router>
    );
  }
}

export default App;
