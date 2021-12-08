const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// Create Schema
const UploadSchema = new Schema({
  filename: {
    type: String,
    required: true
  },
  filesize: {
    type: String,
    required: true
  },
  date: {
    type: Date,
    default: Date.now
  }
});

module.exports = User = mongoose.model("upload", UploadSchema);
