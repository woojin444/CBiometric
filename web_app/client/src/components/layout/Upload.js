import React, { Component } from "react";
import Dropzone from "react-dropzone";
import axios from "axios";

import swal from "sweetalert";

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = { files: [] };
  }

  sendImage(upload, data) {
    axios
      .post("http://localhost:5000/api/upload/image", data)
      .then(function(response) {
        var text_output =
          "The process is on the way, please remember this id: \n" +
          response.data +
          "\n" +
          "You will need this id to access the report later. \n" +
          "The waiting process normally takes 1 hour.";

        swal({
          title: response.data,
          text: text_output,
          showCancelButton: false,
          showConfirmButton: false
        });
      })
      .catch(function(error) {
        console.log(error);
      });
  }

  onImageDrop(files) {
    // popup
    swal({
      title: "Uploaded successfully",
      text: "Click OK, if you want to identify the image",
      icon: "success",
      buttons: true,
      dangerMode: true
    }).then(willDelete => {
      if (willDelete) {
        const data = new FormData();
        data.append("file", this.state.files[0]);
        data.append("filename", this.state.files[0].name);
        this.sendImage(this, data);
      } else {
        swal("Your imaginary file is safe!");
      }
    });

    this.setState({
      toPreview: false,
      files
    });
  }

  render() {
    return (
      <div align="center">
        <h1>
          Upload a photo to start searching.
          <br />
          <br />
        </h1>
        <div className="FileUpload">
          <Dropzone
            onDrop={this.onImageDrop.bind(this)}
            multiple={false}
            accept="image/*"
          >
            <div>Drop an image or click to select a file to upload.</div>
          </Dropzone>
        </div>
        <aside>
          <h2>Dropped files</h2>
          <ul>
            {this.state.files.map(f => (
              <li key={f.name}>
                {f.name} - {f.size} bytes
              </li>
            ))}
          </ul>
        </aside>
      </div>
    );
  }
}

export default Upload;
