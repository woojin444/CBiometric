const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// Create Schema
const DownloadSchema = new Schema({
  caseID: {
    type: String,
    required: true
  }
});

module.exports = User = mongoose.model("download", DownloadSchema);
