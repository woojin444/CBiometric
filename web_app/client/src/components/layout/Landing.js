import React, { Component } from "react";
// import { Link } from "react-router-dom";

class Landing extends Component {
  render() {
    return (
      <div className="landing">
        <div className="dark-overlay landing-inner text-light">
          <div className="container">
            <div className="row">
              <div className="col-md-12 text-center">
                <h1 className="display-3 mb-4">Biometix Face Miner</h1>
                <p className="lead">
                  {" "}
                  The purpose of this application is to find an individual on
                  the internet using face recognition. This tool will mine the
                  web for the faces of Persons of Interest (POI). This will
                  enable intelligence and law enforcement to more effectively
                  find people using technology.
                </p>
                <hr />
                {/* <Link to="/register" className="btn btn-lg btn-info mr-2">
                  Sign 
                </Link>
                <Link to="/login" className="btn btn-lg btn-light">
                  Login 
                </Link> */}
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Landing;
