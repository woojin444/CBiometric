import React, { Component } from "react";
import axios from "axios";
import swal from "sweetalert";

class ReportDownload extends Component {
  constructor(props) {
    super(props);
    this.state = { showPDF: false, file: "" };
    this.setState = this.setState.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);

    axios({
      method: "post",
      url: "http://localhost:5000/api/download/report",
      data: data
    })
      .then(response => {
        //handle success
        this.setState({
          showPDF: true,
          file: response.data
        });
        window.open(response.data);
      })
      .catch(function(response) {
        //handle error
        swal({ title: "Your report can't be found, please check again later." });
        console.log(response);
      });
  }

  render() {
    return (
      <div>
        <div align="center">
          <form onSubmit={this.handleSubmit}>
            <label htmlFor="username">Enter report id</label>
            <input type="text" id="reportID" name="reportID" required />

            <button>Send data!</button>
          </form>
        </div>
      </div>
    );
  }
}
export default ReportDownload;
